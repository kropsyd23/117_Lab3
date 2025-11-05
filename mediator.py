from reader import read_country_file
from writer import write_regions

def mediate():
    countries = read_country_file()
    write_regions(countries)
    pass