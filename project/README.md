# Password Generator

#### Video Demo: https://drive.google.com/file/d/1ETI7fbBeF9EVg68HELmVz04ZoM3w1pO_/view?usp=drive_link

#### Description:

The Password Generator is a Python program that allows users to generate random passwords of a specified length. It provides options for including lowercase letters, uppercase letters, digits, and symbols in the generated password. The program also includes a functionality to assess the strength of the generated password based on its length and character types.

## Files

- `project.py`: This file contains the main function and other utility functions for generating and printing passwords. It prompts the user for input, including the length of the password and the character types to include. It calls the `generate_password` function to generate the password based on the user's choices and then uses the `print_password` function to print the generated password to the console. It also includes the `assess_strength` function to calculate the strength rating of the password.

- `test_project.py`: This file contains unit tests for the functions in `project.py`. It includes test cases for the `generate_password`, `print_password`, and `assess_strength` functions to ensure they produce the expected results. It also tests the overall functionality of the program by simulating user inputs and capturing the printed output.

## Design Choices

- The `generate_password` function uses the `random.choice` function to randomly select characters from the chosen character types and concatenate them to form the password. The `string` module is used to define the available character types, such as lowercase letters, uppercase letters, digits, and symbols.

- The program prompts the user for input using the `input` function and converts the user's choices to boolean values (`True` or `False`) based on their responses. This allows for dynamic customization of the password generation process.

- The `assess_strength` function calculates the strength rating of the generated password based on its length and character types. It assigns a rating of "Weak" if the length is less than 8 characters, "Medium" if the length is 8 or more characters, and "Strong" if the length is 12 or more characters.

- The `print_password` function prints the generated password to the console, and the `print_strength` function prints the strength rating of the password. Both functions ensure that the password and strength are only printed if they are not `None`.

Feel free to explore the code and customize it according to your needs. Have fun generating secure passwords!
