"""
Write separate files for each region
"""

import reader # for testing when ran as main

def write_country(file, line):
    ''' add information about a country to its region file '''
    # add the country name then remove from dictionary to set up commas
    file.write(line["name"])
    del line["name"]

    # loop through remaining information
    for key, value in line.items():    
        # if there is only one element of the list, add that element now
        if isinstance(value, str):
            if value != "":
                file.write("," + value)
            else:
                file.write("," + '""')
    
        # if there are multiple elements of the list, loop through them to add every element
        else:
            for item in value:
                file.write("," + item)
    file.write('\n')

def write(text):
    ''' write information about each country to its region file '''
    
    # open a writing file for each region
    africa = open("africa.csv", 'w')
    americas = open("americas.csv", 'w')
    asia = open("asia.csv", 'w')
    europe = open("europe.csv", 'w')
    oceania = open("oceania.csv", 'w')

    # loop through every line in the text
    for line in text:

        # add to country.log if region is each country
        if line["region"] == "Africa":
            write_country(africa, line)

        if line["region"] == "Americas":
            write_country(americas, line)
        
        if line["region"] == "Asia":
            write_country(asia, line)
        
        if line["region"] == "Europe":
            write_country(europe, line)
        
        if line["region"] == "Oceania":
            write_country(oceania, line)
    
    # close each file
    africa.close()
    americas.close()
    asia.close()
    europe.close()
    oceania.close()

if __name__ == "__main__":
    text = reader.read_country_file()
    write(text)
    