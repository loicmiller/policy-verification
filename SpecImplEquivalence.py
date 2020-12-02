###############################################################################
# Imports

import sys
import argparse # Argument parser

from mgtoolkit.library import *
import networkx as nx
import matplotlib.pyplot as plt

from random import randrange

from sympy import to_dnf
from sympy.parsing.sympy_parser import parse_expr

import ast # String to dict
from importlib import import_module # Import policy metagraph

import cProfile
import pstats
import io

from pprint import pprint


from collections import deque # Popping first elements of list


###############################################################################
# General utility

# Exit the program
def terminate_app(code):
    print("Exiting program...")
    sys.exit(code)


###############################################################################
# Argument parser

class Range(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def __eq__(self, other):
        return self.start <= other <= self.end

def get_parser():
    # Get parser for command line arguments
    parser = argparse.ArgumentParser(description="Metagraph equivalence of specification vs implementation", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--version", action="version", version='%(prog)s 1.0')
    parser.add_argument("-v", "--verbose", action="count", default=0, help="increase output verbosity")
    parser.add_argument("specification", type=str, metavar="FILE", help="workflow specification to use for verification")
    parser.add_argument("implementation", type=str, metavar="FILE", help="metagraph implementation to use for verification")
    parser.add_argument("-o", "--output-file", type=str, metavar="OUTPUT_FILE", default="measures/equivalence.dat", help="path to output file")
    parser.add_argument("-c", "--check", action="store_true", help="Check that the comparison returns the right result")

    return parser


###############################################################################
# Functions

def load_spec_from_file(specification):
    print("\n\n###############################################################################")
    print("Loading workflow specification from file")
    print("###############################################################################")

    with open(specification, 'r') as specification_file:
        workflow_edges = specification_file.readlines()
        workflow_edges = [(set(src.lstrip('{').rstrip('}').split(', ')), set(dst.lstrip('{').rstrip('}').split(', ')), attributes) for src, dst, attributes in (edge.rstrip().split(';') for edge in workflow_edges)]

    if glob_verbose >= 1:
        print("Edges")
        for edge in workflow_edges:
            print(edge)

    return workflow_edges


def spec_graph_to_metagraph(specification_edges):
    print("\n\n###############################################################################")
    print("Turning specification graph into metagraph")
    print("###############################################################################")

    workflow_variable_set = set()
    workflow_propositions_set = set()
    workflow_metagraph_edges = []

    # Simplify boolean expressions (Use simpy) https://stackoverflow.com/questions/52416781/how-to-simplify-these-boolean-statements
    for src, dst, attributes in specification_edges:
        if glob_verbose >= 2:
            print("Edge: {} {} {}".format(src, dst, attributes))

        # Add src and dst to variable set if they are not present yet
        workflow_variable_set.update(src)
        workflow_variable_set.update(dst)

        # Parse policy into expression for sympy
        edge_policy = parse_expr(attributes)
        if glob_verbose >= 2:
            print("Edge policy: {}".format(edge_policy))

        # Convert policy to Disjunctive Normal Form (DNF)
        # I think we don't want to simplify the expression for the comparison
        # since it is not simplified in the metagraph generated from the policy
        # https://en.wikipedia.org/wiki/Disjunctive_normal_form
        # https://docs.sympy.org/latest/modules/logic.html
        # https://docs.sympy.org/latest/modules/parsing.html
        edge_policy_dnf = to_dnf(edge_policy, simplify=False)
        if glob_verbose >= 2:
            print("DNF: {}".format(edge_policy_dnf))

        # Metagraph nodes
        # Each element in metagraph_nodes is the proposition part of a node in the metagraph
        metagraph_nodes = str(edge_policy_dnf).split("|")
        if glob_verbose >= 2:
            print("Metagraph nodes: {}".format(metagraph_nodes))

        # Policy elements in nodes
        # Each element is a part of the propositions_set
        for node_propositions in metagraph_nodes:
            policy_elements = node_propositions.split('&')
            policy_elements = [policy_element.strip().lstrip('(').rstrip(')') for policy_element in policy_elements] # Remove leading and trailing whitespaces, plus leading and trailing parentheses

            # Add policy_elements to propositions_set
            for index, policy_element in enumerate(policy_elements):
                # Add ')' back for equalities
                if 'Eq' in policy_element:
                    policy_element = policy_element + ')'
                    policy_elements[index] = policy_elements[index] + ')'
                workflow_propositions_set.add(policy_element)
            workflow_metagraph_edges.append(Edge(src, dst, attributes=policy_elements))

            if glob_verbose >= 2:
                print("Policy elements: {}".format(policy_elements))

        if glob_verbose >= 2:
            print("\n")


    if glob_verbose >= 1:
        print("Variable set: {}".format(workflow_variable_set))
        print("Propositions set: {}\n".format(workflow_propositions_set))
        print("Metagraph edges: {}\n".format(workflow_metagraph_edges))

    # Create workflow metagraph
    specification_metagraph = ConditionalMetagraph(workflow_variable_set, workflow_propositions_set)
    specification_metagraph.add_edges_from(workflow_metagraph_edges)

    if glob_verbose >= 1:
        print("Specification metagraph\n{}\n".format(repr(specification_metagraph)))

    if glob_verbose >= 2:
        print("Specification metagraph edges")
        print("{} {}".format("INVERTEX", "OUTVERTEX"))
        for edge in specification_metagraph.edges:
            print("{} {}".format(list(edge.invertex), list(edge.outvertex)))

    return specification_metagraph


def load_impl_from_file(implementation):
    print("\n\n###############################################################################")
    print("Importing implementation metagraph configuration")
    print("###############################################################################")

    implementation_chunks = implementation.split('/') # impl-metagraph-generators/generated-from-random/50-nodes-0-3-edges-5-policy-0-25-error/23-1.py
    full_module_name = "impl-metagraph-generators.generated-from-random." + implementation_chunks[-2] + "." + implementation_chunks[-1].split('.')[0]
    policy = import_module(full_module_name)
    implementation_mg_constructor = policy.generate_metagraph()

    print("Imported implementation metagraph\n")

    return implementation_mg_constructor


def impl_metagraph_constructor_to_metagraph(implementation_metagraph_constructor):
    print("\n\n###############################################################################")
    print("Generating implementation metagraph")
    print("###############################################################################")

    # Cleaning up
    for prop in implementation_metagraph_constructor.propositions:
        if prop in implementation_metagraph_constructor.variables:
            implementation_metagraph_constructor.variables.remove(prop)

    variable_set = set(implementation_metagraph_constructor.variables)
    propositions_set = set(implementation_metagraph_constructor.propositions)

    if glob_verbose >= 1:
        print("Variable set: {}".format(variable_set))
        print("Propositions set: {}\n".format(propositions_set))
        print("Metagraph edges: {}\n".format(implementation_metagraph_constructor.edges))

    # Create policy metagraph
    implementation_metagraph = ConditionalMetagraph(variable_set, propositions_set)
    implementation_metagraph.add_edges_from(implementation_metagraph_constructor.edges)

    if glob_verbose >= 1:
        print("Implementation metagraph\n{}\n".format(repr(implementation_metagraph)))

    if glob_verbose >= 2:
        print("Implementation metagraph edges")
        print("{} {}".format("INVERTEX", "OUTVERTEX"))
        for edge in implementation_metagraph.edges:
            print("{} {}".format(list(edge.invertex), list(edge.outvertex)))

    return implementation_metagraph


def impl_metagraph_transform(implementation_metagraph):
    print("\n\n###############################################################################")
    print("Transforming implementation metagraph to be specification-like")
    print("###############################################################################")

    # Clean up irrelevant edges
    edges_to_remove = set()
    for implementation_edge in implementation_metagraph.edges:
        # Clean up edges with outvertex != 'allow'
        if 'allow' not in repr(implementation_edge.outvertex):
            if glob_verbose >= 2:
                print("Edge to remove: {}".format(implementation_edge))
            edges_to_remove.add(implementation_edge)

        # Clean up edges with only rule_x in invertex
        attributes = list(implementation_edge.invertex)
        if len(attributes) == 1 and [attribute for attribute in attributes if 'rule_' in attribute]:
            if glob_verbose >= 2:
                print("Edge to remove: {}".format(implementation_edge))
            edges_to_remove.add(implementation_edge)
    implementation_metagraph.remove_edges_from(edges_to_remove)

    # Transform edges
    transformed_variable_set = set()
    transformed_propositions_set = set()
    transformed_implementation_edges = []
    for implementation_edge in implementation_metagraph.edges:
        if glob_verbose >= 2:
            print("Original invertex: {}".format(implementation_edge.invertex))
            print("Original outvertex: {}".format(implementation_edge.outvertex))

        attributes = list(implementation_edge.invertex)
        transformed_invertex = []
        transformed_outvertex = []
        transformed_attributes = []

        for attribute in attributes:
            # Match equals
            if '==' in attribute:
                left_eq, right_eq = attribute.split("==")
                if left_eq == "user_name":
                    transformed_invertex.append(right_eq.strip('"'))
                    transformed_variable_set.add(right_eq.strip('"'))
                elif left_eq == "http_request.path":
                    transformed_outvertex.append(right_eq.strip('"').split('/')[-1])
                    transformed_variable_set.add(right_eq.strip('"').split('/')[-1])
                elif left_eq == "http_request.method":
                    transformed_attributes.append("Eq(method, {})".format(right_eq.strip('"')))
                    transformed_propositions_set.add("Eq(method, {})".format(right_eq.strip('"')))
            # Match comparison operators
            elif '>=' in attribute:
                left_eq, right_eq = attribute.split(">=")
                if left_eq == "user.tenure":
                    transformed_attributes.append("tenure >= {}".format(right_eq))
                    transformed_propositions_set.add("tenure >= {}".format(right_eq))
                elif "current_time" in left_eq:
                    transformed_attributes.append("time >= {}".format(right_eq))
                    transformed_propositions_set.add("time >= {}".format(right_eq))
            elif '<=' in attribute:
                left_eq, right_eq = attribute.split("<=")
                if left_eq == "user.tenure":
                    transformed_attributes.append("tenure <= {}".format(right_eq))
                    transformed_propositions_set.add("tenure <= {}".format(right_eq))
                elif "current_time" in left_eq:
                    transformed_attributes.append("time <= {}".format(right_eq))
                    transformed_propositions_set.add("time <= {}".format(right_eq))
            elif '>' in attribute:
                left_eq, right_eq = attribute.split(">")
                if left_eq == "user.tenure":
                    transformed_attributes.append("tenure > {}".format(right_eq))
                    transformed_propositions_set.add("tenure > {}".format(right_eq))
                elif "current_time" in left_eq:
                    transformed_attributes.append("time > {}".format(right_eq))
                    transformed_propositions_set.add("time > {}".format(right_eq))
            elif '<' in attribute:
                left_eq, right_eq = attribute.split("<")
                if left_eq == "user.tenure":
                    transformed_attributes.append("tenure < {}".format(right_eq))
                    transformed_propositions_set.add("tenure < {}".format(right_eq))
                elif "current_time" in left_eq:
                    transformed_attributes.append("time < {}".format(right_eq))
                    transformed_propositions_set.add("time < {}".format(right_eq))
            elif 'is_' in attribute: # prop
                transformed_attributes.append(attribute)
                transformed_propositions_set.add(attribute)

        if glob_verbose >= 2:
            print("Transformed invertex: {}".format(transformed_invertex))
            print("Transformed outvertex: {}".format(transformed_outvertex))
            print("Transformed attributes: {}\n".format(transformed_attributes))

        # Add transformed edge to transformed_implementation_edges
        transformed_implementation_edges.append(Edge(set(transformed_invertex), set(transformed_outvertex), attributes=transformed_attributes))

    if glob_verbose >= 1:
        print("Transformed variable set: {}".format(transformed_variable_set))
        print("Transformed propositions set: {}\n".format(transformed_propositions_set))
        print("Transformed metagraph edges: {}\n".format(transformed_implementation_edges))

    transformed_implementation_metagraph = ConditionalMetagraph(transformed_variable_set, transformed_propositions_set)
    transformed_implementation_metagraph.add_edges_from(transformed_implementation_edges)

    if glob_verbose >= 1:
        print("Transformed implementation metagraph\n{}\n".format(repr(transformed_implementation_metagraph)))

    if glob_verbose >= 2:
        print("Transformed implementation metagraph edges")
        print("{} {}".format("INVERTEX", "OUTVERTEX"))
        for edge in transformed_implementation_metagraph.edges:
            print("{} {}".format(list(edge.invertex), list(edge.outvertex)))

    return transformed_implementation_metagraph


# Transform to triple list format (src,dst,attrs)
def metagraph_to_edge_triples(metagraph):
    metagraph_triples = []
    for edge in metagraph.edges:
        if glob_verbose >= 2:
            print(edge, edge.attributes)
        metagraph_triples.append((list({src for src in list(edge.invertex) if src not in edge.attributes}), list(edge.outvertex), set(edge.attributes)))
    if glob_verbose >= 2:
        for triple in metagraph_triples:
            print(triple)

    return metagraph_triples


def compare_metagraphs(specification_metagraph_triples, implementation_metagraph_triples):
    new_triples = []
    for triple in specification_metagraph_triples:
        new_triples.append((sorted(triple[0]), sorted(triple[1]), triple[2]))
    specification_metagraph_triples = new_triples

    new_triples = []
    for triple in implementation_metagraph_triples:
        new_triples.append((sorted(triple[0]), sorted(triple[1]), triple[2]))
    implementation_metagraph_triples = new_triples

    # Sort triples
    specification_edges = deque(sorted(specification_metagraph_triples))
    implementation_edges = deque(sorted(implementation_metagraph_triples))
    #specification_edges = sorted(specification_metagraph_triples, key=lambda element: (element[0], element[1]))
    #implementation_edges = sorted(implementation_metagraph_triples, key=lambda element: (element[0], element[1]))

    if glob_verbose >= 1:
        print("SPEC")
        for triple in specification_edges:
            print(triple)
        print("\nIMPL")
        for triple in implementation_edges:
            print(triple)
        print("\n")

    # Compare metagraphs by matching edges
    unmatched_specification_edges = []
    unmatched_implementation_edges = []
    for specification_edge in list(specification_edges):
        if glob_verbose >= 2:
            print("Spec edge: {}".format(specification_edge))
        for implementation_edge in list(implementation_edges):
            if glob_verbose >= 2:
                print("Impl edge: {}".format(implementation_edge))

            if specification_edge == implementation_edge:
                if glob_verbose >= 2:
                    print("Matched edges: SPEC={} IMPL={}\n".format(specification_edge, implementation_edge))
                specification_edges.popleft()
                implementation_edges.popleft()
                break
            elif specification_edge[0] < implementation_edge[0] or (specification_edge[0] == implementation_edge[0] and specification_edge[1] < implementation_edge[1]): # (0,1,attr) < (1,1,attr)
                if glob_verbose >= 2:
                    print("Unmatched spec edge: SPEC={} IMPL={}\n".format(specification_edge, implementation_edge))
                unmatched_specification_edges.append(specification_edge)
                specification_edges.popleft()
                break
            elif specification_edge[0] > implementation_edge[0] or (specification_edge[0] == implementation_edge[0] and specification_edge[1] > implementation_edge[1]): # (1,1,attr) > (0,1,attr)
                if glob_verbose >= 2:
                    print("Unmatched impl edge: SPEC={} IMPL={}\n".format(specification_edge, implementation_edge))
                unmatched_implementation_edges.append(implementation_edge)
                implementation_edges.popleft()
            elif specification_edge[0] == implementation_edge[0] and specification_edge[1] == implementation_edge[1] and specification_edge[2] != implementation_edge[2]: # SRC and DST match, but attributes do not
                if glob_verbose >= 2:
                    print("Unmatched attributes: SPEC={} IMPL={}\n".format(specification_edge, implementation_edge))
            else:
                if glob_verbose >= 2:
                    print("No action?: SPEC={} IMPL={}\n".format(specification_edge, implementation_edge))
                    terminate_app(1)

    # Compare metagraphs using dominance
    #if workflow_metagraph.equivalent(transformed_implementation_metagraph):
    #    print("Same metagraphs")
    #else:
    #    print("Different metagraphs")

    if glob_verbose >= 1:
        print("Unmatched edges:")
        print(unmatched_specification_edges)
        print(unmatched_implementation_edges)

    return unmatched_specification_edges, unmatched_implementation_edges


###############################################################################
# Main
def main(verbose, specification, implementation, output_file, check):
    global glob_verbose
    glob_verbose = verbose

    # Load specification from file as graph
    specification_edges = load_spec_from_file(specification)
    spec_len = len(specification_edges)

    # Turning specification graph into metagraph
    specification_mg = spec_graph_to_metagraph(specification_edges)

    # Load implementation from file as metagraph constructor
    implementation_mg_constructor = load_impl_from_file(implementation)

    # Generate implementation metagraph
    implementation_mg = impl_metagraph_constructor_to_metagraph(implementation_mg_constructor)

    # Transform implementation metagraph to be more specification-like
    transformed_implementation_mg = impl_metagraph_transform(implementation_mg)

    # Transform to triple list format (src,dst,attrs)
    specification_mg_triples = metagraph_to_edge_triples(specification_mg)
    implementation_mg_triples = metagraph_to_edge_triples(transformed_implementation_mg)


    print("\n\n###############################################################################")
    print("Comparing specification metagraph to transformed implementation metagraph")
    print("###############################################################################")

    output_stream = io.StringIO()
    profiler_status = pstats.Stats(stream=output_stream)
    profiler = cProfile.Profile()
    profiler.enable()

    # Compare specification to implementation via metagraphs and measure time
    spec_edges, impl_edges = compare_metagraphs(specification_mg_triples, implementation_mg_triples)

    profiler.disable()
    profiler_status.add(profiler)

    if not spec_edges and not impl_edges:
        print("Same metagraph edges")
    else:
        print("Different metagraph edges")

    # Store and print profiling results
    results = vars(profiler_status)
    if glob_verbose >= 3:
        pprint(results)
    if glob_verbose >= 2:
        stats = pstats.Stats(profiler)
        stats.sort_stats('tottime')
        stats.print_stats()

    # Dump measures to file
    implementation_chunks = implementation.split('/') # impl-metagraph-generators/generated-from-random/50-nodes-0-3-edges-5-policy-0-25-error/23-1.py
    parameter_chunks = implementation_chunks[-2].split('-')
    node_number = int(parameter_chunks[0])
    edge_prob = float(parameter_chunks[2] + '.' + parameter_chunks[3])
    policy_size = int(parameter_chunks[5])
    error_rate = float(parameter_chunks[7] + '.' + parameter_chunks[8])
    edge_number = len(specification_mg_triples)

    rego_filepath = "generated-rego-from-spec/generated-from-random/" + implementation_chunks[-2] + "/" + implementation_chunks[-1].split('.')[0] + ".rego"
    rego_lines_of_code = len(open(rego_filepath).readlines())

    stats_keys = results['stats'].keys()
    for stat_key in stats_keys:
        if "compare_metagraphs" in stat_key:
            comp_key = stat_key
    comp_time = results['stats'][comp_key][3]

    sameness = not spec_edges and not impl_edges
    if check:
        if not sameness:
            print("ERROR: Edges are different")
            terminate_app(0)

    with open(output_file, 'a+') as output:
        output.write("{};{};{};{};{};{};{};{};{};{};{};{};{}\n".format(specification, implementation, node_number, edge_prob, policy_size, spec_len, rego_lines_of_code, error_rate, edge_number, comp_time, sameness, spec_edges, impl_edges))


if __name__ == '__main__':
    print("\n\n###############################################################################")
    print("Getting arguments")
    print("###############################################################################")

    parser = get_parser() # Create a parser
    args = parser.parse_args() # Parse arguments
    print(args)

    main(args.verbose, args.specification, args.implementation, args.output_file, args.check)

    terminate_app(0)


###############################################################################
