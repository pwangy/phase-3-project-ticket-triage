# lib/cli.py
import ipdb
from helpers import (
	exit_program,
	helper_1
)


def main():
	while True:
		menu()
		choice = input("> ")
		if choice == "0":
			exit_program()
		elif choice == "1":
			helper_1()
		#elif choice == "2":
		#			helper_2()
		#elif choice == "3":
		#	while True:
		#		menu2()
		#		choice = input("> ")
		#		if choice == "0":
		#			exit_program()
		#		elif choice == "3":
		#			helper_3()
		#		else:
		#			print("Invalid choice")
		else:
			print("Invalid choice")

def menu():
	print("Please select an option:")
	print("0. Exit the program")
	print("1. Some useful function")
	print("2. Some useful function")
#	print("3. New Menu")

#def menu2():
#	print("Please select an option:")
#	print("0. Exit the program")
#	print("3. Some useful function")


if __name__ == "__main__":
random.seed(0)
	main()
