import requests, json 
  
# Enter your API key here 
api_key = "d71f373e048f9c80a4cd78ee5f5aa13e"
#open weather map URL
base_url = "http://api.openweathermap.org/data/2.5/weather?"
# relevant city
city_name = "Tel-Aviv"
# request URL
query_url = base_url + "appid=" + api_key + "&q=" + city_name+ "&units=metric"
#get the data
response = requests.get(query_url)
general_data = response.json()

#simple check if the pull worked and no connectivity issues
if str(general_data["cod"]) == '200':

    main_data = general_data["main"]
    #temperature
    temperature = main_data["temp"]
    # what it feels like 
    Feels = main_data["feels_like"]
    #get the description
    weather = general_data["weather"]
    weather_description = weather[0]["description"]
  
    # print following values
    print(" Temperature = " + str(temperature) +
        "\n Description = " + str(weather_description) +
        "\n Feels like = " + str(Feels)
    )
else:
    print("Error in request")