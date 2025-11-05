"""
Write separate files for each country
"""
import reader
filename = 'country_ful.csv'

if __name__ == "__main__":
    text = reader.read_countries()
    africa = open("africa.log", 'w')
    americas = open("americas.log", 'w')
    asia = open("asia.log", 'w')
    europe = open("europe.log", 'w')
    oceania = open("oceania.log", 'w')


    # loop through every line in text
    for line in text:

        # add to country.log if region is each country
        if line["region"] == "Africa":
            for key, value in line.items():
                africa.write(key + ': ')

                # if there is only one element of the list, add that element now
                if isinstance(value, str):
                    africa.write(value + ", ")
                
                # if there are multiple elements of the list, loop through them to add every element
                else:
                    for item in value:
                        africa.write(item + ', ')
            africa.write('\n')
        
        if line["region"] == "Americas":
            for key, value in line.items():
                americas.write(key + ': ')
                if isinstance(value, str):
                    americas.write(value + ", ")
                else:
                    for item in value:
                        americas.write(item + ', ')
            americas.write('\n')
        
        if line["region"] == "Asia":
            for key, value in line.items():
                asia.write(key + ': ')
                if isinstance(value, str):
                    asia.write(value + ", ")
                else:
                    for item in value:
                        asia.write(item + ', ')
            asia.write('\n')
        
        if line["region"] == "Europe":
            for key, value in line.items():
                europe.write(key + ': ')
                if isinstance(value, str):
                    europe.write(value + ", ")
                else:
                    for item in value:
                        europe.write(item + ', ')
            europe.write('\n')
        
        if line["region"] == "Oceania":
            for key, value in line.items():
                oceania.write(key + ': ')
                if isinstance(value, str):
                    oceania.write(value + ", ")
                else:
                    for item in value:
                        oceania.write(item + ', ')
            oceania.write('\n')
    
    # close files
    africa.close()
    americas.close()
    asia.close()
    europe.close()
    oceania.close()