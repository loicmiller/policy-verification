###############################################################################
# Imports

import sys
import argparse # Argument parser

import os

import SpecToRego


###############################################################################
# General utility

# Exit the program
def terminate_app(code):
    print("Exiting program...")
    sys.exit(code)


###############################################################################
# Argument parser

def get_parser():
    # Get parser for command line arguments
    parser = argparse.ArgumentParser(description="Random workflow specification generator", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--version", action="version", version='%(prog)s 1.0')
    parser.add_argument("-v", "--verbose", action="count", default=0, help="increase output verbosity")
    parser.add_argument("-e", "--error-rates", type=str, metavar="ERROR_RATES", default="0.0", help="rate of errors in the generated workflow")
    parser.add_argument("-r", "--repeats", type=int, metavar="REPEATS", default="30", help="number of policy specifications to generate per parameter combination")
    parser.add_argument("--gen-set-filter", type=str, metavar="GEN_SET_FILTER", default=None, help="generating sets to generate Rego for")
    parser.add_argument("--edge-filter", type=str, metavar="EDGE_FILTER", default=None, help="edges to generate Rego for")
    parser.add_argument("--policy-filter", type=str, metavar="POLICY_FILTER", default=None, help="policy sizes to generate Rego for")

    return parser


###############################################################################
# Functions


###############################################################################
# Main

def main(verbose, error_rates, repeats, gen_set_filter, edge_filter, policy_filter):
    print("\n\n###############################################################################")
    print("Generating Rego policies from random workflow specifications")
    print("###############################################################################")

    error_rates = [float(error_rate) for error_rate in error_rates.split(',')]
    if verbose >= 1:
        print("Error rates: {}".format(error_rates))

    if gen_set_filter:
        gen_set_filter = [generating_set_size + "-" for generating_set_size in gen_set_filter.split(',')]
        if verbose >= 2:
            print("Generating set sizes to generate Rego for: {}".format(gen_set_filter))

    if edge_filter:
        edge_filter = [edge for edge in edge_filter.split(',')]
        if verbose >= 2:
            print("Edges to generate Rego for: {}".format(edge_filter))

    if policy_filter:
        policy_filter = [policy for policy in policy_filter.split(',')]
        if verbose >= 2:
            print("Policies to generate Rego for: {}".format(policy_filter))

    spec_dir = "workflow-specs/randomly-generated/"
    print("Spec dir: {}".format(spec_dir))
    workflow_categories = sorted(os.listdir(spec_dir))
    if verbose >= 2:
        print("Workflow categories: {}".format(workflow_categories))

    # Filtering generating set sizes
    if gen_set_filter:
        categories_to_keep = []
        for workflow_category in workflow_categories:
            if workflow_category.startswith(tuple(gen_set_filter)):
                if verbose >= 2:
                    print("Workflow category kept: {}".format(workflow_category))
                categories_to_keep.append(workflow_category)
        workflow_categories = [workflow_category for workflow_category in workflow_categories if workflow_category in categories_to_keep]
    if verbose >= 2:
        print("Workflow categories: {}".format(workflow_categories))

    # Filtering edges
    if edge_filter:
        categories_to_keep = []
        for workflow_category in workflow_categories:
            for filter in edge_filter:
                if "{}-{}-edges".format(filter.split('.')[0], filter.split('.')[1]) in workflow_category:
                    if verbose >= 2:
                        print("Workflow category kept: {}".format(workflow_category))
                    categories_to_keep.append(workflow_category)
        workflow_categories = [workflow_category for workflow_category in workflow_categories if workflow_category in categories_to_keep]
    if verbose >= 2:
        print("Workflow categories: {}".format(workflow_categories))

    # Filtering policy sizes
    if policy_filter:
        categories_to_keep = []
        for workflow_category in workflow_categories:
            for filter in policy_filter:
                if "{}-policy".format(filter) in workflow_category:
                    if verbose >= 2:
                        print("Workflow category kept: {}".format(workflow_category))
                    categories_to_keep.append(workflow_category)
        workflow_categories = [workflow_category for workflow_category in workflow_categories if workflow_category in categories_to_keep]
    print("Workflow categories: {}".format(workflow_categories))

    # Gather all specification filenames for processing
    workflow_specs = []
    for workflow_category in workflow_categories:
        workflow_specs.extend(sorted([spec_dir + workflow_category + "/" + workflow_spec for workflow_spec in os.listdir(spec_dir + workflow_category)]))
    print("Workflow specs: {}".format(len(workflow_specs)))
    if verbose >= 2:
        for workflow_spec in workflow_specs:
            print(workflow_spec)
        print("")


    total_runs = len(workflow_specs) * len(error_rates) * repeats
    print("Total number of runs: {}".format(total_runs))
    run_ctr = 0

    # Loop to generate rego from specifications
    for workflow_spec in workflow_specs:
        for error_rate in error_rates:
            for repeat in range(repeats):
                run_ctr += 1
                print("\n\n\nRun {} out of {} (repeat {})".format(run_ctr, total_runs, repeat+1))
                print("Processing spec: {}".format(workflow_spec))
                SpecToRego.main(verbose, workflow_spec, error_rate)


if __name__ == '__main__':
    print("\n\n###############################################################################")
    print("Getting arguments")
    print("###############################################################################")

    parser = get_parser() # Create a parser
    args = parser.parse_args() # Parse arguments
    print(args)

    # Call main
    main(args.verbose, args.error_rates, args.repeats, args.gen_set_filter, args.edge_filter, args.policy_filter)

    terminate_app(0)


###############################################################################
