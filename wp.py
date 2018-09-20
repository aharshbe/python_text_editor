#!/usr/bin/python
import random
import os
from os import system
from time import sleep
from pathlib import Path

class file_make:
	def __init__(self):
		pass

	def chooser():
		while(1):
			system('clear')
			print("\nWelcome to File Maker built in Python")
			print("\nWhat would you like to do?")
			print("1. Create a new file")
			print("2. View files")
			print("3. Delete a file")
			print("4. Rename file")
			print("5. Edit file")
			print("")
			print("q. Type 'q' to quit.\n")
			choice = input()

			if (choice == str(1)):
				file_make.create_new_file()
			elif (choice == str(2)):
				system('clear')
				file_make.show_files_edit()
				sleep(2)
			elif (choice == str(3)):
				system('clear')
				file_make.show_files()
				filename = input("\nEnter file to delete: ")
				file_make.delete_file(filename)
				sleep(2)
			elif (choice == str(4)):
				print("\nRenameing a file...")
				sleep(2)
			elif (choice == str(5)):
				file_make.show_files_edit()
			elif (choice == str("q")):
				print("Happy day...")
				sleep(.3)
				system('clear')
				quit()
			else:
				print("Choose an option above.")
				file_make.chooser()

	def delete_file(filename):
		print("Are you sure you want to remove:", filename, "?")
		choice = input()
		if (choice == 'y'):
			os.remove(filename)
			print("file, "+filename+" removed.")
			sleep(1)
		elif (choice == 'n'):
			file_make.chooser()
		else:
			print("Choose either (y/n).")
			file_make.delete_file(filename)

	def create_file_name():
		system('clear')
		
		choice = input("Name file? ")

		y = ['y', 'Y', 'Yes', 'YES', 'yes']
		n = ['n', 'N', 'No', 'NO', 'no']

		if choice in y:
			file_name = input("File Name: ") + ".txt"
		elif choice in n:
			file_name = "file_" + str(random.randint(1, 1001)) + ".txt"
		else:
			print("Either (y/n)")
			file_make.create_file_name()
		return file_name

	def show_files_edit():
		system('clear')
		print("Available files:\n")
		
		files_to_edit = file_make.show_files()
		choice = input("\nPick a file number: ")
		
		for index, filename in files_to_edit.items():
			if (int(choice) == index):
				file_make.view_file(filename)
				file_make.edit_file(filename)
		file_make.show_files_edit()

	def edit_file(filename):
		system('clear')
		answer = input("Want to edit file? ")
		if (answer == 'y'):
			file = open(filename, "r")
			system('clear')
			print(file.read(), end='')
			file.close()
			file = open(filename, "a+")
			file_make.add_content(file)
			file.close()
		elif (answer == 'n'):
			file_make.chooser()
		else:
			print("Please enter either (y/n)")
			file_make.edit_file()
		return file

	def view_file(filename):
		print("Opening file `", filename, "`...")
		file = open(filename, "r")
		system('clear')
		print(file.read(), "\n\n")
		file_make.view_timer()
		file.close()
		
	def view_timer():
		print("Done viewing?")
		choice = input()
		if (choice == 'y'):
			pass
		elif (choice == 'n'):
			sleep(4)
			file_make.view_file(filename)
		else:
			print("Enter either (y/n)")
			file_make.view_timer()
	
	def add_content(file):
		while (1):
			content = input()
			file.write(content + "\n")

	def create_new_file():
		
		filename = file_make.create_file_name()
		
		if (not filename):
			print("Error creating file. Exiting program...")
			sleep(2)
			quit()
		
		my_file = Path("./"+filename)
		if (not my_file.is_file()):
			print("Creating new file...\n")
			file = open(filename, "w+")
			sleep(1)
			system('clear')
		else:
			file_make.view_file(filename)
			file = file_make.edit_file(filename)

		file_make.add_content(file)
		file.close()

		print("\nFile: '", filename, "' created.")
		sleep(1)

	def show_files():
		i = 1
		all_files = {}
		files = [f for f in os.listdir('.') if os.path.isfile(f)]
		for f in files:
			if ".txt" not in f:
				continue
			else:
				print(str(i)+'.', f)
				all_files[i] = f
				i += 1
		return all_files

file_make.chooser()

	