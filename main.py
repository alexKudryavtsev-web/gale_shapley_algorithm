import json
from abit import Abit

abit_db = ""
with open("./db/abit.json", mode="r", encoding="utf-8") as f:
    abit_db = f.read()

abit_db = json.loads(abit_db)

dir_db = ""
with open("./db/direction.json", mode="r", encoding="utf-8") as f:
    dir_db = f.read()

dir_db = json.loads(dir_db)

list_abit = [Abit(key, abit_db[key]["dirs"], abit_db[key]["exams"]) for key in abit_db]
enrolled = {key: [] for key in dir_db}

def work_is_complete(list_abit):
    for abit in list_abit:
        if len(abit.dirs) != 0:
            return False
    return True

while not work_is_complete(list_abit):
    empty_abit = []
    while len(list_abit) != 0:
        new_abit = list_abit.pop()
        if len(new_abit.dirs) != 0:
            enrolled[new_abit.enter()].append(new_abit)
        else:
            empty_abit.append(new_abit)

    for dir in enrolled:
        amount = dir_db[dir]["amount"]
        comb = dir_db[dir]["exams"]
        if len(enrolled[dir]) > amount:
            enrolled[dir] = sorted(enrolled[dir], key=lambda abit: abit.calc(comb), reverse=True)
            list_abit.extend(enrolled[dir][amount:])
            enrolled[dir] = enrolled[dir][:amount]
    list_abit.extend(empty_abit)

res = {}

res["Не поступили:"] = []
for a in list_abit:
    res["Не поступили:"].append(a.id)

for e in enrolled:
    res[e] = []
    for a in enrolled[e]:
        res[e].append(a.id)

res = json.dumps(res, ensure_ascii=False, indent=4)
print(res)
with open("./db/total.json", mode="w", encoding="utf-8") as f:
    f.write(res)