from mgtoolkit.library import *
from graphviz import Digraph

if __name__ == "__main__":
	variables = []
	propositions = []
	current_propositions = []
	edges = []

	rule_head = 'namespace=n'
	if "n:=input.AdmissionRequest.object.metadata.namespace" not in propositions:
		propositions.append("n:=input.AdmissionRequest.object.metadata.namespace")
	if "n:=input.AdmissionRequest.object.metadata.namespace" not in current_propositions:
		current_propositions.append("n:=input.AdmissionRequest.object.metadata.namespace")
	if "n:=input.AdmissionRequest.namespace" not in propositions:
		propositions.append("n:=input.AdmissionRequest.namespace")
	if "n:=input.AdmissionRequest.namespace" not in current_propositions:
		current_propositions.append("n:=input.AdmissionRequest.namespace")
	src = "rule_0"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'policy_action_or_empty(policy)=action'
	if "action:=policy.action" not in propositions:
		propositions.append("action:=policy.action")
	if "action:=policy.action" not in current_propositions:
		current_propositions.append("action:=policy.action")
	if "action:=\"<empty>\"" not in propositions:
		propositions.append("action:=\"<empty>\"")
	if "action:=\"<empty>\"" not in current_propositions:
		current_propositions.append("action:=\"<empty>\"")
	src = "rule_1"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'namespace_str(ns)=str'
	if "ns==true" not in propositions:
		propositions.append("ns==true")
	if "ns==true" not in current_propositions:
		current_propositions.append("ns==true")
	if "str:=sprintf(\"Namespace '%s'\",[namespace])" not in propositions:
		propositions.append("str:=sprintf(\"Namespace '%s'\",[namespace])")
	if "str:=sprintf(\"Namespace '%s'\",[namespace])" not in current_propositions:
		current_propositions.append("str:=sprintf(\"Namespace '%s'\",[namespace])")
	if "str:=\"Global\"" not in propositions:
		propositions.append("str:=\"Global\"")
	if "str:=\"Global\"" not in current_propositions:
		current_propositions.append("str:=\"Global\"")
	src = "rule_2"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'policy_str(prefix)=str'
	if "prefix==null" not in propositions:
		propositions.append("prefix==null")
	if "prefix==null" not in current_propositions:
		current_propositions.append("prefix==null")
	if "str:=\"default policy\"" not in propositions:
		propositions.append("str:=\"default policy\"")
	if "str:=\"default policy\"" not in current_propositions:
		current_propositions.append("str:=\"default policy\"")
	if "str:=sprintf(\"custom policy (prefix '%s')\",[prefix])" not in propositions:
		propositions.append("str:=sprintf(\"custom policy (prefix '%s')\",[prefix])")
	if "str:=sprintf(\"custom policy (prefix '%s')\",[prefix])" not in current_propositions:
		current_propositions.append("str:=sprintf(\"custom policy (prefix '%s')\",[prefix])")
	src = "rule_3"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'scope_str(ns,prefix)=str'
	if "str:=sprintf(\"%s %s\",[namespace_str(ns),policy_str(prefix)])" not in propositions:
		propositions.append("str:=sprintf(\"%s %s\",[namespace_str(ns),policy_str(prefix)])")
	if "str:=sprintf(\"%s %s\",[namespace_str(ns),policy_str(prefix)])" not in current_propositions:
		current_propositions.append("str:=sprintf(\"%s %s\",[namespace_str(ns),policy_str(prefix)])")
	src = "rule_4"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'valid_policy_value[value]'
	if "value=valid_policy_values[_]" not in propositions:
		propositions.append("value=valid_policy_values[_]")
	if "value=valid_policy_values[_]" not in current_propositions:
		current_propositions.append("value=valid_policy_values[_]")
	src = "rule_5"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'config_error["AdmissionRequest is missing in input"]'
	if "notinput.AdmissionRequest" not in propositions:
		propositions.append("notinput.AdmissionRequest")
	if "notinput.AdmissionRequest" not in current_propositions:
		current_propositions.append("notinput.AdmissionRequest")
	src = "rule_6"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'invalid_default_policy[value]'
	if "value:=policies.defaultPolicy" not in propositions:
		propositions.append("value:=policies.defaultPolicy")
	if "value:=policies.defaultPolicy" not in current_propositions:
		current_propositions.append("value:=policies.defaultPolicy")
	if "notvalid_policy_value[value]" not in propositions:
		propositions.append("notvalid_policy_value[value]")
	if "notvalid_policy_value[value]" not in current_propositions:
		current_propositions.append("notvalid_policy_value[value]")
	src = "rule_7"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'invalid_default_policy["<empty>"]'
	if "notpolicies.defaultPolicy" not in propositions:
		propositions.append("notpolicies.defaultPolicy")
	if "notpolicies.defaultPolicy" not in current_propositions:
		current_propositions.append("notpolicies.defaultPolicy")
	src = "rule_8"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'config_error[msg]'
	if "invalid_default_policy[value]" not in propositions:
		propositions.append("invalid_default_policy[value]")
	if "invalid_default_policy[value]" not in current_propositions:
		current_propositions.append("invalid_default_policy[value]")
	if "msg=sprintf(\"Invalid value for defaultPolicy - '%s'\",[value])" not in propositions:
		propositions.append("msg=sprintf(\"Invalid value for defaultPolicy - '%s'\",[value])")
	if "msg=sprintf(\"Invalid value for defaultPolicy - '%s'\",[value])" not in current_propositions:
		current_propositions.append("msg=sprintf(\"Invalid value for defaultPolicy - '%s'\",[value])")
	src = "rule_9"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'config_error[msg]'
	if "value:=policies.byNamespace[namespace].defaultPolicy" not in propositions:
		propositions.append("value:=policies.byNamespace[namespace].defaultPolicy")
	if "value:=policies.byNamespace[namespace].defaultPolicy" not in current_propositions:
		current_propositions.append("value:=policies.byNamespace[namespace].defaultPolicy")
	if "notvalid_policy_value[value]" not in propositions:
		propositions.append("notvalid_policy_value[value]")
	if "notvalid_policy_value[value]" not in current_propositions:
		current_propositions.append("notvalid_policy_value[value]")
	if "msg:=sprintf(\"Invalid value for defaultPolicy for namespace '%s' - '%s'\",[namespace,value])" not in propositions:
		propositions.append("msg:=sprintf(\"Invalid value for defaultPolicy for namespace '%s' - '%s'\",[namespace,value])")
	if "msg:=sprintf(\"Invalid value for defaultPolicy for namespace '%s' - '%s'\",[namespace,value])" not in current_propositions:
		current_propositions.append("msg:=sprintf(\"Invalid value for defaultPolicy for namespace '%s' - '%s'\",[namespace,value])")
	src = "rule_10"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'config_error[msg]'
	if "imagePolicy.ns==false" not in propositions:
		propositions.append("imagePolicy.ns==false")
	if "imagePolicy.ns==false" not in current_propositions:
		current_propositions.append("imagePolicy.ns==false")
	if "notimagePolicy.prefix==null" not in propositions:
		propositions.append("notimagePolicy.prefix==null")
	if "notimagePolicy.prefix==null" not in current_propositions:
		current_propositions.append("notimagePolicy.prefix==null")
	if "notvalid_policy_value[imagePolicy.action]" not in propositions:
		propositions.append("notvalid_policy_value[imagePolicy.action]")
	if "notvalid_policy_value[imagePolicy.action]" not in current_propositions:
		current_propositions.append("notvalid_policy_value[imagePolicy.action]")
	if "msg:=sprintf(\"Invalid value for customPolicy with prefix '%s' - '%s'\",[imagePolicy.prefix,imagePolicy.action])" not in propositions:
		propositions.append("msg:=sprintf(\"Invalid value for customPolicy with prefix '%s' - '%s'\",[imagePolicy.prefix,imagePolicy.action])")
	if "msg:=sprintf(\"Invalid value for customPolicy with prefix '%s' - '%s'\",[imagePolicy.prefix,imagePolicy.action])" not in current_propositions:
		current_propositions.append("msg:=sprintf(\"Invalid value for customPolicy with prefix '%s' - '%s'\",[imagePolicy.prefix,imagePolicy.action])")
	src = "rule_11"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'config_error[msg]'
	if "imagePolicy.ns==true" not in propositions:
		propositions.append("imagePolicy.ns==true")
	if "imagePolicy.ns==true" not in current_propositions:
		current_propositions.append("imagePolicy.ns==true")
	if "notimagePolicy.prefix==null" not in propositions:
		propositions.append("notimagePolicy.prefix==null")
	if "notimagePolicy.prefix==null" not in current_propositions:
		current_propositions.append("notimagePolicy.prefix==null")
	if "notvalid_policy_value[imagePolicy.action]" not in propositions:
		propositions.append("notvalid_policy_value[imagePolicy.action]")
	if "notvalid_policy_value[imagePolicy.action]" not in current_propositions:
		current_propositions.append("notvalid_policy_value[imagePolicy.action]")
	if "msg:=sprintf(\"Invalid value for namespace '%s' customPolicy with prefix '%s' - '%s'\",[namespace,imagePolicy.prefix,imagePolicy.action])" not in propositions:
		propositions.append("msg:=sprintf(\"Invalid value for namespace '%s' customPolicy with prefix '%s' - '%s'\",[namespace,imagePolicy.prefix,imagePolicy.action])")
	if "msg:=sprintf(\"Invalid value for namespace '%s' customPolicy with prefix '%s' - '%s'\",[namespace,imagePolicy.prefix,imagePolicy.action])" not in current_propositions:
		current_propositions.append("msg:=sprintf(\"Invalid value for namespace '%s' customPolicy with prefix '%s' - '%s'\",[namespace,imagePolicy.prefix,imagePolicy.action])")
	src = "rule_12"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'first_matching_custom_policy(policies,image)=['
	src = "rule_13"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'c'
	src = "rule_14"
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
	g = Digraph("commonrules", filename="../metagraphs/commonrules.gv")
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
