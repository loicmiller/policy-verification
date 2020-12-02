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
	if "roles_for_user[r]" not in propositions:
		propositions.append("roles_for_user[r]")
	if "roles_for_user[r]" not in current_propositions:
		current_propositions.append("roles_for_user[r]")
	if "required_roles[r]" not in propositions:
		propositions.append("required_roles[r]")
	if "required_roles[r]" not in current_propositions:
		current_propositions.append("required_roles[r]")
	src = "rule_1"
	variables.append(src)
	dst = rule_head
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'roles_for_user[r]'
	if "r:=user_roles[user_name][_]" not in propositions:
		propositions.append("r:=user_roles[user_name][_]")
	if "r:=user_roles[user_name][_]" not in current_propositions:
		current_propositions.append("r:=user_roles[user_name][_]")
	src = "rule_2"
	variables.append(src)
	dst = rule_head
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'required_roles[r]'
	if "perm:=role_perms[r][_]" not in propositions:
		propositions.append("perm:=role_perms[r][_]")
	if "perm:=role_perms[r][_]" not in current_propositions:
		current_propositions.append("perm:=role_perms[r][_]")
	if "perm.method=http_request.method" not in propositions:
		propositions.append("perm.method=http_request.method")
	if "perm.method=http_request.method" not in current_propositions:
		current_propositions.append("perm.method=http_request.method")
	if "perm.path=http_request.path" not in propositions:
		propositions.append("perm.path=http_request.path")
	if "perm.path=http_request.path" not in current_propositions:
		current_propositions.append("perm.path=http_request.path")
	src = "rule_3"
	variables.append(src)
	dst = rule_head
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'user_name=parsed'
	if "[_,_,_,_,_,_,parsed]:=split(input.attributes.source.principal,\"/\")" not in propositions:
		propositions.append("[_,_,_,_,_,_,parsed]:=split(input.attributes.source.principal,\"/\")")
	if "[_,_,_,_,_,_,parsed]:=split(input.attributes.source.principal,\"/\")" not in current_propositions:
		current_propositions.append("[_,_,_,_,_,_,parsed]:=split(input.attributes.source.principal,\"/\")")
	src = "rule_4"
	variables.append(src)
	dst = rule_head
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'user_roles={
"workflow-owner":["owner"],
"workflow-adder":["adder"],
"workflow-multiplier":["multiplier"]
}'
	src = "rule_5"
	variables.append(src)
	dst = rule_head
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'role_perms={
"owner":[
{"method":"POST","path":"/api/adder"}
],
"adder":[
{"method":"POST","path":"/api/multiplier"},
],
"multiplier":[
{"method":"POST","path":"/api/owner"}
],
}'
	src = "rule_6"
	variables.append(src)
	dst = rule_head
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []


	variable_set = set(variables)
	propositions_set = set(propositions)
	cm = ConditionalMetagraph(variable_set, propositions_set)
	cm.add_edges_from(edges)
	print(repr(cm))
	g = Digraph("operation-workflow", filename="../metagraphs/operation-workflow.gv")
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
