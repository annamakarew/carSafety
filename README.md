# IIHS Car Ratings Scraper

This project is a Python script designed to scrape car safety ratings from the [Insurance Institute for Highway Safety (IIHS)](https://www.iihs.org/) website. The script fetches safety ratings for various SUV models available in the United States and exports the data to an Excel spreadsheet. It handles multiple models per car make, and incorporates mechanisms to deal with potential issues like too many requests.

## Features

- **Multiple Car Models**: The script supports scraping ratings for multiple car models across different makes.
- **Excel Export**: The scraped data is exported into an Excel file for easy analysis and sharing.
- **Customizable Input**: The script allows you to easily customize the list of car makes, models, and years to be scraped.

## Prerequisites

- Python 3.x
- Required Python libraries: `requests`, `BeautifulSoup4`, `pandas`, `openpyxl`, `time`

You can install the required libraries using:

```bash
pip install requests beautifulsoup4 pandas openpyxl time
```

## How to Use

1. **Clone the Repository**

   Clone this repository to your local machine:

   ```bash
   git clone https://github.com/annamakarew/carSafety.git
   cd carSafety
   ```

2. **Customize the Input Data**

   The script uses a dictionary called `car_models` to define the car makes and models you want to scrape. You can edit this dictionary in the script to include the cars you're interested in. For example:

   ```python
   car_models = {
       'subaru': [
           'outback-4-door-suv',
           'forester-4-door-suv'
       ],
       'honda': [
           'cr-v-4-door-suv',
           'pilot-4-door-suv'
       ]
   }
   ```

   Similarly, you can adjust the list of years:

   ```python
   car_years = ['2024', '2023', '2022']
   ```

3. **Run the Script**

   Run the script to start scraping the data:

   ```bash
   python carSafety.py
   ```

   The script will output the data to an Excel file (`iihs_car_ratings_suv.xlsx` by default) in the same directory.

## Project Structure

- `carScraper.py`: Main script for scraping IIHS car ratings.
- `README.md`: This documentation file.
- `requirements.txt`: List of required Python libraries.

## Contribution

Contributions are welcome! If you have suggestions, bug reports, or feature requests, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the IIHS for providing public access to their vehicle safety ratings.
