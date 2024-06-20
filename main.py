import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import folium
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Function to validate phone number format
def validate_phone_number(number):
    try:
        parsed_number = phonenumbers.parse(number)
        if phonenumbers.is_valid_number(parsed_number):
            return parsed_number
        else:
            return None
    except phonenumbers.phonenumberutil.NumberParseException:
        return None

# Main function for location tracking
def track_location():
    # Get OpenCage API Key from environment variable
    opencage_api_key = os.getenv("OPENCAGE_API_KEY") ## Otherwise is -> opencage_api_key = "ENTERKEY"
    if not opencage_api_key:
        raise ValueError("OpenCage API Key not found. Please set it in the environment or in a .env file.")

    number = input("Please enter the phone number (with country code): ")

    # Validate phone number format
    parsed_number = validate_phone_number(number)
    if not parsed_number:
        print("Invalid phone number format. Please enter a valid phone number.")
        return

    # Get location and carrier information
    location = geocoder.description_for_number(parsed_number, "en")
    service_name = carrier.name_for_number(parsed_number, "en")

    print(f"Location: {location}")
    print(f"Service Provider: {service_name}")

    # Geocode using OpenCage API
    geocoder_obj = OpenCageGeocode(opencage_api_key)
    query = str(location)
    try:
        result = geocoder_obj.geocode(query)
        if result and len(result):
            lat = result[0]['geometry']['lat']
            lng = result[0]['geometry']['lng']

            # Create map and mark the location
            my_map = folium.Map(location=[lat, lng], zoom_start=9)
            folium.Marker([lat, lng], popup=location).add_to(my_map)

            # Save map to HTML file
            html_file = "location.html"
            my_map.save(html_file)

            # Open the HTML file in the default web browser
            import webbrowser
            webbrowser.open('file://' + os.path.realpath(html_file))

            print("Location tracking completed. Map saved and opened in browser.")
        else:
            print("Location not found.")
    except Exception as e:
        print(f"Error geocoding: {e}")

    print("Thank you")

# Run the main function
if __name__ == "__main__":
    track_location()
