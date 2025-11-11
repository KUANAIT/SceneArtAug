import requests

url = "https://arbitrable-hermine-araneiform.ngrok-free.dev/enhance-image"
files = {'image': open('1.png', 'rb')}
data = {'label': 'messy'}

response = requests.post(url, files=files, data=data)
with open("enhanced.png", "wb") as f:
    f.write(response.content)