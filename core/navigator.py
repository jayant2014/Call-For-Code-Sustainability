import googlemaps
from datetime import datetime

# Replace 'YOUR_API_KEY' with your actual Google Maps API key
gmaps = googlemaps.Client(key='YOUR_API_KEY')

def find_nearby_recycling_units(location, keyword="recycling"):
    try:
        # Perform a nearby search for recycling units
        places = gmaps.places_nearby(location, radius=5000, keyword=keyword)
        
        if not places:
            print("No recycling units found nearby.")
            return
        
        print("Nearby Recycling Units:")
        for place in places['results']:
            name = place['name']
            address = place['vicinity']
            rating = place.get('rating', 'N/A')
            print(f"Name: {name}\nAddress: {address}\nRating: {rating}\n")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    try:
        # Prompt the user for their current location (latitude and longitude)
        lat = float(input("Enter your current latitude: "))
        lng = float(input("Enter your current longitude: "))
        
        # Create a tuple with the user's location
        user_location = (lat, lng)
        
        # Find nearby recycling units
        find_nearby_recycling_units(user_location)
    
    except ValueError:
        print("Invalid latitude or longitude. Please enter valid coordinates.")
