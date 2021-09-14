from gLearn import getClasses
from getpass import getpass
from pprint import pprint as pp

pinNumber = input("Enter PIN Number: ")
password = getpass("Enter Password: ")

classesList = getClasses(pinNumber, password)

pp(classesList)