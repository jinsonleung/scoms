"""
pymysql更新机场信息
"""
import pymysql
import json

conn = pymysql.connect(
    host="localhost",
    port=3306,
    database="scomsdb",
    user="root",
    password="China123",
    charset="utf8"
)

# 打开airport json文件
airport_json_file = r'D:\Jinson\WorkSpace\数据库没计测试数据\airports.json'
in_file = open(airport_json_file, encoding='utf-8')
airport_dic = json.load(in_file)

i = 1
cursor = conn.cursor()
# sql = "update airport set description = %s where iata_code = %s"
sql = "update airport set elevation = %s,longitude = %s,latitude = %s,time_zone = %s,utc = %s where icao_code = %s"
for icao_code in airport_dic:
    # if i < 5:
    if icao_code:
        print('==icao_code==', icao_code)
        params = [airport_dic[icao_code]['elevation'], airport_dic[icao_code]['lon'], airport_dic[icao_code]['lat'], airport_dic[icao_code]['tz'], '', icao_code]
        cursor.execute(sql, params)
        i = i + 1
    else:
        break
conn.commit()
cursor.close()
conn.close()
in_file.close()
print('==update airport end!==')

