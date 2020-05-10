import requests

def random_quote():
    url='http://quotes.stormconsultancy.co.uk/random.json'
    response = requests.get(url)
    posts= response.json()
    return posts