#!/usr/bin/python3

# ------use cmd module ----------------


import models
import json
import cmd
""" cmd module to call subclasses """

class HBNBCommand(cmd.Cmd):
	""" class name to define all the functions """
	
	prompt = '(hbnb)' #-----to display-----
	

	def do_EOF(self, line):
		"""" exit programme """
		return True

	def do_quit(self, line):
		""" same as do_EOF """
		return True
	def help(self):
		""" Customized help command """

		print(' The progamme commands are:')
		print(' EOF exit line.')
		print(' quit exits command.')

	def do_create(BaseModel, id):
		""" creates a new instance of BaseModel"""
		if BaseModel is None:
			print("**class name missing**")
			return

new_object = BaseModel(id) #class instance

with open(f"{BaseModel}.json", "w") as B:
	json.dump(new_object.__dic__, B)
		
	print(new_object.id)



#def do_show(
#		else:
#			print("**class doesn't exist**")
#			return
	




if __name__ == '__main__':
	HBNBCommand().cmdloop()
