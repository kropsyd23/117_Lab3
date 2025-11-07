from reader import read_country_file
from writer import write

def mediate():
    """Read countries and write them out by region."""
    #it reads all countries from the CSV file
    countries = read_country_file()

    #lists for each region
    africa = []
    americas = []
    asia = []
    europe = []
    oceania = []

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
    write(africa, "africa.csv")
    write(americas, "americas.csv")
    write(asia,"asia.csv")
    write(europe,"europe.csv")
    write(oceania, "oceania.csv")

    print("All regional files have been written successfully.")

if __name__ == "__main__":
    mediate()
