# Title
Module 07: Binary Files and Extensions

## Introduction

In this assignment, we worked with writing to and reading from binary files, as well as working with and creating custom exceptions.

## Binary Files
Following the module 07 lab, I defined a pair of functions that would dump data to a binary file using Pickle, as well as read that data into a list:

###### Working with binary files:
![Working with Binary Files](https://github.com/sbe-fop-p-2023/IntroPython_Mod07/blob/main/assignment7-pictures/Screenshot%202023-08-23%20221110.png "Working with Binary Files")

## Custom Exceptions

To try some error handling, I created a pair of custom exceptions to test if the input ID was an integer and the name was not.
Unfortunately, these didn’t work while the inputs were called with an ‘int’ and and ‘str’, so I had to leave the input options open in order for the error handling to work:
###### ID input error:
![ID input error](https://github.com/sbe-fop-p-2023/IntroPython_Mod07/blob/main/assignment7-pictures/Screenshot%202023-08-23%20215424.png "ID input error")

##### Name input error:
![Name input error](https://github.com/sbe-fop-p-2023/IntroPython_Mod07/blob/main/assignment7-pictures/Screenshot%202023-08-23%20215512.png "Name input error")

However, using the input types requested by the errors did allow the script to work as intended:
##### Working in PyCharm:
![Working in PyCharm](https://github.com/sbe-fop-p-2023/IntroPython_Mod07/blob/main/assignment7-pictures/Screenshot%202023-08-23%20220503.png "Working in PyCharm")

##### Working in command shell:
![Working in command shell](https://github.com/sbe-fop-p-2023/IntroPython_Mod07/blob/main/assignment7-pictures/Screenshot%202023-08-23%20220840.png "Working in command shell")

## Conclusion
Another limitation of this script is that it only appeared to save the first inputs entered to the dat file—subsquent name/ID inputs would return the first one entered until a new dat file was created.
