import requests

url = "http://127.0.0.1:3000/claculate/claculate.html?serverWindowId=02da879d-484c-4d13-9c6b-f00901340d52"
response = requests.get(url)
html_content = response.text
button = html_content.find('button')
print(button)
a = int(input(""))
b = int(input(""))
if button == '+':
    print(a+b)