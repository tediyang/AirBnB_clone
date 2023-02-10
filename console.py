#!/usr/bin/python3

# ------use cmd module ----------------

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
if __name__ == '__main__':
	HBNBCommand().cmdloop()
