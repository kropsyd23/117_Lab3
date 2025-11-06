"""
Write separate files given parameters
"""

import reader # for testing when ran as main

def write_line(file, line):
    ''' add information to a file '''
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

def write(text, key, index, file_name):
    ''' write information about a specified key if it matches a specific index '''
    
    # open a writing file
    file_variable = open(file_name, 'w')
    # loop through every line in the text
    for line in text:

        # add to that file if index matches specified index
        if line[key] == index:
            write_line(file_variable, line)

    # close file
    file_variable.close()

if __name__ == "__main__":
    text = reader.read_country_file()
    write(text, "region", "Africa", "africa.csv")
    