from mgtoolkit.library import *
from graphviz import Digraph

if __name__ == "__main__":
	variables = []
	propositions = []
	current_propositions = []
	edges = []

	rule_head = 'deny[{"msg":message,"details":metadata,}]'
	if "constraint:=input.constraint" not in propositions:
		propositions.append("constraint:=input.constraint")
	if "constraint:=input.constraint" not in current_propositions:
		current_propositions.append("constraint:=input.constraint")
	if "lib.get_constraint_params(constraint,params)" not in propositions:
		propositions.append("lib.get_constraint_params(constraint,params)")
	if "lib.get_constraint_params(constraint,params)" not in current_propositions:
		current_propositions.append("lib.get_constraint_params(constraint,params)")
	if "rules_params:=update_params(params.rules[_])" not in propositions:
		propositions.append("rules_params:=update_params(params.rules[_])")
	if "rules_params:=update_params(params.rules[_])" not in current_propositions:
		current_propositions.append("rules_params:=update_params(params.rules[_])")
	if "asset:=input.asset" not in propositions:
		propositions.append("asset:=input.asset")
	if "asset:=input.asset" not in current_propositions:
		current_propositions.append("asset:=input.asset")
	if "asset.asset_type==\"compute.googleapis.com/Firewall\"" not in propositions:
		propositions.append("asset.asset_type==\"compute.googleapis.com/Firewall\"")
	if "asset.asset_type==\"compute.googleapis.com/Firewall\"" not in current_propositions:
		current_propositions.append("asset.asset_type==\"compute.googleapis.com/Firewall\"")
	if "fw_rule=asset.resource.data" not in propositions:
		propositions.append("fw_rule=asset.resource.data")
	if "fw_rule=asset.resource.data" not in current_propositions:
		current_propositions.append("fw_rule=asset.resource.data")
	if "fw_rule_is_restricted(fw_rule,rules_params)" not in propositions:
		propositions.append("fw_rule_is_restricted(fw_rule,rules_params)")
	if "fw_rule_is_restricted(fw_rule,rules_params)" not in current_propositions:
		current_propositions.append("fw_rule_is_restricted(fw_rule,rules_params)")
	if "message:=sprintf(\"%s Firewall rule is prohibited.\",[asset.name])" not in propositions:
		propositions.append("message:=sprintf(\"%s Firewall rule is prohibited.\",[asset.name])")
	if "message:=sprintf(\"%s Firewall rule is prohibited.\",[asset.name])" not in current_propositions:
		current_propositions.append("message:=sprintf(\"%s Firewall rule is prohibited.\",[asset.name])")
	if "metadata:={\"resource\":asset.name,\"restricted_rules\":rules_params,}" not in propositions:
		propositions.append("metadata:={\"resource\":asset.name,\"restricted_rules\":rules_params,}")
	if "metadata:={\"resource\":asset.name,\"restricted_rules\":rules_params,}" not in current_propositions:
		current_propositions.append("metadata:={\"resource\":asset.name,\"restricted_rules\":rules_params,}")
	src = "rule_0"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'fw_rule_is_restricted(fw_rule,params)'
	if "fw_rule_check_direction(fw_rule,params.direction)" not in propositions:
		propositions.append("fw_rule_check_direction(fw_rule,params.direction)")
	if "fw_rule_check_direction(fw_rule,params.direction)" not in current_propositions:
		current_propositions.append("fw_rule_check_direction(fw_rule,params.direction)")
	if "fw_rule_check_rule_type(fw_rule,params.rule_type)" not in propositions:
		propositions.append("fw_rule_check_rule_type(fw_rule,params.rule_type)")
	if "fw_rule_check_rule_type(fw_rule,params.rule_type)" not in current_propositions:
		current_propositions.append("fw_rule_check_rule_type(fw_rule,params.rule_type)")
	if "ip_configs:=fw_rule_get_ip_configs(fw_rule,params.rule_type)" not in propositions:
		propositions.append("ip_configs:=fw_rule_get_ip_configs(fw_rule,params.rule_type)")
	if "ip_configs:=fw_rule_get_ip_configs(fw_rule,params.rule_type)" not in current_propositions:
		current_propositions.append("ip_configs:=fw_rule_get_ip_configs(fw_rule,params.rule_type)")
	if "fw_rule_check_protocol_and_port(ip_configs,params.protocol,params.port)" not in propositions:
		propositions.append("fw_rule_check_protocol_and_port(ip_configs,params.protocol,params.port)")
	if "fw_rule_check_protocol_and_port(ip_configs,params.protocol,params.port)" not in current_propositions:
		current_propositions.append("fw_rule_check_protocol_and_port(ip_configs,params.protocol,params.port)")
	if "fw_rule_check_all_sources(fw_rule,params)" not in propositions:
		propositions.append("fw_rule_check_all_sources(fw_rule,params)")
	if "fw_rule_check_all_sources(fw_rule,params)" not in current_propositions:
		current_propositions.append("fw_rule_check_all_sources(fw_rule,params)")
	if "fw_rule_check_all_targets(fw_rule,params)" not in propositions:
		propositions.append("fw_rule_check_all_targets(fw_rule,params)")
	if "fw_rule_check_all_targets(fw_rule,params)" not in current_propositions:
		current_propositions.append("fw_rule_check_all_targets(fw_rule,params)")
	if "fw_rule_check_enabled(fw_rule,params.enabled)" not in propositions:
		propositions.append("fw_rule_check_enabled(fw_rule,params.enabled)")
	if "fw_rule_check_enabled(fw_rule,params.enabled)" not in current_propositions:
		current_propositions.append("fw_rule_check_enabled(fw_rule,params.enabled)")
	src = "rule_2"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'fw_rule_check_direction(fw_rule,direction)'
	if "direction==\"any\"" not in propositions:
		propositions.append("direction==\"any\"")
	if "direction==\"any\"" not in current_propositions:
		current_propositions.append("direction==\"any\"")
	src = "rule_3"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'fw_rule_check_direction(fw_rule,direction)'
	if "direction!=\"any\"" not in propositions:
		propositions.append("direction!=\"any\"")
	if "direction!=\"any\"" not in current_propositions:
		current_propositions.append("direction!=\"any\"")
	if "lower(direction)==lower(fw_rule.direction)" not in propositions:
		propositions.append("lower(direction)==lower(fw_rule.direction)")
	if "lower(direction)==lower(fw_rule.direction)" not in current_propositions:
		current_propositions.append("lower(direction)==lower(fw_rule.direction)")
	src = "rule_4"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'fw_rule_check_rule_type(fw_rule,rule_type)'
	if "rule_type==\"any\"" not in propositions:
		propositions.append("rule_type==\"any\"")
	if "rule_type==\"any\"" not in current_propositions:
		current_propositions.append("rule_type==\"any\"")
	src = "rule_5"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'fw_rule_check_rule_type(fw_rule,rule_type)'
	if "rule_type!=\"any\"" not in propositions:
		propositions.append("rule_type!=\"any\"")
	if "rule_type!=\"any\"" not in current_propositions:
		current_propositions.append("rule_type!=\"any\"")
	if "fw_rule[lower(rule_type)]" not in propositions:
		propositions.append("fw_rule[lower(rule_type)]")
	if "fw_rule[lower(rule_type)]" not in current_propositions:
		current_propositions.append("fw_rule[lower(rule_type)]")
	src = "rule_6"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'fw_rule_get_ip_configs(fw_rule,rule_type)=ip_configs'
	if "rule_type==\"any\"" not in propositions:
		propositions.append("rule_type==\"any\"")
	if "rule_type==\"any\"" not in current_propositions:
		current_propositions.append("rule_type==\"any\"")
	if "ip_configs=fw_rule.allowed" not in propositions:
		propositions.append("ip_configs=fw_rule.allowed")
	if "ip_configs=fw_rule.allowed" not in current_propositions:
		current_propositions.append("ip_configs=fw_rule.allowed")
	src = "rule_7"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'fw_rule_get_ip_configs(fw_rule,rule_type)=ip_configs'
	if "rule_type==\"any\"" not in propositions:
		propositions.append("rule_type==\"any\"")
	if "rule_type==\"any\"" not in current_propositions:
		current_propositions.append("rule_type==\"any\"")
	if "ip_configs=fw_rule.denied" not in propositions:
		propositions.append("ip_configs=fw_rule.denied")
	if "ip_configs=fw_rule.denied" not in current_propositions:
		current_propositions.append("ip_configs=fw_rule.denied")
	src = "rule_8"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'fw_rule_get_ip_configs(fw_rule,rule_type)=ip_configs'
	if "rule_type!=\"any\"" not in propositions:
		propositions.append("rule_type!=\"any\"")
	if "rule_type!=\"any\"" not in current_propositions:
		current_propositions.append("rule_type!=\"any\"")
	if "ip_configs=fw_rule[rule_type]" not in propositions:
		propositions.append("ip_configs=fw_rule[rule_type]")
	if "ip_configs=fw_rule[rule_type]" not in current_propositions:
		current_propositions.append("ip_configs=fw_rule[rule_type]")
	src = "rule_9"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'fw_rule_check_protocol_and_port(ip_configs,protocol,port)'
	if "ip_configs[_].IPProtocol==\"all\"" not in propositions:
		propositions.append("ip_configs[_].IPProtocol==\"all\"")
	if "ip_configs[_].IPProtocol==\"all\"" not in current_propositions:
		current_propositions.append("ip_configs[_].IPProtocol==\"all\"")
	src = "rule_10"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'fw_rule_check_protocol_and_port(ip_configs,protocol,port)'
	if "protocol==\"any\"" not in propositions:
		propositions.append("protocol==\"any\"")
	if "protocol==\"any\"" not in current_propositions:
		current_propositions.append("protocol==\"any\"")
	if "fw_rule_check_port(ip_configs[_],port)" not in propositions:
		propositions.append("fw_rule_check_port(ip_configs[_],port)")
	if "fw_rule_check_port(ip_configs[_],port)" not in current_propositions:
		current_propositions.append("fw_rule_check_port(ip_configs[_],port)")
	src = "rule_11"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'fw_rule_check_protocol_and_port(ip_configs,protocol,port)'
	if "protocol!=\"any\"" not in propositions:
		propositions.append("protocol!=\"any\"")
	if "protocol!=\"any\"" not in current_propositions:
		current_propositions.append("protocol!=\"any\"")
	if "ip_configs[i].IPProtocol==protocol" not in propositions:
		propositions.append("ip_configs[i].IPProtocol==protocol")
	if "ip_configs[i].IPProtocol==protocol" not in current_propositions:
		current_propositions.append("ip_configs[i].IPProtocol==protocol")
	if "fw_rule_check_port(ip_configs[i],port)" not in propositions:
		propositions.append("fw_rule_check_port(ip_configs[i],port)")
	if "fw_rule_check_port(ip_configs[i],port)" not in current_propositions:
		current_propositions.append("fw_rule_check_port(ip_configs[i],port)")
	src = "rule_12"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'fw_rule_check_port(ip_configs,port)'
	if "port==\"any\"" not in propositions:
		propositions.append("port==\"any\"")
	if "port==\"any\"" not in current_propositions:
		current_propositions.append("port==\"any\"")
	src = "rule_13"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'fw_rule_check_port(ip_config,port)'
	if "protocol_with_ports:={\"tcp\",\"udp\",\"all\"}" not in propositions:
		propositions.append("protocol_with_ports:={\"tcp\",\"udp\",\"all\"}")
	if "protocol_with_ports:={\"tcp\",\"udp\",\"all\"}" not in current_propositions:
		current_propositions.append("protocol_with_ports:={\"tcp\",\"udp\",\"all\"}")
	if "ip_config.IPProtocol==protocol_with_ports[_]" not in propositions:
		propositions.append("ip_config.IPProtocol==protocol_with_ports[_]")
	if "ip_config.IPProtocol==protocol_with_ports[_]" not in current_propositions:
		current_propositions.append("ip_config.IPProtocol==protocol_with_ports[_]")
	if "notip_config.ports" not in propositions:
		propositions.append("notip_config.ports")
	if "notip_config.ports" not in current_propositions:
		current_propositions.append("notip_config.ports")
	src = "rule_14"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'fw_rule_check_port(ip_config,port)'
	if "port!=\"any\"" not in propositions:
		propositions.append("port!=\"any\"")
	if "port!=\"any\"" not in current_propositions:
		current_propositions.append("port!=\"any\"")
	if "notre_match(\"-\",port)" not in propositions:
		propositions.append("notre_match(\"-\",port)")
	if "notre_match(\"-\",port)" not in current_propositions:
		current_propositions.append("notre_match(\"-\",port)")
	if "rule_ports:=ip_config.ports" not in propositions:
		propositions.append("rule_ports:=ip_config.ports")
	if "rule_ports:=ip_config.ports" not in current_propositions:
		current_propositions.append("rule_ports:=ip_config.ports")
	if "port_is_in_values(port,rule_ports[_])" not in propositions:
		propositions.append("port_is_in_values(port,rule_ports[_])")
	if "port_is_in_values(port,rule_ports[_])" not in current_propositions:
		current_propositions.append("port_is_in_values(port,rule_ports[_])")
	src = "rule_15"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'fw_rule_check_port(ip_config,port)'
	if "port!=\"any\"" not in propositions:
		propositions.append("port!=\"any\"")
	if "port!=\"any\"" not in current_propositions:
		current_propositions.append("port!=\"any\"")
	if "re_match(\"-\",port)" not in propositions:
		propositions.append("re_match(\"-\",port)")
	if "re_match(\"-\",port)" not in current_propositions:
		current_propositions.append("re_match(\"-\",port)")
	if "rule_ports:=ip_config.ports" not in propositions:
		propositions.append("rule_ports:=ip_config.ports")
	if "rule_ports:=ip_config.ports" not in current_propositions:
		current_propositions.append("rule_ports:=ip_config.ports")
	if "rule_port:=rule_ports[_]" not in propositions:
		propositions.append("rule_port:=rule_ports[_]")
	if "rule_port:=rule_ports[_]" not in current_propositions:
		current_propositions.append("rule_port:=rule_ports[_]")
	if "range_match(port,rule_port)" not in propositions:
		propositions.append("range_match(port,rule_port)")
	if "range_match(port,rule_port)" not in current_propositions:
		current_propositions.append("range_match(port,rule_port)")
	src = "rule_16"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'port_is_in_values(port,rule_port)'
	if "notre_match(\"-\",rule_port)" not in propositions:
		propositions.append("notre_match(\"-\",rule_port)")
	if "notre_match(\"-\",rule_port)" not in current_propositions:
		current_propositions.append("notre_match(\"-\",rule_port)")
	if "rule_port==port" not in propositions:
		propositions.append("rule_port==port")
	if "rule_port==port" not in current_propositions:
		current_propositions.append("rule_port==port")
	src = "rule_17"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'port_is_in_values(port,rule_port)'
	if "re_match(\"-\",rule_port)" not in propositions:
		propositions.append("re_match(\"-\",rule_port)")
	if "re_match(\"-\",rule_port)" not in current_propositions:
		current_propositions.append("re_match(\"-\",rule_port)")
	if "port_range:=sprintf(\"%s-%s\",[port,port])" not in propositions:
		propositions.append("port_range:=sprintf(\"%s-%s\",[port,port])")
	if "port_range:=sprintf(\"%s-%s\",[port,port])" not in current_propositions:
		current_propositions.append("port_range:=sprintf(\"%s-%s\",[port,port])")
	if "range_match(port_range,rule_port)" not in propositions:
		propositions.append("range_match(port_range,rule_port)")
	if "range_match(port_range,rule_port)" not in current_propositions:
		current_propositions.append("range_match(port_range,rule_port)")
	src = "rule_18"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'range_match(test_range,target_range)'
	if "re_match(\"-\",target_range)" not in propositions:
		propositions.append("re_match(\"-\",target_range)")
	if "re_match(\"-\",target_range)" not in current_propositions:
		current_propositions.append("re_match(\"-\",target_range)")
	if "re_match(\"-\",test_range)" not in propositions:
		propositions.append("re_match(\"-\",test_range)")
	if "re_match(\"-\",test_range)" not in current_propositions:
		current_propositions.append("re_match(\"-\",test_range)")
	if "target_range_bounds:=split(target_range,\"-\")" not in propositions:
		propositions.append("target_range_bounds:=split(target_range,\"-\")")
	if "target_range_bounds:=split(target_range,\"-\")" not in current_propositions:
		current_propositions.append("target_range_bounds:=split(target_range,\"-\")")
	if "target_low_bound:=to_number(target_range_bounds[0])" not in propositions:
		propositions.append("target_low_bound:=to_number(target_range_bounds[0])")
	if "target_low_bound:=to_number(target_range_bounds[0])" not in current_propositions:
		current_propositions.append("target_low_bound:=to_number(target_range_bounds[0])")
	if "target_high_bound:=to_number(target_range_bounds[1])" not in propositions:
		propositions.append("target_high_bound:=to_number(target_range_bounds[1])")
	if "target_high_bound:=to_number(target_range_bounds[1])" not in current_propositions:
		current_propositions.append("target_high_bound:=to_number(target_range_bounds[1])")
	if "test_range_bounds:=split(test_range,\"-\")" not in propositions:
		propositions.append("test_range_bounds:=split(test_range,\"-\")")
	if "test_range_bounds:=split(test_range,\"-\")" not in current_propositions:
		current_propositions.append("test_range_bounds:=split(test_range,\"-\")")
	if "test_low_bound:=to_number(test_range_bounds[0])" not in propositions:
		propositions.append("test_low_bound:=to_number(test_range_bounds[0])")
	if "test_low_bound:=to_number(test_range_bounds[0])" not in current_propositions:
		current_propositions.append("test_low_bound:=to_number(test_range_bounds[0])")
	if "test_high_bound:=to_number(test_range_bounds[1])" not in propositions:
		propositions.append("test_high_bound:=to_number(test_range_bounds[1])")
	if "test_high_bound:=to_number(test_range_bounds[1])" not in current_propositions:
		current_propositions.append("test_high_bound:=to_number(test_range_bounds[1])")
	if "test_low_bound>=target_low_bound" not in propositions:
		propositions.append("test_low_bound>=target_low_bound")
	if "test_low_bound>=target_low_bound" not in current_propositions:
		current_propositions.append("test_low_bound>=target_low_bound")
	if "test_high_bound<=target_high_bound" not in propositions:
		propositions.append("test_high_bound<=target_high_bound")
	if "test_high_bound<=target_high_bound" not in current_propositions:
		current_propositions.append("test_high_bound<=target_high_bound")
	src = "rule_19"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'fw_rule_check_all_sources(fw_rule,params)'
	if "fw_rule_check_source_range(fw_rule,params.source_ranges[_])" not in propositions:
		propositions.append("fw_rule_check_source_range(fw_rule,params.source_ranges[_])")
	if "fw_rule_check_source_range(fw_rule,params.source_ranges[_])" not in current_propositions:
		current_propositions.append("fw_rule_check_source_range(fw_rule,params.source_ranges[_])")
	if "fw_rule_check_source_tag(fw_rule,params.source_tags[_])" not in propositions:
		propositions.append("fw_rule_check_source_tag(fw_rule,params.source_tags[_])")
	if "fw_rule_check_source_tag(fw_rule,params.source_tags[_])" not in current_propositions:
		current_propositions.append("fw_rule_check_source_tag(fw_rule,params.source_tags[_])")
	if "fw_rule_check_source_sas(fw_rule,params.source_service_accounts[_])" not in propositions:
		propositions.append("fw_rule_check_source_sas(fw_rule,params.source_service_accounts[_])")
	if "fw_rule_check_source_sas(fw_rule,params.source_service_accounts[_])" not in current_propositions:
		current_propositions.append("fw_rule_check_source_sas(fw_rule,params.source_service_accounts[_])")
	src = "rule_20"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'fw_rule_check_source_range(fw_rule,source_range)'
	if "fw_rule.sourceRanges" not in propositions:
		propositions.append("fw_rule.sourceRanges")
	if "fw_rule.sourceRanges" not in current_propositions:
		current_propositions.append("fw_rule.sourceRanges")
	if "fw_rule_ranges=fw_rule.sourceRanges" not in propositions:
		propositions.append("fw_rule_ranges=fw_rule.sourceRanges")
	if "fw_rule_ranges=fw_rule.sourceRanges" not in current_propositions:
		current_propositions.append("fw_rule_ranges=fw_rule.sourceRanges")
	if "source_range==fw_rule_ranges[_]" not in propositions:
		propositions.append("source_range==fw_rule_ranges[_]")
	if "source_range==fw_rule_ranges[_]" not in current_propositions:
		current_propositions.append("source_range==fw_rule_ranges[_]")
	src = "rule_21"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'fw_rule_check_source_range(fw_rule,source_range)'
	if "source_range==\"*\"" not in propositions:
		propositions.append("source_range==\"*\"")
	if "source_range==\"*\"" not in current_propositions:
		current_propositions.append("source_range==\"*\"")
	if "fw_rule.sourceRanges" not in propositions:
		propositions.append("fw_rule.sourceRanges")
	if "fw_rule.sourceRanges" not in current_propositions:
		current_propositions.append("fw_rule.sourceRanges")
	src = "rule_22"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'fw_rule_check_source_range(fw_rule,source_range)'
	if "source_range==\"any\"" not in propositions:
		propositions.append("source_range==\"any\"")
	if "source_range==\"any\"" not in current_propositions:
		current_propositions.append("source_range==\"any\"")
	src = "rule_23"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'fw_rule_check_source_tag(fw_rule,source_tag)'
	if "source_tag!=\"*\"" not in propositions:
		propositions.append("source_tag!=\"*\"")
	if "source_tag!=\"*\"" not in current_propositions:
		current_propositions.append("source_tag!=\"*\"")
	if "fw_rule_source_tags:=fw_rule.sourceTags" not in propositions:
		propositions.append("fw_rule_source_tags:=fw_rule.sourceTags")
	if "fw_rule_source_tags:=fw_rule.sourceTags" not in current_propositions:
		current_propositions.append("fw_rule_source_tags:=fw_rule.sourceTags")
	if "re_match(source_tag,fw_rule_source_tags[_])" not in propositions:
		propositions.append("re_match(source_tag,fw_rule_source_tags[_])")
	if "re_match(source_tag,fw_rule_source_tags[_])" not in current_propositions:
		current_propositions.append("re_match(source_tag,fw_rule_source_tags[_])")
	src = "rule_24"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'fw_rule_check_source_tag(fw_rule,source_tag)'
	if "source_tag==\"*\"" not in propositions:
		propositions.append("source_tag==\"*\"")
	if "source_tag==\"*\"" not in current_propositions:
		current_propositions.append("source_tag==\"*\"")
	if "fw_rule.sourceTags" not in propositions:
		propositions.append("fw_rule.sourceTags")
	if "fw_rule.sourceTags" not in current_propositions:
		current_propositions.append("fw_rule.sourceTags")
	src = "rule_25"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'fw_rule_check_source_tag(fw_rule,source_tag)'
	if "source_tag==\"any\"" not in propositions:
		propositions.append("source_tag==\"any\"")
	if "source_tag==\"any\"" not in current_propositions:
		current_propositions.append("source_tag==\"any\"")
	src = "rule_26"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'fw_rule_check_source_sas(fw_rule,source_service_account)'
	if "source_service_account!=\"*\"" not in propositions:
		propositions.append("source_service_account!=\"*\"")
	if "source_service_account!=\"*\"" not in current_propositions:
		current_propositions.append("source_service_account!=\"*\"")
	if "fw_rule_source_sas=fw_rule.sourceServiceAccounts" not in propositions:
		propositions.append("fw_rule_source_sas=fw_rule.sourceServiceAccounts")
	if "fw_rule_source_sas=fw_rule.sourceServiceAccounts" not in current_propositions:
		current_propositions.append("fw_rule_source_sas=fw_rule.sourceServiceAccounts")
	if "re_match(source_service_account,fw_rule_source_sas[_])" not in propositions:
		propositions.append("re_match(source_service_account,fw_rule_source_sas[_])")
	if "re_match(source_service_account,fw_rule_source_sas[_])" not in current_propositions:
		current_propositions.append("re_match(source_service_account,fw_rule_source_sas[_])")
	src = "rule_27"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'fw_rule_check_source_sas(fw_rule,source_service_account)'
	if "source_service_account==\"*\"" not in propositions:
		propositions.append("source_service_account==\"*\"")
	if "source_service_account==\"*\"" not in current_propositions:
		current_propositions.append("source_service_account==\"*\"")
	if "fw_rule.sourceServiceAccounts" not in propositions:
		propositions.append("fw_rule.sourceServiceAccounts")
	if "fw_rule.sourceServiceAccounts" not in current_propositions:
		current_propositions.append("fw_rule.sourceServiceAccounts")
	src = "rule_28"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'fw_rule_check_source_sas(fw_rule,source_service_account)'
	if "source_service_account==\"any\"" not in propositions:
		propositions.append("source_service_account==\"any\"")
	if "source_service_account==\"any\"" not in current_propositions:
		current_propositions.append("source_service_account==\"any\"")
	src = "rule_29"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'fw_rule_check_all_targets(fw_rule,params)'
	if "fw_rule_check_target_range(fw_rule,params.target_ranges[_])" not in propositions:
		propositions.append("fw_rule_check_target_range(fw_rule,params.target_ranges[_])")
	if "fw_rule_check_target_range(fw_rule,params.target_ranges[_])" not in current_propositions:
		current_propositions.append("fw_rule_check_target_range(fw_rule,params.target_ranges[_])")
	if "fw_rule_check_target_tag(fw_rule,params.target_tags[_])" not in propositions:
		propositions.append("fw_rule_check_target_tag(fw_rule,params.target_tags[_])")
	if "fw_rule_check_target_tag(fw_rule,params.target_tags[_])" not in current_propositions:
		current_propositions.append("fw_rule_check_target_tag(fw_rule,params.target_tags[_])")
	if "fw_rule_check_target_sas(fw_rule,params.target_service_accounts[_])" not in propositions:
		propositions.append("fw_rule_check_target_sas(fw_rule,params.target_service_accounts[_])")
	if "fw_rule_check_target_sas(fw_rule,params.target_service_accounts[_])" not in current_propositions:
		current_propositions.append("fw_rule_check_target_sas(fw_rule,params.target_service_accounts[_])")
	src = "rule_30"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'fw_rule_check_target_range(fw_rule,target_range)'
	if "fw_rule.destinationRanges" not in propositions:
		propositions.append("fw_rule.destinationRanges")
	if "fw_rule.destinationRanges" not in current_propositions:
		current_propositions.append("fw_rule.destinationRanges")
	if "fw_rule_ranges=fw_rule.destinationRanges" not in propositions:
		propositions.append("fw_rule_ranges=fw_rule.destinationRanges")
	if "fw_rule_ranges=fw_rule.destinationRanges" not in current_propositions:
		current_propositions.append("fw_rule_ranges=fw_rule.destinationRanges")
	if "target_range==fw_rule_ranges[_]" not in propositions:
		propositions.append("target_range==fw_rule_ranges[_]")
	if "target_range==fw_rule_ranges[_]" not in current_propositions:
		current_propositions.append("target_range==fw_rule_ranges[_]")
	src = "rule_31"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'fw_rule_check_target_range(fw_rule,target_range)'
	if "target_range==\"*\"" not in propositions:
		propositions.append("target_range==\"*\"")
	if "target_range==\"*\"" not in current_propositions:
		current_propositions.append("target_range==\"*\"")
	if "fw_rule.destinationRanges" not in propositions:
		propositions.append("fw_rule.destinationRanges")
	if "fw_rule.destinationRanges" not in current_propositions:
		current_propositions.append("fw_rule.destinationRanges")
	src = "rule_32"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'fw_rule_check_target_range(fw_rule,target_range)'
	if "target_range==\"any\"" not in propositions:
		propositions.append("target_range==\"any\"")
	if "target_range==\"any\"" not in current_propositions:
		current_propositions.append("target_range==\"any\"")
	src = "rule_33"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'fw_rule_check_target_tag(fw_rule,target_tag)'
	if "target_tag!=\"*\"" not in propositions:
		propositions.append("target_tag!=\"*\"")
	if "target_tag!=\"*\"" not in current_propositions:
		current_propositions.append("target_tag!=\"*\"")
	if "fw_rule_target_tags:=fw_rule.targetTags" not in propositions:
		propositions.append("fw_rule_target_tags:=fw_rule.targetTags")
	if "fw_rule_target_tags:=fw_rule.targetTags" not in current_propositions:
		current_propositions.append("fw_rule_target_tags:=fw_rule.targetTags")
	if "re_match(target_tag,fw_rule_target_tags[_])" not in propositions:
		propositions.append("re_match(target_tag,fw_rule_target_tags[_])")
	if "re_match(target_tag,fw_rule_target_tags[_])" not in current_propositions:
		current_propositions.append("re_match(target_tag,fw_rule_target_tags[_])")
	src = "rule_34"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'fw_rule_check_target_tag(fw_rule,target_tag)'
	if "target_tag==\"*\"" not in propositions:
		propositions.append("target_tag==\"*\"")
	if "target_tag==\"*\"" not in current_propositions:
		current_propositions.append("target_tag==\"*\"")
	if "fw_rule.targetTags" not in propositions:
		propositions.append("fw_rule.targetTags")
	if "fw_rule.targetTags" not in current_propositions:
		current_propositions.append("fw_rule.targetTags")
	src = "rule_35"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'fw_rule_check_target_tag(fw_rule,target_tag)'
	if "target_tag==\"any\"" not in propositions:
		propositions.append("target_tag==\"any\"")
	if "target_tag==\"any\"" not in current_propositions:
		current_propositions.append("target_tag==\"any\"")
	src = "rule_36"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'fw_rule_check_target_sas(fw_rule,target_service_account)'
	if "target_service_account!=\"*\"" not in propositions:
		propositions.append("target_service_account!=\"*\"")
	if "target_service_account!=\"*\"" not in current_propositions:
		current_propositions.append("target_service_account!=\"*\"")
	if "fw_rule_target_sas=fw_rule.targetServiceAccounts" not in propositions:
		propositions.append("fw_rule_target_sas=fw_rule.targetServiceAccounts")
	if "fw_rule_target_sas=fw_rule.targetServiceAccounts" not in current_propositions:
		current_propositions.append("fw_rule_target_sas=fw_rule.targetServiceAccounts")
	if "re_match(target_service_account,fw_rule_target_sas[_])" not in propositions:
		propositions.append("re_match(target_service_account,fw_rule_target_sas[_])")
	if "re_match(target_service_account,fw_rule_target_sas[_])" not in current_propositions:
		current_propositions.append("re_match(target_service_account,fw_rule_target_sas[_])")
	src = "rule_37"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'fw_rule_check_target_sas(fw_rule,target_service_account)'
	if "target_service_account==\"*\"" not in propositions:
		propositions.append("target_service_account==\"*\"")
	if "target_service_account==\"*\"" not in current_propositions:
		current_propositions.append("target_service_account==\"*\"")
	if "fw_rule.targetServiceAccounts" not in propositions:
		propositions.append("fw_rule.targetServiceAccounts")
	if "fw_rule.targetServiceAccounts" not in current_propositions:
		current_propositions.append("fw_rule.targetServiceAccounts")
	src = "rule_38"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'fw_rule_check_target_sas(fw_rule,target_service_account)'
	if "target_service_account==\"any\"" not in propositions:
		propositions.append("target_service_account==\"any\"")
	if "target_service_account==\"any\"" not in current_propositions:
		current_propositions.append("target_service_account==\"any\"")
	src = "rule_39"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'fw_rule_check_enabled(fw_rule,enabled)'
	if "enabled==\"any\"" not in propositions:
		propositions.append("enabled==\"any\"")
	if "enabled==\"any\"" not in current_propositions:
		current_propositions.append("enabled==\"any\"")
	src = "rule_40"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'fw_rule_check_enabled(fw_rule,enabled)'
	if "enabled!=\"any\"" not in propositions:
		propositions.append("enabled!=\"any\"")
	if "enabled!=\"any\"" not in current_propositions:
		current_propositions.append("enabled!=\"any\"")
	if "is_boolean(enabled)" not in propositions:
		propositions.append("is_boolean(enabled)")
	if "is_boolean(enabled)" not in current_propositions:
		current_propositions.append("is_boolean(enabled)")
	if "enabled!=fw_rule.disabled" not in propositions:
		propositions.append("enabled!=fw_rule.disabled")
	if "enabled!=fw_rule.disabled" not in current_propositions:
		current_propositions.append("enabled!=fw_rule.disabled")
	src = "rule_41"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'fw_rule_check_enabled(fw_rule,enabled)'
	if "enabled!=\"any\"" not in propositions:
		propositions.append("enabled!=\"any\"")
	if "enabled!=\"any\"" not in current_propositions:
		current_propositions.append("enabled!=\"any\"")
	if "is_string(enabled)" not in propositions:
		propositions.append("is_string(enabled)")
	if "is_string(enabled)" not in current_propositions:
		current_propositions.append("is_string(enabled)")
	if "lower(enabled)==\"true\"" not in propositions:
		propositions.append("lower(enabled)==\"true\"")
	if "lower(enabled)==\"true\"" not in current_propositions:
		current_propositions.append("lower(enabled)==\"true\"")
	if "notfw_rule.disabled" not in propositions:
		propositions.append("notfw_rule.disabled")
	if "notfw_rule.disabled" not in current_propositions:
		current_propositions.append("notfw_rule.disabled")
	src = "rule_42"
	variables.append(src)
	dst = rule_head
	if dst not in variables:
		variables.append(dst)
	edges.append(Edge({src}, {dst}, attributes=current_propositions))
	current_propositions = []

	rule_head = 'fw_rule_check_enabled(fw_rule,enabled)'
	if "enabled!=\"any\"" not in propositions:
		propositions.append("enabled!=\"any\"")
	if "enabled!=\"any\"" not in current_propositions:
		current_propositions.append("enabled!=\"any\"")
	if "is_string(enabled)" not in propositions:
		propositions.append("is_string(enabled)")
	if "is_string(enabled)" not in current_propositions:
		current_propositions.append("is_string(enabled)")
	if "lower(enabled)==\"false\"" not in propositions:
		propositions.append("lower(enabled)==\"false\"")
	if "lower(enabled)==\"false\"" not in current_propositions:
		current_propositions.append("lower(enabled)==\"false\"")
	if "fw_rule.disabled" not in propositions:
		propositions.append("fw_rule.disabled")
	if "fw_rule.disabled" not in current_propositions:
		current_propositions.append("fw_rule.disabled")
	src = "rule_43"
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
	g = Digraph("restricted_firewall_rules", filename="../metagraphs/restricted_firewall_rules.gv")
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
