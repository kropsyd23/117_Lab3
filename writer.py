"""
Write separate files given parameters
"""

import reader # for testing when ran as main

def write(text, file_name):
    ''' write text in a CSV file '''
    file = open(file_name, 'w')

    # write keys as the first line
    keys = list(text[0].keys())
    file.write(keys[0])
    for key in keys[1:]:
        file.write("," + key)
    file.write("\n")

    for line in text:
        # write the first element and then delete to set up commas
        file.write(line[keys[0]])
        del line[keys[0]]

        # loop through remaining information
        for key, value in line.items():
            # if value is a string, write it
            if isinstance(value, str):
                if value != "":
                    file.write("," + value)
                else:
                    file.write("," + '""')
            
            # if value is a list, loop through its elements to write them
            else:
                for item in value:
                    file.write("," + item)

        file.write("\n")

    file.close()

if __name__ == "__main__":
    # test using the .csv file with every country
    text = reader.read_country_file()
    write(text, "test.csv")
    