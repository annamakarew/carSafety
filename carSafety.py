import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Base URL structure
base_url = 'https://www.iihs.org/ratings/vehicle'

# Dictionary of car makes and models
car_models = {
    'subaru': [
        'outback-4-door-wagon',
        'forester-4-door-suv',
        'ascent-4-door-suv'
    ],
    'honda': [
        'cr-v-4-door-suv',
        'pilot-4-door-suv',
        'passport-4-door-suv'
    ],
    'toyota': [
        'rav4-4-door-suv',
        'highlander-4-door-suv',
        '4runner-4-door-suv'
    ],
    'ford': [
        'escape-4-door-suv',
        'explorer-4-door-suv',
        'edge-4-door-suv'
    ],
    'chevrolet': [
        'equinox-4-door-suv',
        'traverse-4-door-suv',
        'blazer-4-door-suv'
    ],
    'nissan': [
        'rogue-4-door-suv',
        'murano-4-door-suv',
        'pathfinder-4-door-suv'
    ],
    'jeep': [
        'cherokee-4-door-suv',
        'grand-cherokee-4-door-suv',
        'compass-4-door-suv',
        'wrangler-4-door-suv'
    ],
    'hyundai': [
        'tucson-4-door-suv',
        'santa-fe-4-door-suv',
        'kona-4-door-suv',
        'palisade-4-door-suv'
    ],
    'kia': [
        'sportage-4-door-suv',
        'sorento-4-door-suv',
        'telluride-4-door-suv'
    ],
    'bmw': [
        'x1-4-door-suv',
        'x3-4-door-suv',
        'x5-4-door-suv'
    ],
    'audi': [
        'q3-4-door-suv',
        'q5-4-door-suv',
        'q7-4-door-suv',
        'q8-4-door-suv'
    ],
    'mercedes-benz': [
        'glc-4-door-suv'
    ],
    'lexus': [
        'nx-4-door-suv',
        'rx-4-door-suv',
        'ux-4-door-suv'
    ],
    'volkswagen': [
        'tiguan-4-door-suv',
        'atlas-4-door-suv'
    ],
    'buick': [
        'encore-4-door-suv',
        'enclave-4-door-suv'
    ],
    'cadillac': [
        'xt4-4-door-suv',
        'xt5-4-door-suv',
        'xt6-4-door-suv',
        'escalade-4-door-suv'
    ]
}

# List of years
car_years = ['2024', '2023', '2022', '2021', '2020']  # List of years to apply to each car make/model


# Function to construct the URL
def construct_url(make, model, year):
    return f"{base_url}/{make}/{model}/{year}"


# Function to scrape a single car page
def scrape_car_page(url, delay=6):
    # Although delay slows down program, it is necessary to avoid being rate limited.
    time.sleep(delay)
    try:
        response = requests.get(url)
        print(response.headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        ratings_div = soup.find('div', class_='ratings-overview')
        # Check if the div was found
        if not ratings_div:
            return {}
        # Dictionary to hold the ratings
        ratings = {}
        # Find all rating rows
        rating_rows = ratings_div.find_all('tr')
        for row in rating_rows:
            # Extract rating name and value
            if row.find('th', scope='row'):
                rating_name = row.find('th', scope='row').text.strip()
                rating_value = row.find('div', class_='rating-icon-block').text.strip()
                # Add to ratings dictionary
                ratings[rating_name] = rating_value
        return ratings
    except requests.exceptions.RequestException as e:
        print(e)
        return {}

# Lists to hold the data
car_data = []

# Loop through each car make and model, then through each year in the list
for make, models in car_models.items():
    for model in models:
        for year in car_years:
            url = construct_url(make, model, year)
            try:
                ratings = scrape_car_page(url)
                # Combine car details with ratings
                car_entry = {'Make': make, 'Model': model, 'Year': year}
                car_entry.update(ratings)
                car_data.append(car_entry)
            except Exception as e:
                print(f"Failed to scrape {url}: {e}")

# Create a DataFrame
df = pd.DataFrame(car_data)

# Export the data to an Excel file
file_path = 'iihs_car_ratings.xlsx'
df.to_excel(file_path, index=False)

print(f'Data successfully exported to {file_path}')
