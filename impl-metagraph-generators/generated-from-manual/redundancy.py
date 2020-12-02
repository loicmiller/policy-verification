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
	if "user_is_owner" not in propositions:
		propositions.append("user_is_owner")
	if "user_is_owner" not in current_propositions:
		current_propositions.append("user_is_owner")
	src = "rule_1"
	variables.append(src)
	dst = rule_head
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'allow'
	if "user_is_employee" not in propositions:
		propositions.append("user_is_employee")
	if "user_is_employee" not in current_propositions:
		current_propositions.append("user_is_employee")
	if "action_is_read" not in propositions:
		propositions.append("action_is_read")
	if "action_is_read" not in current_propositions:
		current_propositions.append("action_is_read")
	src = "rule_2"
	variables.append(src)
	dst = rule_head
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'allow'
	if "user_is_employee" not in propositions:
		propositions.append("user_is_employee")
	if "user_is_employee" not in current_propositions:
		current_propositions.append("user_is_employee")
	if "user_is_senior" not in propositions:
		propositions.append("user_is_senior")
	if "user_is_senior" not in current_propositions:
		current_propositions.append("user_is_senior")
	if "action_is_update" not in propositions:
		propositions.append("action_is_update")
	if "action_is_update" not in current_propositions:
		current_propositions.append("action_is_update")
	src = "rule_3"
	variables.append(src)
	dst = rule_head
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'allow'
	if "user_is_customer" not in propositions:
		propositions.append("user_is_customer")
	if "user_is_customer" not in current_propositions:
		current_propositions.append("user_is_customer")
	if "action_is_read" not in propositions:
		propositions.append("action_is_read")
	if "action_is_read" not in current_propositions:
		current_propositions.append("action_is_read")
	if "notpet_is_adopted" not in propositions:
		propositions.append("notpet_is_adopted")
	if "notpet_is_adopted" not in current_propositions:
		current_propositions.append("notpet_is_adopted")
	src = "rule_4"
	variables.append(src)
	dst = rule_head
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'allow'
	if "user_is_employee" not in propositions:
		propositions.append("user_is_employee")
	if "user_is_employee" not in current_propositions:
		current_propositions.append("user_is_employee")
	if "action_is_read" not in propositions:
		propositions.append("action_is_read")
	if "action_is_read" not in current_propositions:
		current_propositions.append("action_is_read")
	if "pet_is_adopted" not in propositions:
		propositions.append("pet_is_adopted")
	if "pet_is_adopted" not in current_propositions:
		current_propositions.append("pet_is_adopted")
	src = "rule_5"
	variables.append(src)
	dst = rule_head
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'user_is_owner'
	if "data.user_attributes[input.user].title==\"owner\"" not in propositions:
		propositions.append("data.user_attributes[input.user].title==\"owner\"")
	if "data.user_attributes[input.user].title==\"owner\"" not in current_propositions:
		current_propositions.append("data.user_attributes[input.user].title==\"owner\"")
	src = "rule_6"
	variables.append(src)
	dst = rule_head
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'user_is_employee'
	if "data.user_attributes[input.user].title==\"employee\"" not in propositions:
		propositions.append("data.user_attributes[input.user].title==\"employee\"")
	if "data.user_attributes[input.user].title==\"employee\"" not in current_propositions:
		current_propositions.append("data.user_attributes[input.user].title==\"employee\"")
	src = "rule_7"
	variables.append(src)
	dst = rule_head
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'user_is_customer'
	if "data.user_attributes[input.user].title==\"customer\"" not in propositions:
		propositions.append("data.user_attributes[input.user].title==\"customer\"")
	if "data.user_attributes[input.user].title==\"customer\"" not in current_propositions:
		current_propositions.append("data.user_attributes[input.user].title==\"customer\"")
	src = "rule_8"
	variables.append(src)
	dst = rule_head
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'user_is_senior'
	if "data.user_attributes[input.user].tenure>8" not in propositions:
		propositions.append("data.user_attributes[input.user].tenure>8")
	if "data.user_attributes[input.user].tenure>8" not in current_propositions:
		current_propositions.append("data.user_attributes[input.user].tenure>8")
	src = "rule_9"
	variables.append(src)
	dst = rule_head
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'action_is_read'
	if "input.action==\"read\"" not in propositions:
		propositions.append("input.action==\"read\"")
	if "input.action==\"read\"" not in current_propositions:
		current_propositions.append("input.action==\"read\"")
	src = "rule_10"
	variables.append(src)
	dst = rule_head
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'action_is_update'
	if "input.action==\"update\"" not in propositions:
		propositions.append("input.action==\"update\"")
	if "input.action==\"update\"" not in current_propositions:
		current_propositions.append("input.action==\"update\"")
	src = "rule_11"
	variables.append(src)
	dst = rule_head
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'pet_is_adopted'
	if "data.pet_attributes[input.resource].adopted==true" not in propositions:
		propositions.append("data.pet_attributes[input.resource].adopted==true")
	if "data.pet_attributes[input.resource].adopted==true" not in current_propositions:
		current_propositions.append("data.pet_attributes[input.resource].adopted==true")
	src = "rule_12"
	variables.append(src)
	dst = rule_head
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []


	variable_set = set(variables)
	propositions_set = set(propositions)
	cm = ConditionalMetagraph(variable_set, propositions_set)
	cm.add_edges_from(edges)
	print(repr(cm))
	g = Digraph("redundancy", filename="../metagraphs/redundancy.gv")
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
