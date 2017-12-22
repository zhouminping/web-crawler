import requests
from bs4 import BeautifulSoup
import time

cookies = {}

raw_cookies = "lianjia_uuid=711ccdda-8bb5-c238-f744-0601d44b3eef; select_city=310000; cityCode=sh; _ga=GA1.2.406704364.1513676597; ubt_load_interval_b=1513682531391; gr_user_id=9e098646-ede1-4049-b484-5c93ae9a1274; ubta=3357473675.179186095.1513676598420.1513682528326.1513682532333.18; ubtc=3357473675.179186095.1513682532333.24638E4D18A0E61B6365A17FA4D0E108; ubtd=18; __xsptplus696=696.2.1513681947.1513682531.12%234%7C%7C%7C%7C%7C%23%23kO6lFKOBHo1u13-ebjaEivFn6tBUzVO_%23; ubt_load_interval_c=1513682531391; _gat=1; _gat_u=1; gr_session_id_970bc0baee7301fa=2184222b-5e07-47f6-a8d0-a6566eec518c; gr_cs1_2184222b-5e07-47f6-a8d0-a6566eec518c=userid%3A2000000012619524; lianjia_ssid=761678e7-142e-6da8-68c8-6295a4e9ee7a; ubtb=3357473675.179186095.1513682532333.24638E4D18A0E61B6365A17FA4D0E108; lianjia_token=2.004d423eb43419dc5c5cef1785fb711f9e; __xsptplusUT_696=1"

for line in raw_cookies.split(";"):
	key, value = line.split('=', 1)
	cookies[key] = value

session_requests = requests.Session()



# login_url = "http://passport.lianjia.com/cas/login?service=http%3A%2F%2Fuser.sh.lianjia.com%2Ffavor%2Fhouse"

# response = session_requests.get(login_url)
# bsObj = BeautifulSoup(response.content, "lxml")
# lt_value = bsObj.find("input", {"name": "lt"}).get("value")
# execution = bsObj.find("input", {"name": "execution"}).get("value")
# # print(lt_value)
# # print(execution)

# value = {
# 	"username": "13361819695",
# 	"password": "qazwsx123456",
# 	"lt": lt_value,
# 	"execution": execution,
# 	"_eventId": "submit"
# }



# result = session_requests.post(login_url, data=value)
# time.sleep(5000)
# result = session_requests.post(login_url, data=value)
# time.sleep(5000)
# result = session_requests.post(login_url, data=value)
# time.sleep(5000)
# result = session_requests.post(login_url, data=value)
# time.sleep(5000)
# result = session_requests.get(login_url)

# bsObj_result = BeautifulSoup(result.content, "lxml")
# print(bsObj_result)

# input = bsObj.findAll("input")
# print(input)

url = "http://user.sh.lianjia.com/favor/house"

result = session_requests.get(url, cookies=cookies)
result = session_requests.get(url, cookies=cookies)
bsObj = BeautifulSoup(result.content, "lxml")

house_list = bsObj.find("div", {"id": "allList"})

print(house_list)

# favorite_url = "http://sh.lianjia.com/ershoufang/addMyFavorHouse.json"
# data = {
# 	"houseSellId": "4881243",
# 	"id": 0,
# 	"userId": 2000000012619524
# }
# session_requests.get(favorite_url, data=data)

# response = session_requests.get(url, cookies=cookies)
# bsObj = BeautifulSoup(response.content, "lxml")

# house_list = bsObj.find("div", {"id": "allList"})

# print(house_list)









