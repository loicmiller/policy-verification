from mgtoolkit.library import *
from graphviz import Digraph

if __name__ == "__main__":
	variables = []
	propositions = []
	current_propositions = []
	edges = []

	rule_head = 'allow=false'
	src = "rule_0"
	variables.append(src)
	dst = rule_head
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'allow'
	if "is_post" not in propositions:
		propositions.append("is_post")
	if "is_post" not in current_propositions:
		current_propositions.append("is_post")
	if "is_dogs" not in propositions:
		propositions.append("is_dogs")
	if "is_dogs" not in current_propositions:
		current_propositions.append("is_dogs")
	if "claims.username==\"alice\"" not in propositions:
		propositions.append("claims.username==\"alice\"")
	if "claims.username==\"alice\"" not in current_propositions:
		current_propositions.append("claims.username==\"alice\"")
	src = "rule_1"
	variables.append(src)
	dst = rule_head
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'is_post'
	if "input.attributes.request.http.method==\"POST\"" not in propositions:
		propositions.append("input.attributes.request.http.method==\"POST\"")
	if "input.attributes.request.http.method==\"POST\"" not in current_propositions:
		current_propositions.append("input.attributes.request.http.method==\"POST\"")
	src = "rule_2"
	variables.append(src)
	dst = rule_head
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'is_dogs'
	if "input.attributes.request.http.path==\"/pets/dogs\"" not in propositions:
		propositions.append("input.attributes.request.http.path==\"/pets/dogs\"")
	if "input.attributes.request.http.path==\"/pets/dogs\"" not in current_propositions:
		current_propositions.append("input.attributes.request.http.path==\"/pets/dogs\"")
	src = "rule_3"
	variables.append(src)
	dst = rule_head
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'claims:=payload'
	if "io.jwt.verify_hs256(bearer_token,\"B41BD5F462719C6D6118E673A2389\")" not in propositions:
		propositions.append("io.jwt.verify_hs256(bearer_token,\"B41BD5F462719C6D6118E673A2389\")")
	if "io.jwt.verify_hs256(bearer_token,\"B41BD5F462719C6D6118E673A2389\")" not in current_propositions:
		current_propositions.append("io.jwt.verify_hs256(bearer_token,\"B41BD5F462719C6D6118E673A2389\")")
	if "[_,payload,_]:=io.jwt.decode(bearer_token)" not in propositions:
		propositions.append("[_,payload,_]:=io.jwt.decode(bearer_token)")
	if "[_,payload,_]:=io.jwt.decode(bearer_token)" not in current_propositions:
		current_propositions.append("[_,payload,_]:=io.jwt.decode(bearer_token)")
	src = "rule_4"
	variables.append(src)
	dst = rule_head
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'bearer_token:=t'
	if "v:=input.attributes.request.http.headers.authorization" not in propositions:
		propositions.append("v:=input.attributes.request.http.headers.authorization")
	if "v:=input.attributes.request.http.headers.authorization" not in current_propositions:
		current_propositions.append("v:=input.attributes.request.http.headers.authorization")
	if "startswith(v,\"Bearer \")" not in propositions:
		propositions.append("startswith(v,\"Bearer \")")
	if "startswith(v,\"Bearer \")" not in current_propositions:
		current_propositions.append("startswith(v,\"Bearer \")")
	if "t:=substring(v,count(\"Bearer \"),-1)" not in propositions:
		propositions.append("t:=substring(v,count(\"Bearer \"),-1)")
	if "t:=substring(v,count(\"Bearer \"),-1)" not in current_propositions:
		current_propositions.append("t:=substring(v,count(\"Bearer \"),-1)")
	src = "rule_5"
	variables.append(src)
	dst = rule_head
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []


	variable_set = set(variables)
	propositions_set = set(propositions)
	cm = ConditionalMetagraph(variable_set, propositions_set)
	cm.add_edges_from(edges)
	print(repr(cm))
	g = Digraph("jwt-decoding", filename="../metagraphs/jwt-decoding.gv")
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
