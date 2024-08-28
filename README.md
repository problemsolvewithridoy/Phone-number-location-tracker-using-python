
# Phone Number Location Tracker using Python 

Are you curious about the location of a mobile number? Maybe you want to track a lost phone or keep tabs on your child's whereabouts. Whatever your reason, you can use Python to find the location of a mobile number.

In this step-by-step guide, we'll show you how to track a mobile number's location using Python. You'll need some Python coding skills and access to a few geolocation libraries. Let's get started!

To make this project only you need to follow this step:-








## Installation

Install package with pip

```bash
  pip install phonenumbers
  pip install folium
  pip install geocoder
  pip install opencage
```

Now need to collect Geocoder API Key from https://opencagedata.com/

Step1: Need to log in or sign up

![github1](https://user-images.githubusercontent.com/123636419/215339770-3cc5ba46-d502-42b9-9f15-856718cf22d1.PNG)

Step2: Need to click Geocoding API

![github2](https://user-images.githubusercontent.com/123636419/215339775-89aef127-2390-4f8d-8ad6-1129789eabab.PNG)

Step3: From API Keys collect API key

![github3](https://user-images.githubusercontent.com/123636419/215339773-0171d38c-b9ad-490a-95d8-47366321048a.PNG)




## Deployment

To deploy this project run

```bash
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import opencage
from opencage.geocoder import OpenCageGeocode
import folium


key = "your key" #Geocoder API Key need to paste here "your key" 
number = input("please giver your number: ")
new_number = phonenumbers.parse(number)
location = geocoder.description_for_number(new_number, "en")
print(location)

service_name = carrier.name_for_number(new_number,"en")
print(service_name)

geocoder = OpenCageGeocode(key)
query = str(location)
result = geocoder.geocode(query)
#print(result)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']

print(lat,lng)

my_map = folium.Map(location=[lat,lng], zoom_start=9)
folium.Marker([lat, lng], popup= location).add_to(my_map)

my_map.save("location.html")

print("location tracking completed")
print("Thank you")
```


You can follow me

Facebook:- https://www.facebook.com/problemsolvewithridoy/

Linkedin:- https://www.linkedin.com/in/ridoyhossain/

⚠️⚠️⚠️ Attention Please ⚠️⚠️⚠️

Tracking the location of a phone number typically involves using specialized services or apps that can access databases and provide information on the general geographic location of a phone. However, it's important to note that tracking someone's location without their explicit consent can raise ethical and legal concerns.

Here are some common methods used for tracking phone number locations:

1. Mobile Tracking Apps: There are several apps available that claim to track phone numbers. Some require installation on the target device, while others might use different methods like phone number databases or social media profiles to provide location information.

2. Reverse Phone Lookup Services: Websites or services like Truecaller, Whitepages, or Spokeo offer reverse phone lookup services. They might provide information on the registered location of a phone number based on public records or user-contributed data.

3. GPS Tracking Services: Certain apps or services allow you to track the location of family members or devices with their consent. For example, Find My iPhone for Apple devices or Google's Find My Device for Android devices can help locate a device linked to a specific account.

4. Telecom Service Providers: In some cases, telecom service providers might offer location tracking services for authorized purposes like finding a lost device or for legal investigations. This is usually done with proper authorization and legal documentation.

Remember, accessing someone's location without their consent can infringe upon their privacy and might be illegal in some jurisdictions. Always ensure you have permission or legal authorization before attempting to track someone's location.

If you're trying to locate a lost device or have concerns about someone's safety, it's often best to involve the authorities or use legitimate methods designed for such situations.

Note:- This project was developed solely for entertainment purposes. Moreover, this particular method is ineffective. Thank you 

YouTube:- https://www.youtube.com/@problemsolvewithridoy

If you have any confusion, please feel free to contact me. 
Thank you
