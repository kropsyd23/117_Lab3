r"""
Country full CSV file reader.
"""

from csv import DictReader
from pprint import pp

filename = 'country_full.csv'

def read_country_file():
    ''' Read countries '''
    try:   
        countries = open_country_file()
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

def open_country_file():
    ''' Open the country full csv file '''
    return DictReader(open(filename))

if __name__ == "__main__":
    country_file = open_country_file()
    print("Dialect:", country_file.dialect)
    print("line_num:", country_file.line_num)
    # print("fieldnames:", countries.fieldnames)
    print("csv header: ")
    pp(country_file.fieldnames)
    country_list = list(country_file)
    # print("First country:", country_list[0])
    print("first country: ")
    pp(country_list[0])
    print("Number of countries:", len(country_list))