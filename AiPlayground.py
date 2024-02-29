#Programmer: Avonlea Thalmann
#Date: 2.29.2024
#Program: AI Playground

print("This will be a place for me to play with programming using AI technology.\n")

#AI Tell the Weather
"""
import requests
import json

def get_weather(location):
    url = "https://openweathermap.org/faq#error401" + location + "&appid=your api key"
    response = requests.get(url).json()
    return response[ 'main' ][ 'temperature' ]
city = 'Richland'
weather = get_weather(city)
print("The weather is: {weather} degrees.")

import requests
import random

chat_prompt = input("Enter the chat prompt: ")

def get_chatpt(prompt):
    url = "http://chatgpt.com/api/api.jsp?mode=text&prompt=\_" + prompt
    response = requests.get(url)
    return response.json()

response = get_chatpt(chat_prompt)
print(response)

import math

def add(x,y):
    print(add(1, 2))
    return x + y
"""

import random

r = random.randint(1,100)

print(r)



