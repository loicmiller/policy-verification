package istio.authz
import input.attributes.request.http as http_request

default allow = false

user_name = parsed {
  [_, encoded] := split(http_request.headers.authorization, " ")
  [parsed, _] := split(base64url.decode(encoded), ":")
}

user_attributes = {
  "owner": {"tenure": 8},
  "vfx-1": {"tenure": 3},
  "vfx-2": {"tenure": 12},
  "vfx-3": {"tenure": 7},
  "color": {"tenure": 3},
  "sound": {"tenure": 4},
  "hdr": {"tenure": 5},
}

allow {
  user_name == "owner"
  http_request.method == "POST"
  http_request.path == "/api/vfx"
}

allow {
  user_name == "owner"
  http_request.method == "POST"
  http_request.path == "/api/vfx"
}

allow {
  http_request.method == "POST"
  user:=user_attributes[user_name]
  user.tenure > 10
  user_name == "vfx"
  http_request.path == "/api/color"
  http_request.path == "/api/sound"
}

allow {
  http_request.method == "POST"
  current_time := time.clock([time.now_ns(), "Europe/Paris"])
  to_number(current_time[0]) < 17
  to_number(current_time[0]) > 8
  user_name == "vfx"
  http_request.path == "/api/color"
  http_request.path == "/api/sound"
}

allow {
  user_name == "color"
  http_request.method == "POST"
  current_time := time.clock([time.now_ns(), "Europe/Paris"])
  to_number(current_time[0]) > 17
  http_request.path == "/api/hdr"
}

allow {
  user_name == "color"
  http_request.method == "POST"
  current_time := time.clock([time.now_ns(), "Europe/Paris"])
  to_number(current_time[0]) < 8
  http_request.path == "/api/hdr"
}

