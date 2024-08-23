import requests

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data.get('cod') != 200:
        return f"Error: {data.get('message')}"

    main = data.get('main', {})
    weather = data.get('weather', [{}])[0]
    wind = data.get('wind', {})
    
    temperature = main.get('temp')
    description = weather.get('description')
    humidity = main.get('humidity')
    wind_speed = wind.get('speed')
    
    return (
        f"Temperature: {temperature}°C\n"
        f"Weather Description: {description.capitalize()}\n"
        f"Humidity: {humidity}%\n"
        f"Wind Speed: {wind_speed} m/s"
    )

def main():
    api_key = 'Prlease enter your api'  
    city = input("Enter the city name: ")
    weather_info = get_weather(api_key, city)
    print(weather_info)

if __name__ == "__main__":
    main()
