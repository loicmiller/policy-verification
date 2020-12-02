###############################################################################
# Imports

import sys
import argparse # Argument parser

import os

import RegoToMetagraph


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
    parser.add_argument("--gen-set-filter", type=str, metavar="GEN_SET_FILTER", default=None, help="generating sets to generate metagraph generators for")
    parser.add_argument("--policy-filter", type=str, metavar="POLICY_FILTER", default=None, help="policy sizes to generate metagraph generators for")
    parser.add_argument("--error-rate-filter", type=str, metavar="ERR_RATE_FILTER", default=None, help="error rates to generate metagraph generators for")

    return parser


###############################################################################
# Functions


###############################################################################
# Main

def main(verbose, gen_set_filter, policy_filter, error_rate_filter):
    print("\n\n###############################################################################")
    print("Generating Metagraph generators from Rego policies")
    print("###############################################################################")

    if gen_set_filter:
        gen_set_filter = [generating_set_size + "-" for generating_set_size in gen_set_filter.split(',')]
        if verbose >= 2:
            print("Generating set sizes to generate metagraph generators for: {}".format(gen_set_filter))

    if policy_filter:
        policy_filter = [policy for policy in policy_filter.split(',')]
        if verbose >= 2:
            print("Policy sizes to generate metagraph generators for: {}".format(gen_set_filter))

    if error_rate_filter:
        error_rate_filter = [error_rate for error_rate in error_rate_filter.split(',')]
        if verbose >= 2:
            print("Error rates to generate Rego for: {}".format(error_rate_filter))

    rego_dir = "generated-rego-from-spec/generated-from-random/"
    print("Rego dir: {}".format(rego_dir))
    rego_categories = sorted(os.listdir(rego_dir))
    if verbose >= 2:
        print("Rego categories: {}".format(rego_categories))

    # Filtering generating set sizes
    if gen_set_filter:
        categories_to_keep = []
        for rego_category in rego_categories:
            if rego_category.startswith(tuple(gen_set_filter)):
                if verbose >= 3:
                    print("Rego category kept: {}".format(rego_category))
                categories_to_keep.append(rego_category)
        rego_categories = [rego_category for rego_category in rego_categories if rego_category in categories_to_keep]
    if verbose >= 2:
        print("Rego categories: {}".format(rego_categories))

    # Filtering policy sizes
    if policy_filter:
        categories_to_keep = []
        for rego_category in rego_categories:
            for filter in policy_filter:
                if "{}-policy".format(filter) in rego_category:
                    if verbose >= 3:
                        print("Rego category kept: {}".format(rego_category))
                    categories_to_keep.append(rego_category)
        rego_categories = [rego_category for rego_category in rego_categories if rego_category in categories_to_keep]
    if verbose >= 2:
        print("Rego categories: {}".format(rego_categories))

    # Filtering error rates
    if error_rate_filter:
        categories_to_keep = []
        for rego_category in rego_categories:
            for filter in error_rate_filter:
                if "{}-{}-error".format(filter.split('.')[0], filter.split('.')[1]) in rego_category:
                    if verbose >= 3:
                        print("Rego category kept: {}".format(rego_category))
                    categories_to_keep.append(rego_category)
        rego_categories = [rego_category for rego_category in rego_categories if rego_category in categories_to_keep]
    if verbose >= 2:
        print("Rego categories: {}".format(rego_categories))

    # Gather all specification filenames for processing
    policies = []
    for rego_category in rego_categories:
        policies.extend([rego_dir + rego_category + "/" + policy for policy in sorted(os.listdir(rego_dir + rego_category))])
    print("Rego policies: {}".format(len(policies)))
    if verbose >= 3:
        for policy in policies:
            print("{}".format(policy))
        print("")

    total_runs = len(policies)
    print("Total number of runs: {}".format(total_runs))
    run_ctr = 0

    # Loop to generate metagraph generators from Rego
    for policy in policies:
        run_ctr += 1
        print("\n\n\nRun {} out of {}".format(run_ctr, total_runs))
        print("Processing policy: {}".format(policy))
        RegoToMetagraph.main(verbose, policy)


if __name__ == '__main__':
    print("\n\n###############################################################################")
    print("Getting arguments")
    print("###############################################################################")

    parser = get_parser() # Create a parser
    args = parser.parse_args() # Parse arguments
    print(args)

    # Call main
    main(args.verbose, args.gen_set_filter, args.policy_filter, args.error_rate_filter)

    terminate_app(0)


###############################################################################
