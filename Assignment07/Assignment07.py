# ------------------------------------------------- #
# Title: Assignment 7
# Description: Examples of pickling and error handling
# ChangeLog: (Who, When, What)
# Sam Ewald,08.22.2023,Created Script
# ------------------------------------------------- #
import pickle  # This imports code from another code file!

# Data -------------------------------------------- #
strFileName = 'AppData.dat'
lstCustomer = []

# Processing -------------------------------------- #
def save_data_to_file(file_name, list_of_data):
    objFile = open(file_name, "ab")
    pickle.dump(list_of_data, objFile)
    objFile.close()

def read_data_from_file(file_name):
    file = open(file_name, "rb")
    list_of_data = pickle.load(file)
    file.close()
    return list_of_data

# Presentation ------------------------------------ #
# TODO: Get ID and NAME From user, then store it in a list object
intId = input("Enter an Id: ")
strName = str(input("Enter a name: "))
lstCustomer = [intId, strName]

try:
    if intId.isnumeric() == False:
        raise Exception('Use numbers for the ID.')
    if strName.isnumeric() == True:
        raise Exception('Don\'t use numbers for your name.')

except Exception as e:
    print("There was an error:")
    print(e, e.__doc__, type(e), sep='\n')


# TODO: store the list object into a binary file
save_data_to_file(strFileName, lstCustomer)

# TODO: Read the data from the file into a new list object and display the contents
print("User ID: ")
print(read_data_from_file(strFileName)[0], '\n')
print("Name: ")
print(read_data_from_file(strFileName)[1])

input()