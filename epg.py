import requests
import json

def get_epg(channel, date):
  url = "http://epg.112114.xyz/?ch={}&date={}".format(channel, date)
  response = requests.get(url)
  if response.status_code == 200:
    data = json.loads(response.content)
    return data
  else:
    return None

def main():
  channel = input("请输入频道名称：")
  date = input("请输入日期：")
  epg = get_epg(channel, date)
  if epg:
    for program in epg:
      print("时间：", program["time"])
      print("节目名称：", program["name"])
      print("简介：", program["desc"])
      print()
  else:
    print("获取节目单失败")

if __name__ == "__main__":
  main()
