from gLearn import getClasses
from getpass import getpass
from pprint import pprint

pinNumber = input("Enter PIN Number: ")
password = getpass("Enter Password: ")

classList = getClasses(pinNumber, password)

pprint(classList)