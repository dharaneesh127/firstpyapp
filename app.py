import requests

def get_weather(city):
  """
  Fetches weather data for a given city using OpenWeatherMap API.

  Args:
      city (str): Name of the city to get weather information for.

  Returns:
      dict: Dictionary containing weather information or None if an error occurs.
  """
  api_key = "4f9c00e7a85bc5ea06d35ee0e31e48ae"
  url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

  try:
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
  except requests.exceptions.RequestException as e:
    print(f"Error requesting weather data: {e}")
    return None

def main():
  """
  Prompts the user for a city, retrieves weather data, and displays it.
  """
  city = input("Enter a city name: ")
  weather_data = get_weather(city)

  if weather_data:
    description = weather_data["weather"][0]["description"]
    temperature = int(weather_data["main"]["temp"] - 273.15)
    print(f"Weather in {city}: {description}, {temperature}°C")
  else:
    print("Error retrieving weather data. Please try again.")

if __name__ == "__main__":
  main()