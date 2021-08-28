import requests
class WeatherApp(DeviceTracker):
    def __init__(self, ip_url):
        self.ip_url = ip_url
        self.weather_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=9d41bd4e5bffd04e03a6cb'
        self.place_name = None
        
    def get_weather_data(self):
        self.place_name = input("Please enter valid city name: ")
        w_url = self.weather_url.format(self.place_name)
        w_req = requests.get(url=w_url)
 
        if (w_req.status_code == 200):
            w_data = w_req.json()
        else:
            print("-----------------")
            print("The entered place name is not valid")
            print("Getting the user location ...")
            self.place_name = self.get_user_loc()
            w_url = self.weather_url.format(self.place_name)
            w_req = requests.get(url=w_url)
            w_data = w_req.json()
 
        return w_data
 
    def get_parsed_details(self):
        w_data = self.get_weather_data()
 
        desc = w_data['weather'][0]['description']
        temp = w_data['main']['temp']
        humidity = w_data['main']['humidity']
        wind_speed = w_data['wind']['speed']
        all_clouds = w_data['clouds']['all']
 
        celsius = temp - 273
        farenheit = (celsius * (9 / 5)) + 32
 
        print("-----------------")
        print("The weather details of the place - {}".format(self.place_name))
        print("Weather description - ", desc)
        print("The temp in celsius - ", round(celsius, 2))
        print("The temp in farenheit - ", round(farenheit, 2))
        print("The wind speed - {} mpg".format(wind_speed))
        print("Humidity - ", humidity)
        print("Total clouds - ", all_clouds)

        return None
 
 
