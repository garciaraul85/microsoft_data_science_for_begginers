import requests

# Step 1. Getting data
url = 'https://en.wikipedia.org/wiki/Data_science'

text = requests.get(url).content.decode('utf-8')
print(text[:1000])


# Step 2. Gathering data