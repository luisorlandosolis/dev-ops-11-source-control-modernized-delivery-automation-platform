#!/usr/bin/env python3

import yaml
import subprocess
import json

with open("/home/orlando/ansible/monitoring.yml") as f:
    config = yaml.safe_load(f)

results = {}

for host in config["infrastructure_targets"]:
    name = host["name"]
    ip = host["ip"]

    result = subprocess.run(
        ["ping", "-c", "1", "-W", "2", ip],
        capture_output=True
    )

    results[name] = "UP" if result.returncode == 0 else "DOWN"

print(json.dumps(results, indent=2))
