from bs4 import BeautifulSoup
import requests

URL = "https://ai.fmcsa.dot.gov/SMS/Carrier/21800/CarrierRegistration.aspx"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
cargo_carried = soup.find('ul', class_ = 'cargo')
included_cargo_soups = cargo_carried.find_all('li', class_='checked')
# remove checkmark span (redundant on li class)
[item.find('span').decompose() for item in included_cargo_soups]
included_cargo = [item.text for item in included_cargo_soups]
vehicle_type_soups = soup.find_all('th', class_='vehType')
vehicle_type_rows = [item.find_parent('tr') for item in vehicle_type_soups]
vehicle_type_table = [[item.text for item in row.find_all()] for row in vehicle_type_rows]

print(included_cargo, vehicle_type_table)
