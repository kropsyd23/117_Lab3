r"""
Country full CSV file reader.
"""

from csv import DictReader
from pprint import pp

filename = 'country_full.csv'

def read():
    try:   
        countries = read_countries() 
    except EOFError as e:
        pass
    except IOError as e:
        pass
    except FileNotFoundError as e:
        pass
    except PermissionError as e:
        pass

    country_list = list(countries)
    return country_list

def read_countries():
    ''' read in countries from the country full csv file '''
    return DictReader(open(filename))

if __name__ == "__main__":
    countries = read_countries()
    print("Dialect:", countries.dialect)
    print("line_num:", countries.line_num)
    # print("fieldnames:", countries.fieldnames)
    print("csv header: ")
    pp(countries.fieldnames)
    country_list = list(countries)
    # print("First country:", country_list[0])
    print("first country: ")
    pp(country_list[0])
    print("Number of countries:", len(country_list))