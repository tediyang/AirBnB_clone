#!/usr/bin/python3


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
        if len(line) == 0:
            print("** class name missing **")
            return

        database = storage.all() #---fetch the data saved--
        database_all = [database[obj_id].__str__() for obj_id in database.keys()]

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
                for data in database_all:
                    if command[1] in data:
                        print(data)

        else:
            print("Too much argument expected 2: Model and id")


if __name__ == '__main__':
	HBNBCommand().cmdloop()

