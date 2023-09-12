#Author: Jesús Ponte
# 12/09/2023

# 1. Un palíndromo, también llamado palíndromo, palíndroma o palindroma, es una palabra, o
# frase que se lee igual en un sentido que en otro. Ejemplo ANA se puede leer al derecho y al
# revés y significa lo mismo.
# ● Punto extra - No puede usar ciclos
# ● Punto extra - No más de 5 líneas de código


# Considerando que el txt a evaluar es un String, tomaremos en cuenta el texto como valor.
# We use glob to be able to run unit tests from txt files
import glob

# Desc: Function used to return True or False if the string read from the file is a palindrome.
# Params: Text: String
def check_palindrome(text):
    text_filtered = text.replace(' ', '').lower()
    return print('Is palindrome: ' + str(text_filtered == text_filtered[::-1]))

def unit_testing(directory, file_exp):
    files = glob.glob(path + file_exp)
    # For loop to iterate through each of the unit tests
    for i, file in enumerate(files):
        text = open(file, 'r')
        text_string = text.read()
        text.close()
        file_name = 'unit_test_' + str(i + 1) + '_result'
        with open(file_name, 'w') as f:
            f.write(str(check_palindrome(text_string)))


#Base directory for unit tests
path = 'C:/Users/PC/PycharmProjects/gbm_ejercicio1'
#Specify the document path expression
file_exp = '/unit_test_*.txt'

#Example one to run without unit tests
#check_palindrome('aba')

#Run unit tests
unit_testing(path, file_exp)





