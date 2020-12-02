import sys
from antlr4 import *
from .RegoParser import RegoParser
from .RegoParserListener import RegoParserListener


class RegoListener(RegoParserListener):
    def __init__(self, output):
        self.output = output
        self.output.write('import os,sys,inspect\n')
        self.output.write('currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))\n')
        self.output.write('parentdir = os.path.dirname(currentdir)\n')
        self.output.write('sys.path.insert(0,parentdir)\n')
        self.output.write('from PolicyMetagraph import PolicyMetagraph\n\n')
        self.output.write('from mgtoolkit.library import *\n\n\n')
        self.output.write('def generate_metagraph():\n')
        self.output.write('\tpolicy_mg = PolicyMetagraph()\n')

        self.metagraph_name = str(output).split('/')[-1].split('.')[0]
        self.metagraph_filename = "../metagraphs/" + str(output).split('/')[-1].split('.')[0] + ".gv"
        self.rule_count = 0 # Counter for placeholder variables


    # Exit a parse tree produced by RegoParser#module.
    def exitModule(self, ctx:RegoParser.ModuleContext):
        self.output.write('\treturn policy_mg\n')


    # Exit a parse tree produced by RegoParser#g_rule.
    def exitG_rule(self, ctx:RegoParser.G_ruleContext):
        # Add edges and clean
        self.output.write('\tsrc = "rule_' + str(self.rule_count) + '"\n')
        self.output.write('\tpolicy_mg.variables.append(src)\n')
        self.output.write('\tdst = rule_head\n')
        self.output.write('\tif dst not in policy_mg.variables:\n')
        self.output.write('\t\tpolicy_mg.variables.append(dst)\n')
        self.output.write('\tpolicy_mg.edges.append(Edge({src}, {dst}, attributes=policy_mg.current_propositions))\n')
        self.output.write('\tpolicy_mg.current_propositions = []\n\n')
        self.rule_count += 1


    # Enter a parse tree produced by RegoParser#rule_head.
    def enterRule_head(self, ctx:RegoParser.Rule_headContext):
        rule_head = ctx.var().getText()
        self.output.write("\trule_head = '" + rule_head + "'\n")


    # Enter a parse tree produced by RegoParser#literal.
    def enterLiteral(self, ctx:RegoParser.LiteralContext):
        literal = ctx.getText();
        literal = literal.replace('"', '\\"') # Sanitize literal
        self.output.write('\tif "' + literal + '" not in policy_mg.propositions:\n')
        self.output.write('\t\tpolicy_mg.propositions.append("' + literal + '")\n')
        self.output.write('\tif "' + literal + '" not in policy_mg.current_propositions:\n')
        self.output.write('\t\tpolicy_mg.current_propositions.append("' + literal + '")\n')
