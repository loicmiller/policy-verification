import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
from PolicyMetagraph import PolicyMetagraph

from mgtoolkit.library import *


def generate_metagraph():
	policy_mg = PolicyMetagraph()
	rule_head = 'allow'
	src = "rule_0"
	policy_mg.variables.append(src)
	dst = rule_head
	if dst not in policy_mg.variables:
		policy_mg.variables.append(dst)
	policy_mg.edges.append(Edge({src}, {dst}, attributes=policy_mg.current_propositions))
	policy_mg.current_propositions = []

	rule_head = 'allow'
	if "user_is_owner" not in policy_mg.propositions:
		policy_mg.propositions.append("user_is_owner")
	if "user_is_owner" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("user_is_owner")
	src = "rule_1"
	policy_mg.variables.append(src)
	dst = rule_head
	if dst not in policy_mg.variables:
		policy_mg.variables.append(dst)
	policy_mg.edges.append(Edge({src}, {dst}, attributes=policy_mg.current_propositions))
	policy_mg.current_propositions = []

	rule_head = 'allow'
	if "user_is_employee" not in policy_mg.propositions:
		policy_mg.propositions.append("user_is_employee")
	if "user_is_employee" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("user_is_employee")
	if "action_is_read" not in policy_mg.propositions:
		policy_mg.propositions.append("action_is_read")
	if "action_is_read" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("action_is_read")
	src = "rule_2"
	policy_mg.variables.append(src)
	dst = rule_head
	if dst not in policy_mg.variables:
		policy_mg.variables.append(dst)
	policy_mg.edges.append(Edge({src}, {dst}, attributes=policy_mg.current_propositions))
	policy_mg.current_propositions = []

	rule_head = 'allow'
	if "user_is_employee" not in policy_mg.propositions:
		policy_mg.propositions.append("user_is_employee")
	if "user_is_employee" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("user_is_employee")
	if "user_is_senior" not in policy_mg.propositions:
		policy_mg.propositions.append("user_is_senior")
	if "user_is_senior" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("user_is_senior")
	if "action_is_update" not in policy_mg.propositions:
		policy_mg.propositions.append("action_is_update")
	if "action_is_update" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("action_is_update")
	src = "rule_3"
	policy_mg.variables.append(src)
	dst = rule_head
	if dst not in policy_mg.variables:
		policy_mg.variables.append(dst)
	policy_mg.edges.append(Edge({src}, {dst}, attributes=policy_mg.current_propositions))
	policy_mg.current_propositions = []

	rule_head = 'allow'
	if "user_is_customer" not in policy_mg.propositions:
		policy_mg.propositions.append("user_is_customer")
	if "user_is_customer" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("user_is_customer")
	if "action_is_read" not in policy_mg.propositions:
		policy_mg.propositions.append("action_is_read")
	if "action_is_read" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("action_is_read")
	if "pet_is_adopted" not in policy_mg.propositions:
		policy_mg.propositions.append("pet_is_adopted")
	if "pet_is_adopted" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("pet_is_adopted")
	src = "rule_4"
	policy_mg.variables.append(src)
	dst = rule_head
	if dst not in policy_mg.variables:
		policy_mg.variables.append(dst)
	policy_mg.edges.append(Edge({src}, {dst}, attributes=policy_mg.current_propositions))
	policy_mg.current_propositions = []

	rule_head = 'user_is_owner'
	if "data.user_attributes[input.user].title==\"owner\"" not in policy_mg.propositions:
		policy_mg.propositions.append("data.user_attributes[input.user].title==\"owner\"")
	if "data.user_attributes[input.user].title==\"owner\"" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("data.user_attributes[input.user].title==\"owner\"")
	src = "rule_5"
	policy_mg.variables.append(src)
	dst = rule_head
	if dst not in policy_mg.variables:
		policy_mg.variables.append(dst)
	policy_mg.edges.append(Edge({src}, {dst}, attributes=policy_mg.current_propositions))
	policy_mg.current_propositions = []

	rule_head = 'user_is_employee'
	if "data.user_attributes[input.user].title==\"employee\"" not in policy_mg.propositions:
		policy_mg.propositions.append("data.user_attributes[input.user].title==\"employee\"")
	if "data.user_attributes[input.user].title==\"employee\"" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("data.user_attributes[input.user].title==\"employee\"")
	src = "rule_6"
	policy_mg.variables.append(src)
	dst = rule_head
	if dst not in policy_mg.variables:
		policy_mg.variables.append(dst)
	policy_mg.edges.append(Edge({src}, {dst}, attributes=policy_mg.current_propositions))
	policy_mg.current_propositions = []

	rule_head = 'user_is_customer'
	if "data.user_attributes[input.user].title==\"customer\"" not in policy_mg.propositions:
		policy_mg.propositions.append("data.user_attributes[input.user].title==\"customer\"")
	if "data.user_attributes[input.user].title==\"customer\"" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("data.user_attributes[input.user].title==\"customer\"")
	src = "rule_7"
	policy_mg.variables.append(src)
	dst = rule_head
	if dst not in policy_mg.variables:
		policy_mg.variables.append(dst)
	policy_mg.edges.append(Edge({src}, {dst}, attributes=policy_mg.current_propositions))
	policy_mg.current_propositions = []

	rule_head = 'user_is_senior'
	if "data.user_attributes[input.user].tenure>8" not in policy_mg.propositions:
		policy_mg.propositions.append("data.user_attributes[input.user].tenure>8")
	if "data.user_attributes[input.user].tenure>8" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("data.user_attributes[input.user].tenure>8")
	src = "rule_8"
	policy_mg.variables.append(src)
	dst = rule_head
	if dst not in policy_mg.variables:
		policy_mg.variables.append(dst)
	policy_mg.edges.append(Edge({src}, {dst}, attributes=policy_mg.current_propositions))
	policy_mg.current_propositions = []

	rule_head = 'action_is_read'
	if "input.action==\"read\"" not in policy_mg.propositions:
		policy_mg.propositions.append("input.action==\"read\"")
	if "input.action==\"read\"" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("input.action==\"read\"")
	src = "rule_9"
	policy_mg.variables.append(src)
	dst = rule_head
	if dst not in policy_mg.variables:
		policy_mg.variables.append(dst)
	policy_mg.edges.append(Edge({src}, {dst}, attributes=policy_mg.current_propositions))
	policy_mg.current_propositions = []

	rule_head = 'action_is_update'
	if "input.action==\"update\"" not in policy_mg.propositions:
		policy_mg.propositions.append("input.action==\"update\"")
	if "input.action==\"update\"" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("input.action==\"update\"")
	src = "rule_10"
	policy_mg.variables.append(src)
	dst = rule_head
	if dst not in policy_mg.variables:
		policy_mg.variables.append(dst)
	policy_mg.edges.append(Edge({src}, {dst}, attributes=policy_mg.current_propositions))
	policy_mg.current_propositions = []

	rule_head = 'pet_is_adopted'
	if "data.pet_attributes[input.resource].adopted==true" not in policy_mg.propositions:
		policy_mg.propositions.append("data.pet_attributes[input.resource].adopted==true")
	if "data.pet_attributes[input.resource].adopted==true" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("data.pet_attributes[input.resource].adopted==true")
	src = "rule_11"
	policy_mg.variables.append(src)
	dst = rule_head
	if dst not in policy_mg.variables:
		policy_mg.variables.append(dst)
	policy_mg.edges.append(Edge({src}, {dst}, attributes=policy_mg.current_propositions))
	policy_mg.current_propositions = []

	return policy_mg
