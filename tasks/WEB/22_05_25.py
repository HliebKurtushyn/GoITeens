import requests

# 1
# # URL для API-запиту
# url = "https://api.agify.io"

# try:
#     # Виконання GET-запиту
#     response = requests.get(url, params={"name": "Gleb"})
    
#     # Перевірка статусу відповіді
#     if response.status_code == 200:
#         # Перетворення відповіді в JSON
#         posts = response.json()
        
#         # Виведення перших 5 записів
#         print(f"Count: {posts["count"]}, Name: {posts["name"]}, Age: {posts["age"]}")
#     else:
#         print(f"Помилка: {response.status_code}")
# except Exception as e:
#     print(f"Виникла помилка: {e}")

# 2
# url = "https://jsonplaceholder.typicode.com/posts"

# try:
#     # Виконання GET-запиту
#     response = requests.post(url, data={"name": "gleb", "email": "email@email.com", "message": "Message fd gergerg"})
    
#     # Перевірка статусу відповіді
#     if response.status_code == 201:
#         # Перетворення відповіді в JSON
#         posts = response.json()
        
#         # Виведення перших 5 записів
#         print(posts)
#     else:
#         print(f"Помилка: {response.status_code}")
# except Exception as e:
#     print(f"Виникла помилка: {e}")

# 3
