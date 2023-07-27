# Import needed libraries
import string
import sys

# Declare variables
str_list = ""
nws_num = ""

# Try to open Input file, given as 1st command line parameter, read the file contents and handle possible exception
try:
    with open(sys.argv[1], "r") as file_i:
       data = file_i.readlines()
except IndexError:
    print("Invalid or missing Input filename argument, please check that the there are no typos!")
    exit(0)

# Try to open Output file, given as 2nd command line parameter and handle possible exception
try:
    file_o = open(sys.argv[2], "w")
except IndexError:
    print("Missing output filename argument, please check that the there are no typos!")
    exit(0)

# Manipulate the Input file contents
for c in data:
# Variables
    result = 0
    result2 = 0
    end_result = []
# Separate the content lines based on new line
    split_lines = c.split("\n")
# Remove trailing whitespaces
    c.rstrip()
# Display line contents on screen without string apostrophes
    print(split_lines[0])
# Handle each lines values separately
    for x in c:
# Separate line values based on the space
        num = c.split(" ")
# Calculate the 1st 2 values multiples and cast the string to integer
        while(result < int(num[2])):
            result = result + int(num[0])
# Place the calculation value into end list, if 1st calculation value is below the lines 3rd value
            if(result < int(num[2])):
                end_result.append(result)
        while(result2 < int(num[2])):
            result2 = result2 + int(num[1])
# Place the calculation value into end list, if 2nd calculation value is below the lines 3rd value
            if(result2 < int(num[2])):
                end_result.append(result2)
# Reorder the end list to acending order
        end_result.sort()
# Remove the list brackets & commas and cast the integer value as string using space as separator
    str_list = " ".join(map(str,end_result))
# Display the end string on screen
    print(str_list)
# Remove the trailing new line from 3rd value
    nws_num = num[2].rstrip()
# Form the Output file printout and write the line into Output file
    file_o.write(nws_num + ':' + str_list + '\n')   
# Close the Input & Output files   
file_i.close()
file_o.close()