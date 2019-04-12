#!/usr/local/bin/python3

import random
import os
from os import system
from time import sleep
from pathlib import Path
import datetime
import findType
import sys

class file_make:
	def __init__(self):
		pass

	def chooser(flag):
		while(1):
			system('clear')
			print("\nWelcome to File Maker built in Python")
			print("\nWhat would you like to do?")
			print("1. Create a new file")
			print("2. View files")
			print("3. Delete a file or files")
			print("4. Rename file")
			print("5. Edit file")
			print("6. Compile/Run file")
			print("")
			print("q. Type 'q' to quit.\n")
			if (not flag):
				choice = input()
			else:
				choice = flag

			if (choice == str(1) or choice == 'create'):
				file_make.create_new_file() # Create new file
			elif (choice == str(2) or choice == 'view'):
				system('clear')
				file_make.show_files_edit(0) # View files
				sleep(.3)
			elif (choice == str(3) or choice == 'delete'):
				system('clear')
				file_make.delete_file(0) # Delete a file
				sleep(2)
			elif (choice == str(4) or choice == 'mv'):
				print("\nRe-naming a file...") # Raname a file
				sleep(2)
			elif (choice == str(5) or choice == 'edit'):
				system('clear')
				file_make.show_files_edit(1)  # Edit a file

			elif (choice == str(6) or choice == 'run'):
				system('clear')
				file_make.compile_files(0)  # Compile/Run file

			elif (choice == str("q")):
				system('clear')
				quit()
			else:
				print("Choose an option above.")
				file_make.chooser(0)

	def delete_file(filename):
		if filename:
			os.remove(filename)
			print("file, "+filename+" removed.")
			sleep(.2)
			file_make.chooser(0)

		print("Files in current directory:\n")

		val = file_make.show_files()

		if val == 1:
			system('clear')
			print("\n No files in current directory.\n")
			sleep(4)
			file_make.chooser(0)
		else:
			filename = input("\nEnter file name (including extension) to delete.\nExample 1 (single): file_996.txt\nExample 2 (multiple): hello.c hello hello.sh file_2.txt\n\nFile name: ")
			files = filename.split(" ")
			tr = file_make.isFile(files, val)
			if (tr):
				file_make.delete_file(0)
			print("\nAre you sure you want to remove: "+filename+"?")
			choice = input()
			if (choice == 'y'):
				try:
					for i in files:
						os.remove(i)
						print("file, "+i+" removed.")
						sleep(.1)
					sleep(.3)

				except:
					system('clear')
					print("!! File deletion error. Try again (may have misspelled file name.)\n")
					file_make.delete_file(0)
			elif (choice == 'n'):
				file_make.chooser(0)
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
			file_make.chooser(0)
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
			file_make.chooser(0)
		else:
			print("Please enter either (y/n)")
			file_make.edit_file(filename, 1)
		file.close()
		return file

	def view_file(filename):
		print("Opening file `", filename, "`...")
		file = open(filename, "r")
		system('clear')
		print(file.read(), "\n<END OF FILE>")
		file.close()
		file_make.view_timer(filename)

	def view_timer(filename):
		print("Done viewing? (y/n)")
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
			if (content == ":s:"):
				print("\nsaving...")
				file.close()
				file_make.chooser(0)
				break
			elif (content == ":sv:"):
				print("\nsaving and viewing...")
				file.close()
				file_make.view_file(filename)
				break
			elif (content == ":sc:"):
				print("\nsaving and running...")
				file.close()
				file_make.compile_files(filename)
				break
			elif (content == ":d:"):
				file_make.delete_file(filename)
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
			comment = findType.checkType(filename)
			file.write(comment+str(datetime.datetime.now())+"\n\n")
			sleep(.5)
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

	def compile_files(filename):
		if filename:
			findType.compileType(filename)
			file_make.chooser(0)
		print("Files in current directory:\n")

		val = file_make.show_files()

		if val == 1:
			system('clear')
			print("\n No files in current directory.\n")
			sleep(4)
			file_make.chooser(0)
		else:
			filename = input("\nEnter file name (including extension) to execute.\nExample: file_996.txt\n\nFile name: ")
			tr = file_make.isFile(filename, val)
			if (tr):
				file_make.compile_files(0)
			try:
				findType.compileType(filename)
			except:
				print("!! File compile error. Try again (may have misspelled file name.)\n")
				file_make.compile_files(0)
			file_make.chooser(0)

	def isFile(filename, files):
		if (type(filename) == str):
			if (filename not in files.values()):
				print("Make sure to type the name of a file that exists. Try again.")
				sleep(2)
				system('clear')
				return 1
			else:
				return 0
		val = 0
		for i in filename:
			if (i not in files.values()):
				print("Make sure to type the name of a file that exists. Try again.")
				sleep(2)
				system('clear')
				val = 1
		return val

if len(sys.argv) > 1:
	file_make.chooser(sys.argv[1])
else:
	file_make.chooser(0)
