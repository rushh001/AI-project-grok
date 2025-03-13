import requests
from config import WEATHER_API_KEY, NEWS_API_KEY

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url).json()
    if response.get("main"):
        return f"{city.capitalize()}: {response['main']['temp']}°C, {response['weather'][0]['description']}"
    return "City not found."

def get_news():
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}"
    response = requests.get(url).json()
    articles = response.get("articles", [])[:5]
    return "\n".join([f"{i+1}. {article['title']}" for i, article in enumerate(articles)])
