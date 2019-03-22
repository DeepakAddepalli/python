import requests
url="http://garuda.pythonanywhere.com/city"
#add word
payload ={"word":"deepak","meaning":"baml"}

cities =["Hyderabad","New York","Beijing","Tokyo","Hong Kong","New Jersey","Vatican City","Colombo","Dallas"]

for city in cities:
   print( city,requests.get(url +"/"+city).json().get("elevation")[0])

url="http://garuda.pythonanywhere.com/words"
response=requests.get(url)
if response.ok:
    print(response.json()) #dict of words

import requests
url="http://garuda.pythonanywhere.com/words"
response=requests.get(url + "/air") #meaning of the word
if response.ok:
    print(response.json())

import requests
url="http://garuda.pythonanywhere.com/words"
response=requests.get(url + "/deepak") # meaning of the word
if response.ok:
    print(response.json())
