import requests
import sys

API_KEY = "zVawrqxAVNv0jhYscuDvBAAZfWSQJekVR4xK6Myx"

# Check if user provided an argument
if len(sys.argv) < 2:
    print("Usage: python3 usda_search.py <food name>")
    sys.exit(1)

# Join all command-line args to support multi-word foods
SEARCH_TERM = " ".join(sys.argv[1:])

URL = f"https://api.nal.usda.gov/fdc/v1/foods/search?api_key={API_KEY}&query={SEARCH_TERM}"

response = requests.get(URL)

if response.status_code == 200:
    data = response.json()
    foods = data.get("foods", [])
    
    print(f"\nFound {len(foods)} food results for '{SEARCH_TERM}'\n")
    
    for food in foods[:3]:
        print(f"Description: {food['description']}")
        print(f"FDC ID: {food['fdcId']}")
        print("Nutrients:")
        for nutrient in food.get("foodNutrients", []):
            print(f"  - {nutrient['nutrientName']}: {nutrient['value']} {nutrient['unitName']}")
        print("-" * 50)

else:
    print(f"Error: {response.status_code} - {response.text}")
