import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

res.status_code
len(res.text[:500])

playFile = open('RomeoandJuliet.txt', 'wb')

for chunk in res.iter_content(100000):
  playFile.write(chunk)

playFile.close()
