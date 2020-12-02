###############################################################################
# Imports

import sys
import os
from antlr4 import *
from RegoAntlr.RegoLexer import RegoLexer
from RegoAntlr.RegoParser import RegoParser
from RegoAntlr.RegoListener import RegoListener

import argparse # Argument parser


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
    parser = argparse.ArgumentParser(description="Transforms Rego To Metagraph Generators")
    parser.add_argument("--version", action="version", version='%(prog)s 1.0')
    parser.add_argument("-v", "--verbose", action="count", default=0, help="increase output verbosity")
    parser.add_argument("policy", type=str, metavar="FILE", help="Rego policy file to translate")

    return parser


###############################################################################
# Main

def main(verbose, policy):
    global glob_verbose
    glob_verbose = verbose

    print("\n\n###############################################################################")
    print("Tokenizing and parsing policy")
    print("###############################################################################")
    # Generate output policy name
    if "generated-from-manual" in policy:
        output_mgg_file = "impl-metagraph-generators/generated-from-manual/" + policy.split('.')[0].split('/')[-1] + ".py"
    elif "generated-from-random" in policy:  # generated-rego-from-spec generated-from-random 50-nodes-0-3-edges-5-policy-0-0-error 69-1.rego
        path_chunks = policy.split("/")
        generated_mgg_dir_path = "impl-metagraph-generators/generated-from-random/" + path_chunks[-2] + "/"
        if not os.path.exists(generated_mgg_dir_path):
            os.makedirs(generated_mgg_dir_path)
        print("MGG dir path: {}".format(generated_mgg_dir_path))

        # Create __init__.py to make generators importable
        if not os.path.isfile(generated_mgg_dir_path + "__init__.py"):
            open(generated_mgg_dir_path + "__init__.py", 'a').close()

        output_mgg_file = generated_mgg_dir_path + path_chunks[-1].split('.')[0] + ".py"
    else:
        terminate_app(0) #TODO Handle error

    print("Output file: {}".format(output_mgg_file))

    if glob_verbose >= 1:
        print("policy -> input")
    input = FileStream(policy)
    if glob_verbose >= 1:
        print("input -> lexer")
    lexer = RegoLexer(input)
    if glob_verbose >= 1:
        print("lexer -> stream")
    stream = CommonTokenStream(lexer)
    if glob_verbose >= 1:
        print("stream -> parser")
    parser = RegoParser(stream)
    if glob_verbose >= 1:
        print("parser -> tree")
    tree = parser.module() # Rule to evaluate
    if glob_verbose >= 1:
        print("tree -> output")
    output = open(output_mgg_file,"w")


    print("\n\n###############################################################################")
    print("Creating listener and walking AST")
    print("###############################################################################")
    rego = RegoListener(output)
    walker = ParseTreeWalker()
    walker.walk(rego, tree)

    output.close()


if __name__ == '__main__':
    print("\n\n###############################################################################")
    print("Getting arguments")
    print("###############################################################################")

    parser = get_parser() # Create a parser
    args = parser.parse_args() # Parse arguments
    print(args)

    # Call main
    main(args.verbose, args.policy)

    terminate_app(0)


###############################################################################
