print("This program will tell you if the temperature is cold.")
service = WeatherService()
temperature = service.get_fahrenheit()
print("The temperature is {0} degrees fahrenheit.".format(temperature))
if temperature < 30.0:
    print("It is currently very cold.")