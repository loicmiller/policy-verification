###############################################################################
# Imports

import sys
import argparse # Argument parser

from mgtoolkit.library import *
import networkx as nx

from sympy import to_dnf
from sympy.parsing.sympy_parser import parse_expr

import random # Random indices of list

import os


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
    parser = argparse.ArgumentParser(description="Workflow specification to Rego", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--version", action="version", version='%(prog)s 1.0')
    parser.add_argument("-v", "--verbose", action="count", default=0, help="increase output verbosity")
    parser.add_argument("workflow", type=str, metavar="FILE", help="workflow to generate policy from")
    parser.add_argument("-e", "--error-rate", type=float, choices=[Range(0.0, 1.0)], metavar="ERROR_RATE", default=0.0, help="rate of errors in the generated workflow")

    return parser


###############################################################################
# Functions

def policy_eq_range(attribute):
    left_eq, right_eq = attribute.split(",")
    left_eq = left_eq[3:]
    right_eq = right_eq.strip().strip(')')

    if left_eq == "method":
        method_range.add(right_eq)

def policy_comp_range(attribute):
    if '>=' in attribute:
        left_eq, right_eq = attribute.split(">=")
    elif '<=' in attribute:
        left_eq, right_eq = attribute.split("<=")
    elif '>' in attribute:
        left_eq, right_eq = attribute.split(">")
    elif '<' in attribute:
        left_eq, right_eq = attribute.split("<")
    left_eq = left_eq.strip()
    right_eq = right_eq.strip()

    if left_eq == "tenure":
        tenure_range.add(right_eq)
    elif left_eq == "time":
        time_range.add(right_eq)

def policy_user_range(attribute):
    user_range.add(attribute)

def policy_prop_range(attribute):
    prop_range.add(attribute)

def policy_dst_range(attribute):
    dst_range.add(attribute)


def policy_eq_add(attribute):
    left_eq, right_eq = attribute.split(",")
    left_eq = left_eq[3:]
    right_eq = right_eq.strip().strip(')')

    if left_eq == "method":
        policy.append('  http_request.method == "{}"\n'.format(right_eq))

# Can change sign to !=
# Can change method to other method
def policy_eq_err(attribute):
    left_eq, right_eq = attribute.split(",")
    left_eq = left_eq[3:]
    right_eq = right_eq.strip().strip(')')

    # Which error? Only allow type 1 for now
    #error_type = random.randrange(2)
    error_type = 1

    if left_eq == "method":
        if error_type == 0: # Change sign to !=
            policy.append('  http_request.method != "{}"\n'.format(right_eq))
        elif error_type == 1: # Change method to other method
            random_method = random.sample(method_range, 1)[0]
            policy.append('  http_request.method != "{}"\n'.format(random_method))


def policy_ge_add(attribute, user_attributes_set, time_set):
    left_eq, right_eq = attribute.split(">=")
    left_eq = left_eq.strip()
    right_eq = right_eq.strip()
    if left_eq == "tenure":
        if not user_attributes_set:
            policy.append('  user:=user_attributes[user_name]\n')
            user_attributes_set = True
        policy.append('  user.tenure >= {}\n'.format(right_eq))
    elif left_eq == "time":
        if not time_set:
            policy.append('  current_time := time.clock([time.now_ns(), "Europe/Paris"])\n')
            time_set = True
        policy.append('  to_number(current_time[0]) >= {}\n'.format(right_eq))

    return user_attributes_set, time_set

# Can change sign
# Can change tenure/time to other tenure/time
def policy_ge_err(attribute, user_attributes_set, time_set):
    left_eq, right_eq = attribute.split(">=")
    left_eq = left_eq.strip()
    right_eq = right_eq.strip()

    # Which error?
    error_type = random.randrange(2)

    if left_eq == "tenure":
        if not user_attributes_set:
            policy.append('  user:=user_attributes[user_name]\n')
            user_attributes_set = True
        if error_type == 0: # Change sign to other sign
            random_sign = random.sample(comp_operators, 1)[0]
            policy.append('  user.tenure {} {}\n'.format(random_sign, right_eq))
        elif error_type == 1: # Change tenure to other tenure
            random_tenure = random.sample(tenure_range, 1)[0]
            policy.append('  user.tenure >= {}\n'.format(random_tenure))
    elif left_eq == "time":
        if not time_set:
            policy.append('  current_time := time.clock([time.now_ns(), "Europe/Paris"])\n')
            time_set = True
        if error_type == 0: # Change sign to other sign
            random_sign = random.sample(comp_operators, 1)[0]
            policy.append('  to_number(current_time[0]) {} {}\n'.format(random_sign, right_eq))
        elif error_type == 1: # Change time to other time
            random_time = random.sample(time_range, 1)[0]
            policy.append('  to_number(current_time[0]) >= {}\n'.format(random_time))

    return user_attributes_set, time_set


def policy_le_add(attribute, user_attributes_set, time_set):
    left_eq, right_eq = attribute.split("<=")
    left_eq = left_eq.strip()
    right_eq = right_eq.strip()
    if left_eq == "tenure":
        if not user_attributes_set:
            policy.append('  user:=user_attributes[user_name]\n')
            user_attributes_set = True
        policy.append('  user.tenure <= {}\n'.format(right_eq))
    elif left_eq == "time":
        if not time_set:
            policy.append('  current_time := time.clock([time.now_ns(), "Europe/Paris"])\n')
            time_set = True
        policy.append('  to_number(current_time[0]) <= {}\n'.format(right_eq))

    return user_attributes_set, time_set

# Can change sign
# Can change tenure/time to other tenure/time
def policy_le_err(attribute, user_attributes_set, time_set):
    left_eq, right_eq = attribute.split("<=")
    left_eq = left_eq.strip()
    right_eq = right_eq.strip()

    # Which error?
    error_type = random.randrange(2)

    if left_eq == "tenure":
        if not user_attributes_set:
            policy.append('  user:=user_attributes[user_name]\n')
            user_attributes_set = True
        if error_type == 0: # Change sign to other sign
            random_sign = random.sample(comp_operators, 1)[0]
            policy.append('  user.tenure {} {}\n'.format(random_sign, right_eq))
        elif error_type == 1: # Change tenure to other tenure
            random_tenure = random.sample(tenure_range, 1)[0]
            policy.append('  user.tenure <= {}\n'.format(random_tenure))
    elif left_eq == "time":
        if not time_set:
            policy.append('  current_time := time.clock([time.now_ns(), "Europe/Paris"])\n')
            time_set = True
        if error_type == 0: # Change sign to other sign
            random_sign = random.sample(comp_operators, 1)[0]
            policy.append('  to_number(current_time[0]) {} {}\n'.format(random_sign, right_eq))
        elif error_type == 1: # Change time to other time
            random_time = random.sample(time_range, 1)[0]
            policy.append('  to_number(current_time[0]) <= {}\n'.format(random_time))

    return user_attributes_set, time_set


def policy_gt_add(attribute, user_attributes_set, time_set):
    left_eq, right_eq = attribute.split(">")
    left_eq = left_eq.strip()
    right_eq = right_eq.strip()
    if left_eq == "tenure":
        if not user_attributes_set:
            policy.append('  user:=user_attributes[user_name]\n')
            user_attributes_set = True
        policy.append('  user.tenure > {}\n'.format(right_eq))
    elif left_eq == "time":
        if not time_set:
            policy.append('  current_time := time.clock([time.now_ns(), "Europe/Paris"])\n')
            time_set = True
        policy.append('  to_number(current_time[0]) > {}\n'.format(right_eq))

    return user_attributes_set, time_set

# Can change sign
# Can change tenure/time to other tenure/time
def policy_gt_err(attribute, user_attributes_set, time_set):
    left_eq, right_eq = attribute.split(">")
    left_eq = left_eq.strip()
    right_eq = right_eq.strip()

    # Which error?
    error_type = random.randrange(2)

    if left_eq == "tenure":
        if not user_attributes_set:
            policy.append('  user:=user_attributes[user_name]\n')
            user_attributes_set = True
        if error_type == 0: # Change sign to other sign
            random_sign = random.sample(comp_operators, 1)[0]
            policy.append('  user.tenure {} {}\n'.format(random_sign, right_eq))
        elif error_type == 1: # Change tenure to other tenure
            random_tenure = random.sample(tenure_range, 1)[0]
            policy.append('  user.tenure > {}\n'.format(random_tenure))
    elif left_eq == "time":
        if not time_set:
            policy.append('  current_time := time.clock([time.now_ns(), "Europe/Paris"])\n')
            time_set = True
        if error_type == 0: # Change sign to other sign
            random_sign = random.sample(comp_operators, 1)[0]
            policy.append('  to_number(current_time[0]) {} {}\n'.format(random_sign, right_eq))
        elif error_type == 1: # Change time to other time
            random_time = random.sample(time_range, 1)[0]
            policy.append('  to_number(current_time[0]) > {}\n'.format(random_time))

    return user_attributes_set, time_set


def policy_lt_add(attribute, user_attributes_set, time_set):
    left_eq, right_eq = attribute.split("<")
    left_eq = left_eq.strip()
    right_eq = right_eq.strip()
    if left_eq == "tenure":
        if not user_attributes_set:
            policy.append('  user:=user_attributes[user_name]\n')
            user_attributes_set = True
        policy.append('  user.tenure < {}\n'.format(right_eq))
    elif left_eq == "time":
        if not time_set:
            policy.append('  current_time := time.clock([time.now_ns(), "Europe/Paris"])\n')
            time_set = True
        policy.append('  to_number(current_time[0]) < {}\n'.format(right_eq))

    return user_attributes_set, time_set

# Can change sign
# Can change tenure/time to other tenure/time
def policy_lt_err(attribute, user_attributes_set, time_set):
    left_eq, right_eq = attribute.split("<")
    left_eq = left_eq.strip()
    right_eq = right_eq.strip()

    # Which error?
    error_type = random.randrange(2)

    if left_eq == "tenure":
        if not user_attributes_set:
            policy.append('  user:=user_attributes[user_name]\n')
            user_attributes_set = True
        if error_type == 0: # Change sign to other sign
            random_sign = random.sample(comp_operators, 1)[0]
            policy.append('  user.tenure {} {}\n'.format(random_sign, right_eq))
        elif error_type == 1: # Change tenure to other tenure
            random_tenure = random.sample(tenure_range, 1)[0]
            policy.append('  user.tenure < {}\n'.format(random_tenure))
    elif left_eq == "time":
        if not time_set:
            policy.append('  current_time := time.clock([time.now_ns(), "Europe/Paris"])\n')
            time_set = True
        if error_type == 0: # Change sign to other sign
            random_sign = random.sample(comp_operators, 1)[0]
            policy.append('  to_number(current_time[0]) {} {}\n'.format(random_sign, right_eq))
        elif error_type == 1: # Change time to other time
            random_time = random.sample(time_range, 1)[0]
            policy.append('  to_number(current_time[0]) < {}\n'.format(random_time))

    return user_attributes_set, time_set


def policy_user_add(attribute):
    policy.append('  user_name == "{}"\n'.format(attribute))

# Can change sign to !=
# Can change user to other user
def policy_user_err(attribute):
    # Which error? Only allow type 1 for now
    #error_type = random.randrange(2)
    error_type = 1

    if error_type == 0: # Change sign to !=
        policy.append('  user_name != "{}"\n'.format(attribute))
    elif error_type == 1: # Change user to other user
        random_user = random.sample(user_range, 1)[0]
        policy.append('  user_name == "{}"\n'.format(random_user))


def policy_prop_add(attribute):
    policy.append('  {}\n'.format(attribute))

# Can change prop to other prop
def policy_prop_err(attribute):
    random_prop = random.sample(prop_range, 1)[0]
    policy.append('  {}\n'.format(random_prop))


def policy_dst_add(attribute):
    policy.append('  http_request.path == "/api/{}"\n'.format(attribute))

# Can change sign to !=
# Can change dst to other dst
def policy_dst_err(attribute):
    # Which error? Only allow type 1 for now
    #error_type = random.randrange(2)
    error_type = 1

    if error_type == 0: # Change sign to !=
        policy.append('  http_request.path != "/api/{}"\n'.format(attribute))
    elif error_type == 1: # Change user to other user
        random_dst = random.sample(dst_range, 1)[0]
        policy.append('  http_request.path == "/api/{}"\n'.format(random_dst))


###############################################################################
# Main

def main(verbose, workflow, error_rate):
    global glob_verbose
    glob_verbose = verbose

    print("\n\n###############################################################################")
    print("Loading workflow specification from file")
    print("###############################################################################")

    with open(workflow, 'r') as workflow_file:
        workflow_edges = workflow_file.readlines()
        workflow_edges = [(set(src.lstrip('{').rstrip('}').split(', ')), set(dst.lstrip('{').rstrip('}').split(', ')), attributes) for src, dst, attributes in (edge.rstrip().split(';') for edge in workflow_edges)]

    if glob_verbose >= 1:
        print("Edges")
        for edge in workflow_edges:
            print(edge)


    print("\n\n###############################################################################")
    print("Turning workflow graph into metagraph")
    print("###############################################################################")

    workflow_variable_set = set()
    workflow_propositions_set = set()
    workflow_metagraph_edges = []

    # Simplify boolean expressions (Use simpy) https://stackoverflow.com/questions/52416781/how-to-simplify-these-boolean-statements
    for src, dst, attributes in workflow_edges:
        if glob_verbose >= 2:
            print("Edge: {} {} {}".format(src, dst, attributes))

        # Add src and dst to variable set if they are not present yet
        workflow_variable_set.update(src)
        workflow_variable_set.update(dst)


        # Parse policy into expression for simpy
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


    if glob_verbose >= 4:
        print("Variable set: {}".format(workflow_variable_set))
        print("Propositions set: {}\n".format(workflow_propositions_set))
        print("Metagraph edges: {}\n".format(workflow_metagraph_edges))

    # Create workflow metagraph
    print("Creating workflow metagraph")
    workflow_metagraph = ConditionalMetagraph(workflow_variable_set, workflow_propositions_set)
    workflow_metagraph.add_edges_from(workflow_metagraph_edges)

    if glob_verbose >= 4:
        print("Policy metagraph\n{}\n".format(repr(workflow_metagraph)))

    if glob_verbose >= 4:
        print("Workflow metagraph edges")
        print("{} {}".format("INVERTEX", "OUTVERTEX"))
        for edge in workflow_metagraph.edges:
            print("{} {}".format(list(edge.invertex), list(edge.outvertex)))


    # For error generation
    number_of_expressions = 0 # How many expressions are there in the metagraph
    for edge in workflow_metagraph.edges:
        number_of_expressions += len(list(edge.invertex)) + len(list(edge.outvertex))
    expressions_map = [0] * number_of_expressions

    if error_rate > 0.0:
        print("\n\n###############################################################################")
        print("Generating errors")
        print("###############################################################################")

        print("Number of expressions in metagraph: {}".format(number_of_expressions))

        number_of_errors = int(round(number_of_expressions * error_rate))
        print("Number of errors to generate: {}".format(number_of_errors))

        if glob_verbose >= 4:
            print(expressions_map)

        error_indices = random.sample(range(0, number_of_expressions), number_of_errors)
        if glob_verbose >= 4:
            print(error_indices)
        if glob_verbose >= 1:
            print("Number of errors indices: {}".format(len(error_indices)))

        for error_index in error_indices:
            expressions_map[error_index] = 1
        if glob_verbose >= 4:
            print(expressions_map)


    print("\n\n###############################################################################")
    print("Generating policy")
    print("###############################################################################")

    # Generate output policy name
    if "manually-generated" in workflow:
        output_policy_name = "generated-rego-from-spec/generated-from-manual/" + workflow.split('.')[0].split('/')[-1] + "-" + str(error_rate).split('.')[0] + "-" + str(error_rate).split('.')[-1] + "-error.rego"
    elif "randomly-generated" in workflow:
        path_chunks = workflow.split("/")
        generated_rego_dir_path = "generated-rego-from-spec/generated-from-random/" + path_chunks[-2] + "-" + str(error_rate).split('.')[0] + "-" + str(error_rate).split('.')[-1] + "-error/"
        if not os.path.exists(generated_rego_dir_path):
            os.makedirs(generated_rego_dir_path)
        print("Rego dir path: {}".format(generated_rego_dir_path))

        # Determine file uid
        file_id = path_chunks[-1].split('.')[0].split('-')[0] + '-'
        if glob_verbose >= 2:
            print("File id: {}".format(file_id))
        random_rego_filenames = [filename for filename in os.listdir(generated_rego_dir_path) if filename.startswith(file_id)]
        if glob_verbose >= 2:
            print("Random rego filenames: {}".format(random_rego_filenames))
        if not random_rego_filenames: # Dir empty
            uid = "1"
        else:
            uids = []
            for random_rego_filename in random_rego_filenames:
                if random_rego_filename.startswith(file_id):
                    uids.append(int(random_rego_filename.split('.')[0].split('-')[-1]))
            max_uid = max(uids)
            uid = str(max_uid + 1)
        if glob_verbose >= 2:
            print("UID: {}".format(uid))

        output_policy_name = generated_rego_dir_path + path_chunks[-1].split('.')[0] + "-" + uid + ".rego"
    else:
        terminate_app(0) #TODO Handle error
    print("Output policy file: {}\n".format(output_policy_name))

    # Basic ABAC structure
    global policy
    policy = []
    policy.append("package istio.authz\n")
    policy.append("import input.attributes.request.http as http_request\n\n")
    policy.append("default allow = false\n\n")
    policy.append("user_name = parsed {\n")
    policy.append('  [_, encoded] := split(http_request.headers.authorization, " ")\n')
    policy.append('  [parsed, _] := split(base64url.decode(encoded), ":")\n')
    policy.append("}\n\n")

    # Generate attributes
    #TODO Improvement: Generate based on random tenure + for all 'real' user
    policy.append('user_attributes = {\n')
    policy.append('  "owner": {"tenure": 8},\n')
    policy.append('  "vfx-1": {"tenure": 3},\n')
    policy.append('  "vfx-2": {"tenure": 12},\n')
    policy.append('  "vfx-3": {"tenure": 7},\n')
    policy.append('  "color": {"tenure": 3},\n')
    policy.append('  "sound": {"tenure": 4},\n')
    policy.append('  "hdr": {"tenure": 5},\n')
    policy.append('}\n\n')


    # Getting attribute ranges for error generation:
    global comp_operators, method_range, tenure_range, time_range, prop_range, user_range, dst_range
    comp_operators = {"==", ">=", "<=", ">", "<"}
    method_range = set()
    tenure_range = set()
    time_range = set()
    prop_range = set()
    user_range = set()
    dst_range = set()
    for edge in workflow_metagraph.edges:
        # Invertex
        for attribute in list(edge.invertex):
            # Match equals
            if 'Eq' in attribute:
                policy_eq_range(attribute)

            # Match comparison operators
            elif '>=' in attribute:
                policy_comp_range(attribute)

            elif '<=' in attribute:
                policy_comp_range(attribute)

            elif '>' in attribute:
                policy_comp_range(attribute)

            elif '<' in attribute:
                policy_comp_range(attribute)

            elif 'is_' in attribute: # prop
                policy_prop_range(attribute)

            else: # username
                policy_user_range(attribute)

        # Outvertex
        for attribute in list(edge.outvertex):
            policy_dst_range(attribute)

    if glob_verbose >= 3:
        print("Operators : {}".format(list(comp_operators)))
        print("Method range : {}".format(list(method_range)))
        print("Tenure range : {}".format(list(tenure_range)))
        print("Time range : {}".format(list(time_range)))
        print("Prop range : {}".format(list(prop_range)))
        print("User range : {}".format(list(user_range)))
        print("Dst range : {}\n".format(list(dst_range)))


    # Filling policy
    print("Filling policy")
    global_expressions_index = 0 # Global index for error generation
    for edge in workflow_metagraph.edges:
        if glob_verbose >= 4:
            print(edge)

        user_attributes_set = False
        time_set = False
        policy.append('allow {\n')

        # Invertex
        for attribute in list(edge.invertex):
            # Match equals
            if 'Eq' in attribute:
                if expressions_map[global_expressions_index] == 0:
                    policy_eq_add(attribute)
                else:
                    policy_eq_err(attribute)

            # Match comparison operators
            elif '>=' in attribute:
                if expressions_map[global_expressions_index] == 0:
                    user_attributes_set, time_set = policy_ge_add(attribute, user_attributes_set, time_set)
                else:
                    user_attributes_set, time_set = policy_ge_err(attribute, user_attributes_set, time_set)

            elif '<=' in attribute:
                if expressions_map[global_expressions_index] == 0:
                    user_attributes_set, time_set = policy_le_add(attribute, user_attributes_set, time_set)
                else:
                    user_attributes_set, time_set = policy_le_err(attribute, user_attributes_set, time_set)

            elif '>' in attribute:
                if expressions_map[global_expressions_index] == 0:
                    user_attributes_set, time_set = policy_gt_add(attribute, user_attributes_set, time_set)
                else:
                    user_attributes_set, time_set = policy_gt_err(attribute, user_attributes_set, time_set)

            elif '<' in attribute:
                if expressions_map[global_expressions_index] == 0:
                    user_attributes_set, time_set = policy_lt_add(attribute, user_attributes_set, time_set)
                else:
                    user_attributes_set, time_set = policy_lt_err(attribute, user_attributes_set, time_set)

            elif 'is_' in attribute: # prop
                if expressions_map[global_expressions_index] == 0:
                    policy_prop_add(attribute)
                else:
                    policy_prop_err(attribute)

            else: # username
                if expressions_map[global_expressions_index] == 0:
                    policy_user_add(attribute)
                else:
                    policy_user_err(attribute)

            global_expressions_index += 1

        # Outvertex
        for attribute in list(edge.outvertex):
            if expressions_map[global_expressions_index] == 0:
                policy_dst_add(attribute)
            else:
                policy_dst_err(attribute)

            global_expressions_index += 1

        policy.append('}\n\n')


    # Writing policy to file
    with open(output_policy_name, 'w') as output_policy:
        output_policy.writelines(policy)


if __name__ == '__main__':
    print("\n\n###############################################################################")
    print("Getting arguments")
    print("###############################################################################")

    parser = get_parser() # Create a parser
    args = parser.parse_args() # Parse arguments
    print(args)

    # Call main
    main(args.verbose, args.workflow, args.error_rate)

    terminate_app(0)


###############################################################################
