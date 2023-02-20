# Module list 
import os,sys,json,requests
from colorama import *
from pystyle import *

# for run program + title name + clear | ^^
init()
os.system("title 𝒅𝒆𝒗 𝒃𝒚 𝒍𝒐𝒄𝒌𝒆𝒅")
os.system("cls")

# my banner is so bad :/
banner = (Colorate.Vertical(Colors.purple_to_blue, """
          .__            .__                 __                 
          |__|_____      |  |   ____   ____ |  | ____ ________  
          |  \____ \     |  |  /  _ \ /  _ \|  |/ /  |  \____ \ 
          |  |  |_> >    |  |_(  <_> |  <_> )    <|  |  /  |_> >
          |__|   __/     |____/\____/ \____/|__|_ \____/|   __/ 
             |__|                                \/     |__|      (dev by locked)
   
"""))
print(banner)

# requests for use api ^^
ip = input(Colorate.Vertical(Colors.purple_to_blue, "\n Type IP address to Lookup -> ")); ip.replace(" ", "")
r = requests.get(f"http://ip-api.com/json/{ip}")
r2 = requests.get(f"https://ipinfo.io/{ip}")
values = json.loads(r.text)
data = r2.json()
city = data["city"]
ip = data["ip"]
hostname = data["hostname"]
postal = data["postal"]
location = data["loc"].split(",")
latitude = location[0]
longitude = location[1]



# response for the request è_è
print("\n \n" + Colorate.Horizontal(Colors.purple_to_red,"    LOCATION"))

print( "\n" + Colorate.Vertical(Colors.purple_to_blue," City ") + " -> "  + city)
print(Colorate.Vertical(Colors.purple_to_blue," Region ") +  " -> " + values["regionName"])
print(Colorate.Vertical(Colors.purple_to_blue," Postale Code ") + "-> " + postal)
print(Colorate.Vertical(Colors.purple_to_blue," Country + Code ") + " -> " + values["country"] + f" [{values['countryCode']}]")
print(Colorate.Vertical(Colors.purple_to_blue," Time Zone ") + " -> " + values["timezone"])
print(Colorate.Vertical(Colors.purple_to_blue," Coordinates ") +  " -> " + latitude, "|", longitude)

print("\n \n" + Colorate.Horizontal(Colors.purple_to_red,"    NETWORK"))

print("\n" + Colorate.Vertical(Colors.purple_to_blue, " Ip Address " ) + " -> " + ip)
print(Colorate.Vertical(Colors.purple_to_blue," Hostname ") +  " -> " + hostname)
print(Colorate.Vertical(Colors.purple_to_blue," Provider ") +  " -> " + values["isp"])
print("\n \n")

# Allows to restart the program to use another ip ;)
os.system("pause")
os.system('cmd /k "python Iplookup.py"')