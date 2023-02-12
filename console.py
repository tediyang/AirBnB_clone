#!/usr/bin/python3

"""
    cmd module to call subclasses.
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ class name to define all the functions """

    prompt = '(hbnb) ' #-----to display-----

    def do_EOF(self, line):
        """ exit programme """
        return True

    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    def help(self):
        """ Customized help command """

        print(' The progamme commands are:')
        print(' EOF exit line.')
        print(' quit exits command.')

    def do_create(self, line):
        """
            Create a model using the provided class.
            if the class is not provided print ** class name missing **
            and if the class is provided doesn't exist
            ** class doesn't exist **
        """
        if len(line) == 0:
            print("** class name missing **")
            return

        if len(line) > 0 and line != "BaseModel":
            print("** class doesn't exist **")
            return

        else:
            new = BaseModel()
            new.save()
            print(new.id)

    def do_show(self, line):
        """ Fetch the data using the Model and id from
            the file storage.
        """

        if len(line) == 0:
            print("** class name missing **")
            return

        command = line.split(" ")

        if len(command) == 1:
            if command[0] != "BaseModel":
                print("** class doesn't exist **")
                return
            print("** instance id missing **")
        
        elif len(command) == 2:
            if command[0] != "BaseModel":
                print("** class doesn't exist **")
                return
            
            if len(command[1]) != 36:
                print("** no instance found **")
            
            else:
                for key, value in storage.all().items():
                    if command[1] in key:
                        print(value.__str__())
                        return
                print("** no instance found **")

        else:
            print("Too much argument expected 2: Model and id")

    def do_destroy(self, line):
        """ delete data using the model and id from
            the file storage
        """
        
        if len(line) == 0:
            print("** class name missing **")
            return

        command = line.split(" ")

        if len(command) == 1:
            if command[0] != "BaseModel":
                print("** class doesn't exist **")
                return
            print("** instance id missing **")
        
        elif len(command) == 2:
            if command[0] != "BaseModel":
                print("** class doesn't exist **")
                return
            
            if len(command[1]) != 36:
                print("** no instance found **")
            
            else:    
                for key in storage.all().keys():
                    if command[1] in key:
                        del storage.all()[key]
                        storage.save()
                        return
                print("** no instance found **")


if __name__ == '__main__':
	HBNBCommand().cmdloop()