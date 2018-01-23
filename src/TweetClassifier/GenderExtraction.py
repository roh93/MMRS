import requests

def genderExtract(name):
    url= "https://api.genderize.io/?name=" + name;
    response = requests.get(url)
    return response.json()['gender']

#genderExtract("harish")