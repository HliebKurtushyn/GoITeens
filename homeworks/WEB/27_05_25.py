import requests

url = "https://akabab.github.io/superhero-api/api/all.json"

try:
    response = requests.get(url)
    
    if response.status_code == 200:
        posts = response.json()
        
        for post in posts[:5]:
            print(f"Name: {post['name']}, Powerstats: {', '.join(f'{stat}: {value}' for stat, value in post['powerstats'].items())}")
            
    else:
        print(f"Помилка: {response.status_code}")
except Exception as e:
    print(f"Виникла помилка: {e}")