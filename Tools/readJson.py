import json

json_file = r'D:\Jinson\WorkSpace\数据库没计测试数据\airports.json'
# json_file = r'D:\Jinson\WorkSpace\数据库没计测试数据\airports-1.json'
txt_file = r'D:\Jinson\WorkSpace\数据库没计测试数据\airports-1.txt'
in_file = open(json_file, encoding='utf-8')
json_dic = json.load(in_file)

out_file = open(txt_file, "w", encoding='utf-8')
# print(len(json_dic), json_dic)
# print(json_dic['ZYYY']['name'])

icaos = []

# for item in json_dic:
#     icaos.append(item)
# # print(icaos)

for item in json_dic:
    elevation = '' if json_dic[item]['elevation'] is None else json_dic[item]['elevation'] is None
    lat = '' if json_dic[item]['lat'] is None else json_dic[item]['lat'] is None
    lon = '' if json_dic[item]['lon'] is None else json_dic[item]['lon'] is None
    # item_str = json_dic[item]['icao'] + ',' + json_dic[item]['iata'] + ',' + json_dic[item]['name'] + ',' + json_dic[item]['city'] + ',' + json_dic[item]['state'] + ',' + json_dic[item]['country'] + ',' + str(json_dic[item]['elevation']) + ',' + str(json_dic[item]['lat']) + ',' + str(json_dic[item]['lon']) + ',' + json_dic[item]['tz'] + '\n'
    # item_str = json_dic[item]['icao'] + ',' + json_dic[item]['iata'] + ',' + json_dic[item]['name'] + ',' + json_dic[item]['city'] + ',' + json_dic[item]['state'] + ',' + json_dic[item]['country'] + ',' + json_dic[item]['elevation'] + ',' + str(json_dic[item]['lat']) + ',' + str(json_dic[item]['lon']) + ',' + json_dic[item]['tz'] + '\n'
    item_str = '%s%s%s' %(json_dic[item]['icao'],json_dic[item]['iata'],json_dic[item]['name'],json_dic[item]['city'],json_dic[item]['state'],json_dic[item]['country'],json_dic[item]['elevation'],json_dic[item]['lat'],json_dic[item]['lon'],json_dic[item]['tz'],'\n')
    print('==icao==', json_dic[item]['icao'])
    # item_str = json_dic[item]['icao'] + ',' + json_dic[item]['iata'] + ',' + json_dic[item]['name'] + ',' + json_dic[item]['city'] + ',' + json_dic[item]['state'] + ',' + json_dic[item]['country'] + ',' + elevation + ',' + lat + ',' + lon + ',' + json_dic[item]['tz'] + '\n'
    # item_str = json_dic[item]['icao'] + ',' + json_dic[item]['iata']
    out_file.write(item_str)

in_file.close()
out_file.close()

