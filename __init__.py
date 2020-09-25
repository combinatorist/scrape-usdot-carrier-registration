from bs4 import BeautifulSoup
import requests
URL = "https://ai.fmcsa.dot.gov/SMS/Carrier/21800/CarrierRegistration.aspx"
page = requests.get(URL)
page[:15]
page.content[:15]
pprint(page.content)
from pprint import pprint
pprint(page.content)
pprint(page.content())
soup = BeautifulSoup(page.content, 'html.parser')
help(soup)
help(soup)
soup.decode(pretty_print=true)
soup.decode(pretty_print=True)
pprint(soup.decode(pretty_print=True))
soup.find_all('li', class='checked')
b'id' in soup.text
'id' in soup.text
soup.find_all('li', class_='checked')
cargo_carried = soup.find('ul', class_ = 'cargo')
cargo_carried.prettify
cargo_types = cargo_carried.find_all('li', class_='checked')
cargo_types
included_cargo_soup = cargo_carried.find_all('li', class_='checked')
del included_cargo_soup
included_cargo_soups = cargo_carried.find_all('li', class_='checked')
[item.text for item in included_cargo_soups]
[item.find('span').decompose().text for item in included_cargo_soups]
included_cargo_soups
[item.text for item in included_cargo_soups]
[item.find('span').extract().text for item in included_cargo_soups]
included_cargo_soups = cargo_carried.find_all('li', class_='checked')
[item.find('span').extract().text for item in included_cargo_soups]
help(soup.find_all)
del included_cargo_soups
included_cargo_soups = cargo_carried.find_all('li', class_='checked')
# remove checkmark span (redundant on li class)
[item.find('span').decompose() for item in included_cargo_soups]
del soup
soup = BeautifulSoup(page.content, 'html.parser')
cargo_carried = soup.find('ul', class_ = 'cargo')
included_cargo_soups = cargo_carried.find_all('li', class_='checked')
included_cargo_soups.prettify
included_cargo_soups
# remove checkmark span (redundant on li class)
[item.find('span').decompose() for item in included_cargo_soups]
[item.text for item in included_cargo_soups]
included_cargo = [item.text for item in included_cargo_soups]
vehicle_type_soups = soup.find_all('th', class_='vehType')
vehicle_type_rows = [item.find_parent('tr') for item in vehicle_type_soups]
vehicle_type_rows
vehicle_type_rows[0].text
vehicle_type_rows[0].text.split('\n')
vehicle_type_rows[0].find_all()
[[item.text for item in row.find_all()] for row in vehicle_type_rows]
vehicle_type_table = [[item.text for item in row.find_all()] for row in vehicle_type_rows]
pprint(vehicle_type_table)
%hist > __init__.py
! cat __init__.py
! ls
%history
%history -g -f __init__.py
%history -f __init__.py
