import json
file_LJJ = "D:/WeChat/WeChat Files/wxid_4eoriey19h5n12/FileStorage/File/2024-03/Contry-20240310-JJL.txt"
file_echarts = "D:/WeChat/WeChat Files/wxid_4eoriey19h5n12/FileStorage/File/2024-03/map_JSON.txt"

country_LJJ = set()
with open(file_LJJ, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if len(line.split(" ")) <= 1:
            continue
        abbr = line.split(" ")[0]
        country_LJJ.add(line[len(abbr):].strip())

cnt = 0
unmatched_lst = []
echarts_countries = set()
echarts_country = json.load(open(file_echarts, 'r', encoding='utf-8'))
for country in echarts_country["features"]:
    name = country["properties"]["name"]
    echarts_countries.add(name)

for name in country_LJJ:
    if name in echarts_countries:
        cnt += 1
    else:
        unmatched_lst.append(name)

print("LJJ total countries", len(country_LJJ))
print("Echarts total countries", len(echarts_country["features"]))
print("Matched countries", cnt)

# print(country_map.keys())


dic = sorted(echarts_countries)
unmatched_lst.sort()


country_map = {}
with open(file_LJJ, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if len(line.split(" ")) <= 1:
            continue
        abbr = line.split(" ")[0]
        full_name = line[len(abbr):].strip()
        if full_name in unmatched_lst:
            continue
        country_map[abbr] = full_name

with open("country_map.json", "w") as f:
    json.dump(country_map, f, ensure_ascii=False, indent=4)

print(len(country_map.keys()))