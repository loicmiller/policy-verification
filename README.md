# Requirements

- ANTLR tool and python runtime
- The python3 version of mgtoolkit, which can be found [here](https://github.com/loicmiller/mgtoolkit).

# ANTLR install

Install the tool:
```bash
curl -O http://www.antlr.org/download/antlr-4.9-complete.jar
sudo cp antlr-4.9-complete.jar /usr/local/lib/
export CLASSPATH=".:/usr/local/lib/antlr-4.9-complete.jar:$CLASSPATH"
alias antlr4='java -Xmx500M -cp "/usr/local/lib/antlr-4.9-complete.jar:$CLASSPATH" org.antlr.v4.Tool'
alias grun='java org.antlr.v4.gui.TestRig'
```

Install the python runtime:
```bash
pip install antlr4-python3-runtime
```



# Data generation

## Files

- `PolicyMetagraph.py`: Represents a policy metagraph. Used for policy implementation metagraphs of the impl-metagraph-generators folder.
- `RandomWorkflowSpecGenerator.py`: Generates random workflow specifications from graph parameters. Outputs specifications to the workflow-specs folder.
- `SpecToRego.py`: Takes a policy specification and transforms it into a Rego policy implementation. Files are generated in the generated-rego-from-spec folder. Can optionally introduce errors in the translation.
- `RegoToMetagraph.py`: Takes a Rego policy implementation and turns it into a metagraph generator. Files are generated in the impl-metagraph-generators folder.
- `SpecImplEquivalence.py`: Loads a policy specification and a policy implementation, transforms them to metagraphs, and compares them. Measures time taken to achieve comparison and dumps data to file in the CSV format.


- `bulk-random-workflow-spec-generator.py`: Bulk version of RandomWorkflowSpecGenerator.py. Generate random workflow specifications in bulk.
- `bulk-spec-to-rego.py`: Bulk version of SpecToRego.py. Generate Rego policy implementations in bulk.
- `bulk-rego-to-metagraph.py`: Bulk version of RegoToMetagraph.py. Generate metagraph generators in bulk.
- `bulk-spec-impl-equivalence.py`: Bulk version of SpecImplEquivalence.py. Compare metagraphs in bulk.


## Folders

- `workflow-specs`: Policy specifications of workflows. Manually or randomly generated.
- `generated-rego-from-spec`: Rego policies generated from policy specifications, via the SpecToRego.py script.
- `impl-metagraph-generators`: Generated Python files containing code to generate the implementation metagraph. Files generated from using ANTLR on Rego policies. Can be imported to other scripts.
- `RegoAntlr`: ANTLR parser, grammar and listener for parsing a Rego policy to generate a Python file which constructs a metagraph from the parsed policy.


## Generate listener for the Rego language

The first thing we need to do is generate the listener in order to construct the AST for the Rego language.

```bash
cd RegoAntlr/
antlr4 -Dlanguage=Python3 RegoLexer.g4
antlr4 -Dlanguage=Python3 RegoParser.g4
```


## Measurements

Once we have generated the listener, we can create our data and launch our measures.


1. Create a lot of random workflow specifications for different parameters

```bash
python bulk-random-workflow-spec-generator.py -n "10,20,30,50,100" -s "1,2"
```

This will generate 30 random workflow specifications for set sizes of 10, 20, 30, 50 and 100 elements, and policy sizes of 1 and 2.
Generated workflow specifications can be found in the `workflow-specs` folder.


2. Transform those workflow specifications into Rego with different error rates

```bash
python bulk-spec-to-rego.py -e "0.0,0.2,0.4"
```

This will take all random workflow specifications we generated, and convert them to Rego, with different error rates; Here, the error rates are 0.0, 0.2 and 0.4.
Since errors are randomly created, the default parameter will generate 30 different Rego implementations per workflow specification.


3. Use ANTLR to generate metagraph constructors from all Rego policy implementations

```bash
python bulk-rego-to-metagraph.py
```

For each Rego implementation, this will generate the associated metagraph constructor.
There is a 1-to-1 mapping between implementations and constructors.


4. Use SpecImplEquivalence to compare the generated metagraph construction files to the original workflow specifications for all created random specs, and measure time to comparison

```bash
python bulk-spec-impl-equivalence.py
```

This will compare specification and implementation of randomly generated workflow policies, and dump data to the `measures/equivalence.dat` file.
Use the notebooks in `measures/` to analyze the data.



## Optional: Show AST for a Rego file

```bash
cd RegoAntlr/
antlr4 RegoLexer.g4
antlr4 RegoParser.g4
javac Rego*.java
grun Rego module -tokens -gui < ../generated-rego-from-spec/generated-from-manual/movie-wfs.rego
```



# Data analysis

## Files

- `boxplot-generation.ipynb`: Generate boxplot.
- `regression-plot-generation.ipynb`: Generate regression scatterplot.


- `descriptive-stats.ipynb`: Descriptive statistics about the data
- `regression.ipynb`: Regression analysis

## Folders

- `figures`: Folder containing all generated figures from analysis.
