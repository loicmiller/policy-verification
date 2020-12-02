from mgtoolkit.library import *
from graphviz import Digraph

if __name__ == "__main__":
	variables = []
	propositions = []
	current_propositions = []
	edges = []

	rule_head = 'allow=true'
	src = "rule_0"
	variables.append(src)
	dst = rule_head
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []


	variable_set = set(variables)
	propositions_set = set(propositions)
	cm = ConditionalMetagraph(variable_set, propositions_set)
	cm.add_edges_from(edges)
	print(repr(cm))
	g = Digraph("all-allow", filename="../metagraphs/all-allow.gv")
	g.attr(compound="true")
	for idx, edge in enumerate(edges):
		print(list(edge.invertex))
		print(list(edge.outvertex))
		for src_var in list(edge.invertex):
			if "\t" + src_var not in g.source:
				g.node(src_var)
				print("SRC Node " + src_var + " created.")
		for dst_var in list(edge.outvertex):
			if "\t" + dst_var not in g.source:
				g.node(dst_var)
				print("DST Node " + dst_var + " created.")

		src_cluster_name = "cluster_src_" + str(idx)
		with g.subgraph(name=src_cluster_name) as src_subg:
			for src_var in list(edge.invertex):
				src_subg.node(src_var)
			print("SRC Subgraph " + src_cluster_name + " created.")
		dst_cluster_name = "cluster_dst_" + str(idx)
		with g.subgraph(name=dst_cluster_name) as dst_subg:
			for dst_var in list(edge.outvertex):
				dst_subg.node(dst_var)
			print("DST Subgraph " + dst_cluster_name + " created.")

		g.edge(list(edge.invertex)[0], list(edge.outvertex)[0], ltail=src_cluster_name, lhead=dst_cluster_name)

	g.view()
