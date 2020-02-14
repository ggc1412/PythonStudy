import requests
url =  'https://www.ppomppu.co.kr/zboard/login_check.php?s_url=%2F'
data = {
    'user_id': 'ggc',
    'password' : 'soros!'
}
resp = requests.post(url, data=data)
print(resp.text)
