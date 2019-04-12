#!/usr/local/bin/python3

import random
import os
from os import system
from time import sleep
from pathlib import Path
import datetime
import findType

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
			print("6. Compile/Run file")
			print("")
			print("q. Type 'q' to quit.\n")
			choice = input()

			if (choice == str(1)):
				file_make.create_new_file() # Create new file
			elif (choice == str(2)):
				system('clear')
				file_make.show_files_edit(0) # View files
				sleep(.3)
			elif (choice == str(3)):
				system('clear')
				file_make.delete_file() # Delete a file
				sleep(2)
			elif (choice == str(4)):
				print("\nRe-naming a file...") # Raname a file
				sleep(2)
			elif (choice == str(5)):
				system('clear')
				file_make.show_files_edit(1)  # Edit a file

			elif (choice == str(6)):
				system('clear')
				file_make.compile_files()  # Compile/Run file

			elif (choice == str("q")):
				print("Happy day...")
				sleep(.3)
				system('clear')
				quit()
			else:
				print("Choose an option above.")
				file_make.chooser()

	def delete_file():
		print("Files in current directory:\n")

		val = file_make.show_files()

		if val == 1:
			system('clear')
			print("\n No files in current directory.\n")
			sleep(4)
			file_make.chooser()
		else:
			filename = input("\nEnter file name (including extension) to delete.\nExample: file_996.txt\n\nFile name: ")
			print("\nAre you sure you want to remove: "+filename+"?")
			choice = input()
			if (choice == 'y'):
				try:
					files = filename.split(" ")
					for i in files:
						os.remove(i)
						print("file, "+i+" removed.")
						sleep(.1)
					sleep(.3)
				except:
					system('clear')
					print("!! File deletion error. Try again (may have misspelled file name.)\n")
					file_make.delete_file()
			elif (choice == 'n'):
				file_make.chooser()
			else:
				print("Choose either (y/n).")
				file_make.delete_file(filename)

	def create_file_name():
		system('clear')
		file_name = input("File Name: ")
		if not file_name or file_name == " ":
			file_name = "file_" + str(random.randint(1, 1001)) + ".txt"
		return file_name

	def create_new_question():
		choice = input("Want to create a new file? ")
		if (choice == 'y'):
			file_make.create_new_file()
		elif (choice == 'n'):
			file_make.chooser()
		else:
			print("Please enter either (y/n)")
			file_make.create_new_question()

	def show_files_edit(flag):

		if (not flag):
			print("Available files:\n")
			files_to_edit = file_make.show_files()

			if (files_to_edit == 1):
				system('clear')
				print("\n No files in current directory.\n")
				file_make.create_new_question()
			else:
				choice = input("\nPick a file number: ")

			for index, filename in files_to_edit.items():
				if (int(choice) == index):
					file_make.view_file(filename)
		else:
			print("Available files:\n")
			files_to_edit = file_make.show_files()

			if (files_to_edit == 1):
				system('clear')
				print("\n No files in current directory.\n")
				file_make.create_new_question()
			else:
				choice = input("\nPick a file number: ")

			for index, filename in files_to_edit.items():
				if (int(choice) == index):
					file_make.edit_file(filename, 0)

	def edit_file(filename, flag):
		system('clear')
		if (flag):
			answer = input("Want to edit file? ")
		else:
			answer = 'y'

		if (answer == 'y'):
			file = open(filename, "r")
			system('clear')
			file_make.add_content(file, filename, 1)
		elif (answer == 'n'):
			file_make.chooser()
		else:
			print("Please enter either (y/n)")
			file_make.edit_file(filename, 1)
		file.close()
		return file

	def view_file(filename):
		print("Opening file `", filename, "`...")
		file = open(filename, "r")
		system('clear')
		print(file.read(), "\n\n")
		file.close()
		file_make.view_timer(filename)

	def view_timer(filename):
		print("Done viewing?")
		choice = input()
		if (choice == 'y'):
			return
		elif (choice == 'n'):
			sleep(2)
			file_make.view_file(filename)
		else:
			print("Enter either (y/n)")
			file_make.view_timer(filename)

	def add_content(file, filename, flag):

		if (not flag):
			print("Editing "+filename+" ...\n")
			print("**To save file, type ':save:' on a new line.**\n")
		else:
			print("Editing "+filename+" ...\n")
			print(file.read(), end='')
			file.close()
			file = open(filename, "a+")
		while (1):
			content = input()
			if (content == ":save:"):
				print("\nsaving...")
				sleep(.2)
				file.close()
				file_make.chooser()
				break
			elif (content == ":save+view:"):
				print("\nsaving and viewing...")
				sleep(.2)
				file.close()
				file_make.view_file(filename)
				break
			else:
				file.write(content + "\n")

	def create_new_file():

		filename = file_make.create_file_name()

		if (not filename):
			print("Error creating file. Exiting program...\n")
			sleep(2)
			quit()

		my_file = Path("./"+filename)
		if (not my_file.is_file()):
			file = open(filename, "w+")
			# Check to see if file was named or not e.g., if it's a program or text file
			if not "file_" in filename:
				comment = findType.checkType(filename)
			else:
				comment = ""
			file.write(comment+str(datetime.datetime.now())+"\n\n")
			sleep(1)
			system('clear')
		else:
			file_make.view_file(filename)
			file = file_make.edit_file(filename, 1)
		print(datetime.datetime.now(), "\n")
		file_make.add_content(file, filename, 0)

		print("\nFile: '", filename, "' created.")
		sleep(1)

	def show_files():
		i = 0
		all_files = {}
		files = [f for f in os.listdir('.') if os.path.isfile(f)]
		for f in files:
			print(str(i)+'.', f)
			all_files[i] = f
			i += 1
		if (not i):
			return 1
		return all_files

	def compile_files():
		print("Files in current directory:\n")

		val = file_make.show_files()

		if val == 1:
			system('clear')
			print("\n No files in current directory.\n")
			sleep(4)
			file_make.chooser()
		else:

			filename = input("\nEnter file name (including extension) to execute.\nExample: file_996.txt\n\nFile name: ")
			try:
				findType.compileType(filename)
			except:
				print("!! File compile error. Try again (may have misspelled file name.)\n")
				file_make.compile_files()
			file_make.chooser()

file_make.chooser()
