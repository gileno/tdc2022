import urllib.request
import re
url = 'https://www.melhorcambio.com/dolar-hoje'
headers = {
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/5'
}
req = urllib.request.Request(url, headers=headers)

with urllib.request.urlopen(req) as response:
	html = response.read().decode('utf-8')
preco = re.findall(r'<input type="hidden" value="(.*)" id="taxa-comercial">', html)[0]
print(preco)

