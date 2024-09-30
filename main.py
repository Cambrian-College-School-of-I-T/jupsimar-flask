#find the location of ISS
#weather information
#reverse geolocation(we have lat and lon we will find the country above which the ISS is ?)
#distance between you and ISS
#rest countries api 
# The Flag of Country 


from get_country import country
from get_iss import iss_loc 
from get_weather import get_weather
from get_address import address
from get_country import country
from get_distance import dist


data = iss_loc()
lat,lon=data[0],data[1]

# Weather
weather =get_weather(lat,lon)
temp_c = round(weather["main"]["temp"]-273.15,2)
description = weather["weather"][0]["description"]
print(str(temp_c) + " C " + description)


#address reverse geolocation
add = address(lat,lon)
#Print the Country Code
print("Country Code is :",add["countryCode"])
if(add["countryCode"]==""):
  location = 'pe'
  print("The ISS is over Water")
  flag = country(location)[0]["flags"]["png"]
  print(flag)
else:
  location= add["countryCode"]
  flag= country(location)[0]["flags"]["png"]
  print(flag)

# the distance between ISS and you 
distance = dist(lat,lon,46.5290876,-80.9432954)
print(f"You are {distance} km from ISS !")

