#-------------------Phone Number trace-------------------------------------------------------------------------------#
import phonenumbers       #-------------------------------import phonenumbers module for trace
from phonenumbers import timezone,geocoder,carrier  #-----import timezone, geocoder, carrier from phonenumbers module
number = input("Enter Phone Number....") #----------------input phonenumber-------
phone = phonenumbers.parse(number)       #----------------converting these codes into machine language
time = timezone.time_zones_for_number(phone) #------------timezone for number
car = carrier.name_for_number(phone,"en") #---------------carrier for service provider
reg=  geocoder.description_for_number(phone,"en")#--------geo region location
print(phone)
print(time)
print(car)
print(reg)