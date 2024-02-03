# Geocoding-scrape
Scraping tool using Selenium, Geocoding and Flask

## Prerequisites
- selenium==4.2.0
- flask==3.0.1
- Chromedriver.exe downloaded and change the path to the directory of the .exe file

## Scrape data & Serving data in REST API
- Run python scrape.py to scrape the data and store into SQL Database
- To serve the data in REST API: run python app.py ->
- Navigate to http://localhost:5000/subway_locations?page=10 or http://localhost:5000/subway_locations?per_page=10
- Pagination is applied as query parameters to display how many data required 

## Web application & Data visualization
- 
