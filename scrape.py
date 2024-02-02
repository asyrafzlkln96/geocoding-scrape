from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import selenium.common.exceptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

import time
import os
import logging,logging.handlers
import argparse
import sqlite3
from insert_table import insert_data
from get_coordinates import get_lat_long

# Tool to scrape subway name, address, opening hours, waze link 
# ensure have pagination
# Push all data to DB

# Initialize chrome webdriver, change to your chromedriver.exe path
chrome = webdriver.Chrome(r'C:\Users\Asyraf Zainor Rashid\Desktop\API-Building\tsl_assignment\automate_instagram_login-selenium\chromedriver.exe')
chrome.get('https://subway.com.my/find-a-subway')


input_element = chrome.find_element(By.XPATH, '//input[@id="fp_searchAddress"]')

# Enter text into the input element
input_element.send_keys('kuala lumpur')

# Perform any additional actions, like clicking the search button
search_button = chrome.find_element(By.XPATH, '//button[@id="fp_searchAddressBtn"]')
search_button.click()

# location_list = '//div[@id="fp_locationlist"]'
# locations = chrome.find_elements(By.XPATH, location_list)
base_class = 'fp_listitem fp_list_marker'
location_list_xpath = f'//*[contains(@class, "{base_class}")]'
locations = chrome.find_elements(By.XPATH, location_list_xpath)

# print('locations:',locations)


names = []
addresses = []
opening_hours_list = []
waze_urls = []

for location in locations:
	try:
		# Extract information from the results
		name = location.find_element(By.XPATH, './/h4').text
		address = location.find_element(By.XPATH, './/div[@class="infoboxcontent"]/p[1]').text
		opening_hours = location.find_element(By.XPATH, './/div[@class="infoboxcontent"]/p[3]').text
		# waze_url = location.find_element(By.XPATH,'//i[@class="fa-brands fa-waze"]/ancestor::a').get_attribute('href')
		waze_url = location.find_element(By.XPATH, './/a[contains(@href, "waze.com")]').get_attribute('href')


	except NoSuchElementException:
		opening_hours = "Opening hours not available"

	names.append(name)
	addresses.append(address)
	opening_hours_list.append(opening_hours)
	waze_urls.append(waze_url)
	# Print or use the extracted information as needed
	print("Names:", names)
	print("Address:", addresses)
	print("Opening Hours:", opening_hours_list)
	print('Waze URL:',waze_urls)

	insert_data(names, addresses, opening_hours_list, waze_urls)
	# api_key = 'AIzaSyD3-nDvFPvB6yUMY4VgzKAZGVOj1chFrvk'

	# coordinates = get_lat_long(api_key, address)
	# print('coordinates:',coordinates)

chrome.quit()