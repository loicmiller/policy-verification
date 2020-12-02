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

	rule_head = 'user_name'
	if "[_,encoded]:=split(http_request.headers.authorization,\" \")" not in policy_mg.propositions:
		policy_mg.propositions.append("[_,encoded]:=split(http_request.headers.authorization,\" \")")
	if "[_,encoded]:=split(http_request.headers.authorization,\" \")" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("[_,encoded]:=split(http_request.headers.authorization,\" \")")
	if "[parsed,_]:=split(base64url.decode(encoded),\":\")" not in policy_mg.propositions:
		policy_mg.propositions.append("[parsed,_]:=split(base64url.decode(encoded),\":\")")
	if "[parsed,_]:=split(base64url.decode(encoded),\":\")" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("[parsed,_]:=split(base64url.decode(encoded),\":\")")
	src = "rule_1"
	policy_mg.variables.append(src)
	dst = rule_head
	if dst not in policy_mg.variables:
		policy_mg.variables.append(dst)
	policy_mg.edges.append(Edge({src}, {dst}, attributes=policy_mg.current_propositions))
	policy_mg.current_propositions = []

	rule_head = 'user_roles'
	src = "rule_2"
	policy_mg.variables.append(src)
	dst = rule_head
	if dst not in policy_mg.variables:
		policy_mg.variables.append(dst)
	policy_mg.edges.append(Edge({src}, {dst}, attributes=policy_mg.current_propositions))
	policy_mg.current_propositions = []

	rule_head = 'role_permissions'
	src = "rule_3"
	policy_mg.variables.append(src)
	dst = rule_head
	if dst not in policy_mg.variables:
		policy_mg.variables.append(dst)
	policy_mg.edges.append(Edge({src}, {dst}, attributes=policy_mg.current_propositions))
	policy_mg.current_propositions = []

	rule_head = 'rbac_logic'
	if "roles:=user_roles[user_name]" not in policy_mg.propositions:
		policy_mg.propositions.append("roles:=user_roles[user_name]")
	if "roles:=user_roles[user_name]" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("roles:=user_roles[user_name]")
	if "r:=roles[_]" not in policy_mg.propositions:
		policy_mg.propositions.append("r:=roles[_]")
	if "r:=roles[_]" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("r:=roles[_]")
	if "permissions:=role_permissions[r]" not in policy_mg.propositions:
		policy_mg.propositions.append("permissions:=role_permissions[r]")
	if "permissions:=role_permissions[r]" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("permissions:=role_permissions[r]")
	if "p:=permissions[_]" not in policy_mg.propositions:
		policy_mg.propositions.append("p:=permissions[_]")
	if "p:=permissions[_]" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("p:=permissions[_]")
	if "p=={\"method\":http_request.method,\"path\":http_request.path}" not in policy_mg.propositions:
		policy_mg.propositions.append("p=={\"method\":http_request.method,\"path\":http_request.path}")
	if "p=={\"method\":http_request.method,\"path\":http_request.path}" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("p=={\"method\":http_request.method,\"path\":http_request.path}")
	src = "rule_4"
	policy_mg.variables.append(src)
	dst = rule_head
	if dst not in policy_mg.variables:
		policy_mg.variables.append(dst)
	policy_mg.edges.append(Edge({src}, {dst}, attributes=policy_mg.current_propositions))
	policy_mg.current_propositions = []

	rule_head = 'user_attributes'
	src = "rule_5"
	policy_mg.variables.append(src)
	dst = rule_head
	if dst not in policy_mg.variables:
		policy_mg.variables.append(dst)
	policy_mg.edges.append(Edge({src}, {dst}, attributes=policy_mg.current_propositions))
	policy_mg.current_propositions = []

	rule_head = 'allow'
	if "user_name==\"owner\"" not in policy_mg.propositions:
		policy_mg.propositions.append("user_name==\"owner\"")
	if "user_name==\"owner\"" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("user_name==\"owner\"")
	if "rbac_logic" not in policy_mg.propositions:
		policy_mg.propositions.append("rbac_logic")
	if "rbac_logic" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("rbac_logic")
	src = "rule_6"
	policy_mg.variables.append(src)
	dst = rule_head
	if dst not in policy_mg.variables:
		policy_mg.variables.append(dst)
	policy_mg.edges.append(Edge({src}, {dst}, attributes=policy_mg.current_propositions))
	policy_mg.current_propositions = []

	rule_head = 'allow'
	if "user_name==\"vfx-1\"" not in policy_mg.propositions:
		policy_mg.propositions.append("user_name==\"vfx-1\"")
	if "user_name==\"vfx-1\"" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("user_name==\"vfx-1\"")
	if "rbac_logic" not in policy_mg.propositions:
		policy_mg.propositions.append("rbac_logic")
	if "rbac_logic" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("rbac_logic")
	src = "rule_7"
	policy_mg.variables.append(src)
	dst = rule_head
	if dst not in policy_mg.variables:
		policy_mg.variables.append(dst)
	policy_mg.edges.append(Edge({src}, {dst}, attributes=policy_mg.current_propositions))
	policy_mg.current_propositions = []

	rule_head = 'allow'
	if "user_name==\"vfx-2\"" not in policy_mg.propositions:
		policy_mg.propositions.append("user_name==\"vfx-2\"")
	if "user_name==\"vfx-2\"" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("user_name==\"vfx-2\"")
	if "rbac_logic" not in policy_mg.propositions:
		policy_mg.propositions.append("rbac_logic")
	if "rbac_logic" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("rbac_logic")
	if "user:=user_attributes[user_name]" not in policy_mg.propositions:
		policy_mg.propositions.append("user:=user_attributes[user_name]")
	if "user:=user_attributes[user_name]" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("user:=user_attributes[user_name]")
	if "user.tenure>10" not in policy_mg.propositions:
		policy_mg.propositions.append("user.tenure>10")
	if "user.tenure>10" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("user.tenure>10")
	src = "rule_8"
	policy_mg.variables.append(src)
	dst = rule_head
	if dst not in policy_mg.variables:
		policy_mg.variables.append(dst)
	policy_mg.edges.append(Edge({src}, {dst}, attributes=policy_mg.current_propositions))
	policy_mg.current_propositions = []

	rule_head = 'allow'
	if "user_name==\"vfx-2\"" not in policy_mg.propositions:
		policy_mg.propositions.append("user_name==\"vfx-2\"")
	if "user_name==\"vfx-2\"" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("user_name==\"vfx-2\"")
	if "rbac_logic" not in policy_mg.propositions:
		policy_mg.propositions.append("rbac_logic")
	if "rbac_logic" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("rbac_logic")
	if "current_time:=time.clock([time.now_ns(),\"Europe/Paris\"])" not in policy_mg.propositions:
		policy_mg.propositions.append("current_time:=time.clock([time.now_ns(),\"Europe/Paris\"])")
	if "current_time:=time.clock([time.now_ns(),\"Europe/Paris\"])" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("current_time:=time.clock([time.now_ns(),\"Europe/Paris\"])")
	if "to_number(current_time[0])>=8" not in policy_mg.propositions:
		policy_mg.propositions.append("to_number(current_time[0])>=8")
	if "to_number(current_time[0])>=8" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("to_number(current_time[0])>=8")
	if "to_number(current_time[0])<=17" not in policy_mg.propositions:
		policy_mg.propositions.append("to_number(current_time[0])<=17")
	if "to_number(current_time[0])<=17" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("to_number(current_time[0])<=17")
	src = "rule_9"
	policy_mg.variables.append(src)
	dst = rule_head
	if dst not in policy_mg.variables:
		policy_mg.variables.append(dst)
	policy_mg.edges.append(Edge({src}, {dst}, attributes=policy_mg.current_propositions))
	policy_mg.current_propositions = []

	rule_head = 'allow'
	if "user_name==\"vfx-3\"" not in policy_mg.propositions:
		policy_mg.propositions.append("user_name==\"vfx-3\"")
	if "user_name==\"vfx-3\"" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("user_name==\"vfx-3\"")
	if "rbac_logic" not in policy_mg.propositions:
		policy_mg.propositions.append("rbac_logic")
	if "rbac_logic" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("rbac_logic")
	if "user:=user_attributes[user_name]" not in policy_mg.propositions:
		policy_mg.propositions.append("user:=user_attributes[user_name]")
	if "user:=user_attributes[user_name]" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("user:=user_attributes[user_name]")
	if "user.tenure>10" not in policy_mg.propositions:
		policy_mg.propositions.append("user.tenure>10")
	if "user.tenure>10" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("user.tenure>10")
	src = "rule_10"
	policy_mg.variables.append(src)
	dst = rule_head
	if dst not in policy_mg.variables:
		policy_mg.variables.append(dst)
	policy_mg.edges.append(Edge({src}, {dst}, attributes=policy_mg.current_propositions))
	policy_mg.current_propositions = []

	rule_head = 'allow'
	if "user_name==\"vfx-3\"" not in policy_mg.propositions:
		policy_mg.propositions.append("user_name==\"vfx-3\"")
	if "user_name==\"vfx-3\"" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("user_name==\"vfx-3\"")
	if "rbac_logic" not in policy_mg.propositions:
		policy_mg.propositions.append("rbac_logic")
	if "rbac_logic" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("rbac_logic")
	if "current_time:=time.clock([time.now_ns(),\"Europe/Paris\"])" not in policy_mg.propositions:
		policy_mg.propositions.append("current_time:=time.clock([time.now_ns(),\"Europe/Paris\"])")
	if "current_time:=time.clock([time.now_ns(),\"Europe/Paris\"])" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("current_time:=time.clock([time.now_ns(),\"Europe/Paris\"])")
	if "to_number(current_time[0])>=8" not in policy_mg.propositions:
		policy_mg.propositions.append("to_number(current_time[0])>=8")
	if "to_number(current_time[0])>=8" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("to_number(current_time[0])>=8")
	if "to_number(current_time[0])<=17" not in policy_mg.propositions:
		policy_mg.propositions.append("to_number(current_time[0])<=17")
	if "to_number(current_time[0])<=17" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("to_number(current_time[0])<=17")
	src = "rule_11"
	policy_mg.variables.append(src)
	dst = rule_head
	if dst not in policy_mg.variables:
		policy_mg.variables.append(dst)
	policy_mg.edges.append(Edge({src}, {dst}, attributes=policy_mg.current_propositions))
	policy_mg.current_propositions = []

	rule_head = 'allow'
	if "user_name==\"color\"" not in policy_mg.propositions:
		policy_mg.propositions.append("user_name==\"color\"")
	if "user_name==\"color\"" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("user_name==\"color\"")
	if "rbac_logic" not in policy_mg.propositions:
		policy_mg.propositions.append("rbac_logic")
	if "rbac_logic" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("rbac_logic")
	if "current_time:=time.clock([time.now_ns(),\"Europe/Paris\"])" not in policy_mg.propositions:
		policy_mg.propositions.append("current_time:=time.clock([time.now_ns(),\"Europe/Paris\"])")
	if "current_time:=time.clock([time.now_ns(),\"Europe/Paris\"])" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("current_time:=time.clock([time.now_ns(),\"Europe/Paris\"])")
	if "to_number(current_time[0])<=8" not in policy_mg.propositions:
		policy_mg.propositions.append("to_number(current_time[0])<=8")
	if "to_number(current_time[0])<=8" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("to_number(current_time[0])<=8")
	if "to_number(current_time[0])>=17" not in policy_mg.propositions:
		policy_mg.propositions.append("to_number(current_time[0])>=17")
	if "to_number(current_time[0])>=17" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("to_number(current_time[0])>=17")
	src = "rule_12"
	policy_mg.variables.append(src)
	dst = rule_head
	if dst not in policy_mg.variables:
		policy_mg.variables.append(dst)
	policy_mg.edges.append(Edge({src}, {dst}, attributes=policy_mg.current_propositions))
	policy_mg.current_propositions = []

	rule_head = 'allow'
	if "user_name==\"sound\"" not in policy_mg.propositions:
		policy_mg.propositions.append("user_name==\"sound\"")
	if "user_name==\"sound\"" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("user_name==\"sound\"")
	if "rbac_logic" not in policy_mg.propositions:
		policy_mg.propositions.append("rbac_logic")
	if "rbac_logic" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("rbac_logic")
	if "current_time:=time.clock([time.now_ns(),\"Europe/Paris\"])" not in policy_mg.propositions:
		policy_mg.propositions.append("current_time:=time.clock([time.now_ns(),\"Europe/Paris\"])")
	if "current_time:=time.clock([time.now_ns(),\"Europe/Paris\"])" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("current_time:=time.clock([time.now_ns(),\"Europe/Paris\"])")
	if "to_number(current_time[0])<=8" not in policy_mg.propositions:
		policy_mg.propositions.append("to_number(current_time[0])<=8")
	if "to_number(current_time[0])<=8" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("to_number(current_time[0])<=8")
	if "to_number(current_time[0])>=17" not in policy_mg.propositions:
		policy_mg.propositions.append("to_number(current_time[0])>=17")
	if "to_number(current_time[0])>=17" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("to_number(current_time[0])>=17")
	src = "rule_13"
	policy_mg.variables.append(src)
	dst = rule_head
	if dst not in policy_mg.variables:
		policy_mg.variables.append(dst)
	policy_mg.edges.append(Edge({src}, {dst}, attributes=policy_mg.current_propositions))
	policy_mg.current_propositions = []

	rule_head = 'allow'
	if "user_name==\"hdr\"" not in policy_mg.propositions:
		policy_mg.propositions.append("user_name==\"hdr\"")
	if "user_name==\"hdr\"" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("user_name==\"hdr\"")
	if "rbac_logic" not in policy_mg.propositions:
		policy_mg.propositions.append("rbac_logic")
	if "rbac_logic" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("rbac_logic")
	if "current_time:=time.clock([time.now_ns(),\"Europe/Paris\"])" not in policy_mg.propositions:
		policy_mg.propositions.append("current_time:=time.clock([time.now_ns(),\"Europe/Paris\"])")
	if "current_time:=time.clock([time.now_ns(),\"Europe/Paris\"])" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("current_time:=time.clock([time.now_ns(),\"Europe/Paris\"])")
	if "to_number(current_time[0])>=8" not in policy_mg.propositions:
		policy_mg.propositions.append("to_number(current_time[0])>=8")
	if "to_number(current_time[0])>=8" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("to_number(current_time[0])>=8")
	if "to_number(current_time[0])<=17" not in policy_mg.propositions:
		policy_mg.propositions.append("to_number(current_time[0])<=17")
	if "to_number(current_time[0])<=17" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("to_number(current_time[0])<=17")
	src = "rule_14"
	policy_mg.variables.append(src)
	dst = rule_head
	if dst not in policy_mg.variables:
		policy_mg.variables.append(dst)
	policy_mg.edges.append(Edge({src}, {dst}, attributes=policy_mg.current_propositions))
	policy_mg.current_propositions = []

	return policy_mg
