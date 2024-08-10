import requests
from bs4 import BeautifulSoup
import pandas as pd

# Base URL structure (modify as needed)
base_url = 'https://www.iihs.org/ratings/vehicle'

# Dictionary of car makes and models
car_models = {
    'subaru': 'outback-4-door-wagon',
    'honda': 'accord-4-door-sedan',
    # Add more makes and models here
}

# List of years
car_years = ['2024', '2023', '2022']  # List of years to apply to each car make/model


# Function to construct the URL
def construct_url(make, model, year):
    return f"{base_url}/{make}/{model}/{year}"


# Function to scrape a single car page
def scrape_car_page(url):
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the rating (Adjust this part according to actual HTML structure)
    rating = soup.find('tr', class_='overall-rating').text.strip()  # Placeholder

    return rating


# Lists to hold the data
makes = []
models = []
years = []
ratings = []

# Loop through each car make and model, then through each year in the list
for make, model in car_models.items():
    for year in car_years:
        url = construct_url(make, model, year)
        try:
            rating = scrape_car_page(url)
            makes.append(make)
            models.append(model)
            years.append(year)
            ratings.append(rating)
        except Exception as e:
            print(f"Failed to scrape {url}: {e}")

# Create a DataFrame
df = pd.DataFrame({
    'Make': makes,
    'Model': models,
    'Year': years,
    'Rating': ratings
})

# Export the data to an Excel file
file_path = 'iihs_car_ratings.xlsx'
df.to_excel(file_path, index=False)

print(f'Data successfully exported to {file_path}')
