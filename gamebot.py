import requests

url = "https://tbot.xyz/api/setScore"
foruser = input("Please enter you unique URL: ")
score = int(input("Please enter score: "))
payload = f"data={foruser}&score={score}"
headers = {
  'Connection': 'keep-alive',
  'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
  'Content-Type': 'text/plain;charset=UTF-8',
  'Accept': '*/*',
  'Origin': 'https://tbot.xyz',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-Mode': 'cors',
  'Referer': 'https://tbot.xyz/lumber/',
  'Accept-Encoding': 'gzip, deflate, br',
  'Accept-Language': 'en-US,en;q=0.9'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
