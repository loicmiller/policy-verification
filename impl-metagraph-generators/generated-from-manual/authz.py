from mgtoolkit.library import *
from graphviz import Digraph

if __name__ == "__main__":
	variables = []
	propositions = []
	current_propositions = []
	edges = []

	rule_head = 'authorized=false'
	src = "rule_0"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'has_member[pol_id]'
	if "pol_sub:=policies[pol_id].members[_]" not in propositions:
		propositions.append("pol_sub:=policies[pol_id].members[_]")
	if "pol_sub:=policies[pol_id].members[_]" not in current_propositions:
		current_propositions.append("pol_sub:=policies[pol_id].members[_]")
	if "input_sub:=input.subjects[_]" not in propositions:
		propositions.append("input_sub:=input.subjects[_]")
	if "input_sub:=input.subjects[_]" not in current_propositions:
		current_propositions.append("input_sub:=input.subjects[_]")
	if "common.subject_matches(input_sub,pol_sub)" not in propositions:
		propositions.append("common.subject_matches(input_sub,pol_sub)")
	if "common.subject_matches(input_sub,pol_sub)" not in current_propositions:
		current_propositions.append("common.subject_matches(input_sub,pol_sub)")
	src = "rule_1"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'has_resource[[pol_id,statement_id]]'
	if "statement_resource:=policies[pol_id].statements[statement_id].resources[_]" not in propositions:
		propositions.append("statement_resource:=policies[pol_id].statements[statement_id].resources[_]")
	if "statement_resource:=policies[pol_id].statements[statement_id].resources[_]" not in current_propositions:
		current_propositions.append("statement_resource:=policies[pol_id].statements[statement_id].resources[_]")
	if "common.resource_matches(input.resource,statement_resource)" not in propositions:
		propositions.append("common.resource_matches(input.resource,statement_resource)")
	if "common.resource_matches(input.resource,statement_resource)" not in current_propositions:
		current_propositions.append("common.resource_matches(input.resource,statement_resource)")
	src = "rule_2"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'no_wildcard(a)'
	if "contains(a,\"*\")==false" not in propositions:
		propositions.append("contains(a,\"*\")==false")
	if "contains(a,\"*\")==false" not in current_propositions:
		current_propositions.append("contains(a,\"*\")==false")
	src = "rule_3"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'action_matches(in,stored)'
	if "no_wildcard(stored)" not in propositions:
		propositions.append("no_wildcard(stored)")
	if "no_wildcard(stored)" not in current_propositions:
		current_propositions.append("no_wildcard(stored)")
	if "in==stored" not in propositions:
		propositions.append("in==stored")
	if "in==stored" not in current_propositions:
		current_propositions.append("in==stored")
	src = "rule_4"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'action_matches(in,stored)=action_match(split(stored,":"),split(in,":"))'
	src = "rule_5"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'action_match([service,"*"],[service,_,_])=true'
	src = "rule_6"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'action_match([service,type,"*"],[service,type,_])=true'
	src = "rule_7"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'action_match([service,"*",verb],[service,_,verb])=true'
	src = "rule_8"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'action_match(["*",verb],[_,_,verb])=true'
	src = "rule_9"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'action_match(["*"],_)=true'
	src = "rule_10"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'has_action[[pol_id,statement_id]]'
	if "statement_action:=policies[pol_id].statements[statement_id].actions[_]" not in propositions:
		propositions.append("statement_action:=policies[pol_id].statements[statement_id].actions[_]")
	if "statement_action:=policies[pol_id].statements[statement_id].actions[_]" not in current_propositions:
		current_propositions.append("statement_action:=policies[pol_id].statements[statement_id].actions[_]")
	if "action_matches(input.action,statement_action)" not in propositions:
		propositions.append("action_matches(input.action,statement_action)")
	if "action_matches(input.action,statement_action)" not in current_propositions:
		current_propositions.append("action_matches(input.action,statement_action)")
	src = "rule_11"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'has_action[[pol_id,statement_id]]'
	if "policies[pol_id].statements[statement_id].role=role_id" not in propositions:
		propositions.append("policies[pol_id].statements[statement_id].role=role_id")
	if "policies[pol_id].statements[statement_id].role=role_id" not in current_propositions:
		current_propositions.append("policies[pol_id].statements[statement_id].role=role_id")
	if "roles[role_id].actions[_]=role_action" not in propositions:
		propositions.append("roles[role_id].actions[_]=role_action")
	if "roles[role_id].actions[_]=role_action" not in current_propositions:
		current_propositions.append("roles[role_id].actions[_]=role_action")
	if "action_matches(input.action,role_action)" not in propositions:
		propositions.append("action_matches(input.action,role_action)")
	if "action_matches(input.action,role_action)" not in current_propositions:
		current_propositions.append("action_matches(input.action,role_action)")
	src = "rule_12"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'has_project[[project,pol_id,statement_id]]'
	if "proj:=policies[pol_id].statements[statement_id].projects[_]" not in propositions:
		propositions.append("proj:=policies[pol_id].statements[statement_id].projects[_]")
	if "proj:=policies[pol_id].statements[statement_id].projects[_]" not in current_propositions:
		current_propositions.append("proj:=policies[pol_id].statements[statement_id].projects[_]")
	if "projects:=project_matches(proj)" not in propositions:
		propositions.append("projects:=project_matches(proj)")
	if "projects:=project_matches(proj)" not in current_propositions:
		current_propositions.append("projects:=project_matches(proj)")
	if "project:=projects[_]" not in propositions:
		propositions.append("project:=projects[_]")
	if "project:=projects[_]" not in current_propositions:
		current_propositions.append("project:=projects[_]")
	src = "rule_13"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'project_matches(proj)=projects'
	if "proj==common.const_all_projects" not in propositions:
		propositions.append("proj==common.const_all_projects")
	if "proj==common.const_all_projects" not in current_propositions:
		current_propositions.append("proj==common.const_all_projects")
	if "projects:=input.projects" not in propositions:
		propositions.append("projects:=input.projects")
	if "projects:=input.projects" not in current_propositions:
		current_propositions.append("projects:=input.projects")
	src = "rule_14"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'project_matches(proj)=projects'
	if "proj!=common.const_all_projects" not in propositions:
		propositions.append("proj!=common.const_all_projects")
	if "proj!=common.const_all_projects" not in current_propositions:
		current_propositions.append("proj!=common.const_all_projects")
	if "proj=input.projects[_]" not in propositions:
		propositions.append("proj=input.projects[_]")
	if "proj=input.projects[_]" not in current_propositions:
		current_propositions.append("proj=input.projects[_]")
	if "projects:=[proj]" not in propositions:
		propositions.append("projects:=[proj]")
	if "projects:=[proj]" not in current_propositions:
		current_propositions.append("projects:=[proj]")
	src = "rule_15"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'match[[effect,pol_id,statement_id]]'
	if "effect:=policies[pol_id].statements[statement_id].effect" not in propositions:
		propositions.append("effect:=policies[pol_id].statements[statement_id].effect")
	if "effect:=policies[pol_id].statements[statement_id].effect" not in current_propositions:
		current_propositions.append("effect:=policies[pol_id].statements[statement_id].effect")
	if "has_member[pol_id]" not in propositions:
		propositions.append("has_member[pol_id]")
	if "has_member[pol_id]" not in current_propositions:
		current_propositions.append("has_member[pol_id]")
	if "has_resource[[pol_id,statement_id]]" not in propositions:
		propositions.append("has_resource[[pol_id,statement_id]]")
	if "has_resource[[pol_id,statement_id]]" not in current_propositions:
		current_propositions.append("has_resource[[pol_id,statement_id]]")
	if "has_action[[pol_id,statement_id]]" not in propositions:
		propositions.append("has_action[[pol_id,statement_id]]")
	if "has_action[[pol_id,statement_id]]" not in current_propositions:
		current_propositions.append("has_action[[pol_id,statement_id]]")
	src = "rule_16"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'allow'
	if "match[[\"allow\",_,_]]" not in propositions:
		propositions.append("match[[\"allow\",_,_]]")
	if "match[[\"allow\",_,_]]" not in current_propositions:
		current_propositions.append("match[[\"allow\",_,_]]")
	src = "rule_17"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'deny'
	if "match[[\"deny\",_,_]]" not in propositions:
		propositions.append("match[[\"deny\",_,_]]")
	if "match[[\"deny\",_,_]]" not in current_propositions:
		current_propositions.append("match[[\"deny\",_,_]]")
	src = "rule_18"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'authorized'
	if "allow" not in propositions:
		propositions.append("allow")
	if "allow" not in current_propositions:
		current_propositions.append("allow")
	if "notdeny" not in propositions:
		propositions.append("notdeny")
	if "notdeny" not in current_propositions:
		current_propositions.append("notdeny")
	src = "rule_19"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'allowed_project[project]'
	if "match[[\"allow\",pol_id,statement_id]]" not in propositions:
		propositions.append("match[[\"allow\",pol_id,statement_id]]")
	if "match[[\"allow\",pol_id,statement_id]]" not in current_propositions:
		current_propositions.append("match[[\"allow\",pol_id,statement_id]]")
	if "has_project[[project,pol_id,statement_id]]" not in propositions:
		propositions.append("has_project[[project,pol_id,statement_id]]")
	if "has_project[[project,pol_id,statement_id]]" not in current_propositions:
		current_propositions.append("has_project[[project,pol_id,statement_id]]")
	src = "rule_20"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'denied_project[project]'
	if "match[[\"deny\",pol_id,statement_id]]" not in propositions:
		propositions.append("match[[\"deny\",pol_id,statement_id]]")
	if "match[[\"deny\",pol_id,statement_id]]" not in current_propositions:
		current_propositions.append("match[[\"deny\",pol_id,statement_id]]")
	if "has_project[[project,pol_id,statement_id]]" not in propositions:
		propositions.append("has_project[[project,pol_id,statement_id]]")
	if "has_project[[project,pol_id,statement_id]]" not in current_propositions:
		current_propositions.append("has_project[[project,pol_id,statement_id]]")
	src = "rule_21"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'authorized_project[project]'
	if "allowed_project[project]" not in propositions:
		propositions.append("allowed_project[project]")
	if "allowed_project[project]" not in current_propositions:
		current_propositions.append("allowed_project[project]")
	if "notdenied_project[project]" not in propositions:
		propositions.append("notdenied_project[project]")
	if "notdenied_project[project]" not in current_propositions:
		current_propositions.append("notdenied_project[project]")
	src = "rule_22"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []


	for prop in propositions:
		if prop in variables:
			variables.remove(prop)
	print("Variables : {}\n".format(variables))
	print("Propositions : {}\n".format(propositions))
	variable_set = set(variables)
	propositions_set = set(propositions)

	cm = ConditionalMetagraph(variable_set, propositions_set)
	cm.add_edges_from(edges)
	print(repr(cm))
	print("\n")
	for edge in cm.edges:
		source = edge.invertex
		target = {"allow"}
		print("Source, target: {}, {}".format(source, target))
		metapaths = cm.get_all_metapaths_from(source,target)
		for metapath in metapaths:
			print(repr(metapath))
		print("\n")
	g = Digraph("authz", filename="../metagraphs/authz.gv")
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
