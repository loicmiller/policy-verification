# Folders
***
- example-policies : example Rego policies (implementation) from the OPA website / Github / manually created.
- generated-rego-from-spec : Rego policies generated from policy specifications, via the SpecToRego.py script.
- graphviz-impl-metagraphs : Metagraph representations generated with graphviz. They are inaccurate.
- impl-metagraph-generators : Generated Python files containing code to generate the implementation metagraph. Files generated from using ANTLR on Rego policies contained in example-policies. Can be imported to other scripts.
- manually-drawn-metagraphs : Metagraphs manually drawn with draw.io.
- old :
 - graphviz-example : Unusability of graphviz for metagraph representation
 - opa-playground-example : OPA playground example
 - workflow-antlr : ANTLR parser, grammar and listener for parsing attributes of a workflow specification. Example attributes in example-attributes folder.
   - example-attributes : example expression for attributes on an edge of the policy specification.
 - metagraph-equivalence.py : Shows a bug in mgtoolkit's equivalence function.
 - old-graph-generation.py : Old workflow specification generation function.
 - pyparsing-example.py : Unusability of pyparsing for logical expression parsing.
- RegoAntlr : ANTLR parser, grammar and listener for parsing a Rego policy to generate a Python file which constructs a metagraph from the parsed policy.
- workflow-specs : Policy specifications of workflows. Manually or randomly generated.



# Files
***
- bulk-spec-impl-equivalence.py : Bulk version of SpecImplEquivalence.py
- bulk-random-workflow-spec-generator.py : Bulk version of RandomWorkflowSpecGenerator.py
- bulk-rego-to-metagraph.py : Bulk version of antlr.py
- bulk-spec-to-rego.py : Bulk version of SpecToRego.py
- PolicyMetagraph.py : Represents a policy metagraph. Used for policy implementation metagraphs of the impl-metagraph-generators folder.
- RandomWorkflowSpecGenerator.py : Generates random workflow specifications from graph parameters. Outputs specifications to the workflow-specs folder.
- redundancy-conflicts-detection.py : Loads an implementation metagraph and tries to detect redundancies or conflicts.
- SpecImplEquivalence.py : Loads a policy specification and a policy implementation, transforms them to metagraphs, and compares them.
- SpecToRego.py : Takes a policy specification and transforms it into a Rego policy implementation. Files are generated in the generated-rego-from-spec folder. Can introduce errors in the translation.



# How to use
***
## Show AST for a Rego file
***
antlr4 RegoLexer.g4
antlr4 RegoParser.g4
javac Rego*.java
grun Rego module -tokens -gui < ../example-policies/abac.rego


## Generate metagraph from Rego policy implementation
***
cd RegoAntlr/
antlr4 -Dlanguage=Python3 RegoLexer.g4
antlr4 -Dlanguage=Python3 RegoParser.g4
cd ..
python3 RegoAntlr/antlr.py example-policies/abac.rego
python2.7 redundancy-conflicts-detection.py abac


## Show AST for a policy specification expression
***
antlr4 Workflow.g4
javac Workflow*.java
grun Workflow policy -tokens -gui < ../example-attributes/example.dat


## Listener for policy specification expression
***
antlr4 -Dlanguage=Python3 workflow-antlr/Workflow.g4
python3 workflow-antlr/antlr.py example-attributes/example.dat


## Generate random workflow specification
***
python RandomWorkflowSpecGenerator.py


## Convert specification to Rego
***
python2.7 SpecToRego.py workflow-specs/randomly-generated/10-nodes-0-3-edges-2-policy/1.dat


## Compare equivalence of policy specification and implementation
***
python2.7 SpecImplEquivalence.py workflow-specs/randomly-generated/50-nodes-0-3-edges-5-policy/23.dat impl-metagraph-generators/generated-from-random/50-nodes-0-3-edges-5-policy-0-25-error/23-1.py


# Measurements
***
1. Create a lot of random workflow specifications for different parameters

python bulk-random-workflow-spec-generator.py -n "10,20" -e "0.3,0.6" -s "1,2"

2. Transform those workflow specifications into Rego with different error rates

python bulk-spec-to-rego.py -e "0.0,0.3,0.6,0.9"

3. Use ANTLR to generate metagraph construction files on all Rego generated implementations

python bulk-rego-to-metagraph.py

4. Use SpecImplEquivalence to compare the generated metagraph construction files to the original workflow specifications for all created random specs, and measure time to comparison

python bulk-spec-impl-equivalence.py


#TODO (bulk-spec-impl-equivalence) Python script to massively compare specs and impls, and measure time to completion. Dump results to CSV.
#TODO Generate Figure from CSV data
