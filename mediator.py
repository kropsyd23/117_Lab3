from reader import read_country_file
from writer import write

def mediate():
    """Read countries and write them out by region.

    The original code attempted to import `write_regions` from
    `writer.py` which doesn't exist. The writer module exposes
    `write(text)` so import that and call it.
    """
    countries = read_country_file()
    write(countries)