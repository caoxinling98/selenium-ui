import requests
# import io,sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
# payload = {"loginId":"caoxinling1","password":"cxl123456.","orgId":16}
# response = requests.post("http://acv3.learn.it101.live/api/auth/login",payload)
# print(response.json())

# headers = {"ac-token":"fmf0uO2LsBl_zd8-hVGxF2gpydx9rKXC"}
# r = requests.get("http://acv3.learn.it101.live/api/courses/v3/trends",headers=headers)
# data = r.json()
# assert data["ok"] == True

r = requests.get("https://www.baidu.com/")
print(r.text)