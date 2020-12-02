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
	if "user_is_admin" not in policy_mg.propositions:
		policy_mg.propositions.append("user_is_admin")
	if "user_is_admin" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("user_is_admin")
	src = "rule_1"
	policy_mg.variables.append(src)
	dst = rule_head
	if dst not in policy_mg.variables:
		policy_mg.variables.append(dst)
	policy_mg.edges.append(Edge({src}, {dst}, attributes=policy_mg.current_propositions))
	policy_mg.current_propositions = []

	rule_head = 'allow'
	if "somegrant" not in policy_mg.propositions:
		policy_mg.propositions.append("somegrant")
	if "somegrant" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("somegrant")
	if "user_is_granted[grant]" not in policy_mg.propositions:
		policy_mg.propositions.append("user_is_granted[grant]")
	if "user_is_granted[grant]" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("user_is_granted[grant]")
	if "input.action==grant.action" not in policy_mg.propositions:
		policy_mg.propositions.append("input.action==grant.action")
	if "input.action==grant.action" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("input.action==grant.action")
	if "input.type==grant.type" not in policy_mg.propositions:
		policy_mg.propositions.append("input.type==grant.type")
	if "input.type==grant.type" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("input.type==grant.type")
	src = "rule_2"
	policy_mg.variables.append(src)
	dst = rule_head
	if dst not in policy_mg.variables:
		policy_mg.variables.append(dst)
	policy_mg.edges.append(Edge({src}, {dst}, attributes=policy_mg.current_propositions))
	policy_mg.current_propositions = []

	rule_head = 'user_is_admin'
	if "somei" not in policy_mg.propositions:
		policy_mg.propositions.append("somei")
	if "somei" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("somei")
	if "data.user_roles[input.user][i]==\"admin\"" not in policy_mg.propositions:
		policy_mg.propositions.append("data.user_roles[input.user][i]==\"admin\"")
	if "data.user_roles[input.user][i]==\"admin\"" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("data.user_roles[input.user][i]==\"admin\"")
	src = "rule_3"
	policy_mg.variables.append(src)
	dst = rule_head
	if dst not in policy_mg.variables:
		policy_mg.variables.append(dst)
	policy_mg.edges.append(Edge({src}, {dst}, attributes=policy_mg.current_propositions))
	policy_mg.current_propositions = []

	rule_head = 'user_is_granted'
	if "somei,j" not in policy_mg.propositions:
		policy_mg.propositions.append("somei,j")
	if "somei,j" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("somei,j")
	if "role:=data.user_roles[input.user][i]" not in policy_mg.propositions:
		policy_mg.propositions.append("role:=data.user_roles[input.user][i]")
	if "role:=data.user_roles[input.user][i]" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("role:=data.user_roles[input.user][i]")
	if "grant:=data.role_grants[role][j]" not in policy_mg.propositions:
		policy_mg.propositions.append("grant:=data.role_grants[role][j]")
	if "grant:=data.role_grants[role][j]" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("grant:=data.role_grants[role][j]")
	src = "rule_4"
	policy_mg.variables.append(src)
	dst = rule_head
	if dst not in policy_mg.variables:
		policy_mg.variables.append(dst)
	policy_mg.edges.append(Edge({src}, {dst}, attributes=policy_mg.current_propositions))
	policy_mg.current_propositions = []

	return policy_mg
