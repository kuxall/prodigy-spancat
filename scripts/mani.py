import json

output = {"text": ""}
with open(f"/home/kushal/Documents/spancat/files/158_WebSphere Portal Admin.jsonl") as f:
    for line in f:
        data = json.loads(line)
        output["text"] += data["text"] + " "

with open("/home/kushal/Documents/spancat/out/158.jsonl", "w") as f:
    json.dump(output, f)
    f.write("\n")
