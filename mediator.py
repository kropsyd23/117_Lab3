from reader import read_country_file
from writer import write

def mediate():
    """Read countries and write them out by region.

    The original code attempted to import `write_regions` from
    `writer.py` which doesn't exist. The writer module exposes
    `write(text)` so import that and call it.
    """
    #it reads all countries from the CSV file
    countries = read_country_file()

    #lists for each region
    Africa = []
    Americas = []
    Asia = []
    Europe = []
    Oceania = []

    #it loops through all countries and separate them by region
    for country in countries:
        region = country.get("region", "").strip()  

        if region == "Africa":
            africa.append(country)

        elif region == "Americas":
            americas.append(country)

        elif region == "Asia":
            asia.append(country)

        elif region == "Europe":
            europe.append(country)

        elif region == "Oceania":
            oceania.append(country)

    #now write one file per region using the writer.write() function
    # writer.write(text, key, index, file_name)
    write(africa, "Africa.csv")
    write(americas, "Americas.csv")
    write(asia,"Asia.csv")
    write(europe,"Europe.csv")
    write(oceania, "Oceania.csv")

    print("All regional files have been written successfully.")


if __name__ == "__main__":
    mediate()
