import json
read = json.load(open('gen_res_val1.json','r',encoding="utf-8"))
for line in read:
    lines = read[line]['gen'][0]
    print(lines)
# print(read)