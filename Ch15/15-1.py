import json
with open("questions_and_answers.json", "r", encoding = "utf8") as f:
    contents = f.read()
    json_ex = json.loads(contents)

print(json_ex["quiz"]["sport"]["q1"]["question"] + "\n")

options = json_ex["quiz"]["sport"]["q1"]["options"]
for i in range(len(options)):
    print(str(i) +". "+options[i])

print("\n" "answer " + json_ex["quiz"]["sport"]["q1"]["answer"] )
