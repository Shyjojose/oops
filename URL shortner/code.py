import random
import string
import json

# in this code short is a python dictionary and when i call save_data () it will save
# it as a json file. 
# in large system the production systems persistent data is usally stored as postgresql,
# mysql mongodb there is redis for caching and many more. but here we are using json file to store the data.
def save_data():
    with open("URL shortner/short_urls.json", "w") as file:
        json.dump(short, file)

def load_data():
    try:
        with open("URL shortner/short_urls.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    

def generate_code():
    characters = string.ascii_letters + string.digits
    # ascii_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # digits = "0123456789"
    code = ""
    for i in range(6):
        code += random.choice(characters)
    return code

print(generate_code())   # something like "aB3x9K"

def shorten_url(url):
    code = generate_code()
    short[code] = url
    return code

def retrieve_url(code):
    return short.get(code, "URL not found")

user= "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
short = load_data()  # Load existing short URLs from file
code = shorten_url(user)  
save_data()  # Save the updated short URLs to file
print("Shortened code:", code)  # something like "aB3x9K"
print("Original URL:", retrieve_url(code))  # https://www.youtube.com/watch?v=d