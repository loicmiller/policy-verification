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

	rule_head = 'user_attributes'
	src = "rule_2"
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
	if "http_request.method==\"POST\"" not in policy_mg.propositions:
		policy_mg.propositions.append("http_request.method==\"POST\"")
	if "http_request.method==\"POST\"" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("http_request.method==\"POST\"")
	if "http_request.path==\"/api/vfx\"" not in policy_mg.propositions:
		policy_mg.propositions.append("http_request.path==\"/api/vfx\"")
	if "http_request.path==\"/api/vfx\"" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("http_request.path==\"/api/vfx\"")
	src = "rule_3"
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
	if "http_request.method==\"POST\"" not in policy_mg.propositions:
		policy_mg.propositions.append("http_request.method==\"POST\"")
	if "http_request.method==\"POST\"" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("http_request.method==\"POST\"")
	if "http_request.path==\"/api/vfx\"" not in policy_mg.propositions:
		policy_mg.propositions.append("http_request.path==\"/api/vfx\"")
	if "http_request.path==\"/api/vfx\"" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("http_request.path==\"/api/vfx\"")
	src = "rule_4"
	policy_mg.variables.append(src)
	dst = rule_head
	if dst not in policy_mg.variables:
		policy_mg.variables.append(dst)
	policy_mg.edges.append(Edge({src}, {dst}, attributes=policy_mg.current_propositions))
	policy_mg.current_propositions = []

	rule_head = 'allow'
	if "http_request.method==\"POST\"" not in policy_mg.propositions:
		policy_mg.propositions.append("http_request.method==\"POST\"")
	if "http_request.method==\"POST\"" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("http_request.method==\"POST\"")
	if "user:=user_attributes[user_name]" not in policy_mg.propositions:
		policy_mg.propositions.append("user:=user_attributes[user_name]")
	if "user:=user_attributes[user_name]" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("user:=user_attributes[user_name]")
	if "user.tenure>10" not in policy_mg.propositions:
		policy_mg.propositions.append("user.tenure>10")
	if "user.tenure>10" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("user.tenure>10")
	if "user_name==\"vfx\"" not in policy_mg.propositions:
		policy_mg.propositions.append("user_name==\"vfx\"")
	if "user_name==\"vfx\"" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("user_name==\"vfx\"")
	if "http_request.path==\"/api/color\"" not in policy_mg.propositions:
		policy_mg.propositions.append("http_request.path==\"/api/color\"")
	if "http_request.path==\"/api/color\"" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("http_request.path==\"/api/color\"")
	if "http_request.path==\"/api/sound\"" not in policy_mg.propositions:
		policy_mg.propositions.append("http_request.path==\"/api/sound\"")
	if "http_request.path==\"/api/sound\"" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("http_request.path==\"/api/sound\"")
	src = "rule_5"
	policy_mg.variables.append(src)
	dst = rule_head
	if dst not in policy_mg.variables:
		policy_mg.variables.append(dst)
	policy_mg.edges.append(Edge({src}, {dst}, attributes=policy_mg.current_propositions))
	policy_mg.current_propositions = []

	rule_head = 'allow'
	if "http_request.method==\"POST\"" not in policy_mg.propositions:
		policy_mg.propositions.append("http_request.method==\"POST\"")
	if "http_request.method==\"POST\"" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("http_request.method==\"POST\"")
	if "current_time:=time.clock([time.now_ns(),\"Europe/Paris\"])" not in policy_mg.propositions:
		policy_mg.propositions.append("current_time:=time.clock([time.now_ns(),\"Europe/Paris\"])")
	if "current_time:=time.clock([time.now_ns(),\"Europe/Paris\"])" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("current_time:=time.clock([time.now_ns(),\"Europe/Paris\"])")
	if "to_number(current_time[0])<17" not in policy_mg.propositions:
		policy_mg.propositions.append("to_number(current_time[0])<17")
	if "to_number(current_time[0])<17" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("to_number(current_time[0])<17")
	if "to_number(current_time[0])>8" not in policy_mg.propositions:
		policy_mg.propositions.append("to_number(current_time[0])>8")
	if "to_number(current_time[0])>8" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("to_number(current_time[0])>8")
	if "user_name==\"vfx\"" not in policy_mg.propositions:
		policy_mg.propositions.append("user_name==\"vfx\"")
	if "user_name==\"vfx\"" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("user_name==\"vfx\"")
	if "http_request.path==\"/api/color\"" not in policy_mg.propositions:
		policy_mg.propositions.append("http_request.path==\"/api/color\"")
	if "http_request.path==\"/api/color\"" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("http_request.path==\"/api/color\"")
	if "http_request.path==\"/api/sound\"" not in policy_mg.propositions:
		policy_mg.propositions.append("http_request.path==\"/api/sound\"")
	if "http_request.path==\"/api/sound\"" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("http_request.path==\"/api/sound\"")
	src = "rule_6"
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
	if "http_request.method==\"POST\"" not in policy_mg.propositions:
		policy_mg.propositions.append("http_request.method==\"POST\"")
	if "http_request.method==\"POST\"" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("http_request.method==\"POST\"")
	if "current_time:=time.clock([time.now_ns(),\"Europe/Paris\"])" not in policy_mg.propositions:
		policy_mg.propositions.append("current_time:=time.clock([time.now_ns(),\"Europe/Paris\"])")
	if "current_time:=time.clock([time.now_ns(),\"Europe/Paris\"])" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("current_time:=time.clock([time.now_ns(),\"Europe/Paris\"])")
	if "to_number(current_time[0])>17" not in policy_mg.propositions:
		policy_mg.propositions.append("to_number(current_time[0])>17")
	if "to_number(current_time[0])>17" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("to_number(current_time[0])>17")
	if "http_request.path==\"/api/hdr\"" not in policy_mg.propositions:
		policy_mg.propositions.append("http_request.path==\"/api/hdr\"")
	if "http_request.path==\"/api/hdr\"" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("http_request.path==\"/api/hdr\"")
	src = "rule_7"
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
	if "http_request.method==\"POST\"" not in policy_mg.propositions:
		policy_mg.propositions.append("http_request.method==\"POST\"")
	if "http_request.method==\"POST\"" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("http_request.method==\"POST\"")
	if "current_time:=time.clock([time.now_ns(),\"Europe/Paris\"])" not in policy_mg.propositions:
		policy_mg.propositions.append("current_time:=time.clock([time.now_ns(),\"Europe/Paris\"])")
	if "current_time:=time.clock([time.now_ns(),\"Europe/Paris\"])" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("current_time:=time.clock([time.now_ns(),\"Europe/Paris\"])")
	if "to_number(current_time[0])<8" not in policy_mg.propositions:
		policy_mg.propositions.append("to_number(current_time[0])<8")
	if "to_number(current_time[0])<8" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("to_number(current_time[0])<8")
	if "http_request.path==\"/api/hdr\"" not in policy_mg.propositions:
		policy_mg.propositions.append("http_request.path==\"/api/hdr\"")
	if "http_request.path==\"/api/hdr\"" not in policy_mg.current_propositions:
		policy_mg.current_propositions.append("http_request.path==\"/api/hdr\"")
	src = "rule_8"
	policy_mg.variables.append(src)
	dst = rule_head
	if dst not in policy_mg.variables:
		policy_mg.variables.append(dst)
	policy_mg.edges.append(Edge({src}, {dst}, attributes=policy_mg.current_propositions))
	policy_mg.current_propositions = []

	return policy_mg
