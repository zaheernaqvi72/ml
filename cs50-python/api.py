import requests

username = input('Enter your github username: ')

url = f"https://api.github.com/users/{username}"

response = requests.get(url).json()

print(f"Your name is {response['name']} and you have {response['public_repos']} public repositories. You joined github on {response['created_at']}. Your bio is {response['bio']} and your location is {response['location']}.")


