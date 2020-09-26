from bs4 import BeautifulSoup
import requests
import csv

def scrape_carrier(carried_id):
    """"scrape the page of one carrier"""
    URL = f"https://ai.fmcsa.dot.gov/SMS/Carrier/{carrier_id}/CarrierRegistration.aspx"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    # get cargo
    cargo_carried = soup.find('ul', class_ = 'cargo')
    included_cargo_soups = cargo_carried.find_all('li', class_='checked')
    # remove checkmark span (redundant on li class)
    [item.find('span').decompose() for item in included_cargo_soups]
    included_cargo = [item.text for item in included_cargo_soups]

    # get vehicle type
    vehicle_type_soups = soup.find_all('th', class_='vehType')
    vehicle_type_rows = [item.find_parent('tr') for item in vehicle_type_soups]
    vehicle_type_table = [[item.text for item in row.find_all()] for row in vehicle_type_rows]

    return (included_cargo, vehicle_type_table)

def parse_carrier_ids(fp):
    """parse carriers ids to put into scraper"""
    with open(fp, 'r') as csvfile:
        reader = csv.reader(csvfile)
        CARRIER_ID_COLUMN_INDEX = 0
        ids = [row[CARRIER_ID_COLUMN_INDEX] for row in reader]
    return ids

def write_carrier_results(results):
    """writes carrier information into joinable csvs"""
    with open('data/carrier.csv', 'a') as carrier_file:
        csv.writer(carrier_file).write_row(results[0])

    with open('data/carrier_vehicle.csv', 'a') as carrier_vehicle_file:
        csv.writer(carrier_vehicle_file).write_row(results[1])

def main(fp):
    """scrape all carriers"""
    ids = parse_carrier_ids(fp)
    for carrier_id in ids:
        results = scrape_carrier(carrier_id)
        write_carrier_results(results)

if __name__ == "__main__":
    main('FMCSA_CENSUS1_2020Aug/FMCSA_CENSUS1_2020Aug.txt')
