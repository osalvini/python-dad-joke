import requests
from colorama import init, Fore, Back

init()

headers = {"Accept": "application/json"}
response = requests.get('https://icanhazdadjoke.com/', headers=headers)

if response.status_code == 200:
    data = response.json()
    print(Back.BLUE + Fore.YELLOW + "\n\n"+data['joke']+"\n\n")
else:
    print(f"Request failed with status code: {response.status_code}")
    print("Response content:")
    print(response.text)