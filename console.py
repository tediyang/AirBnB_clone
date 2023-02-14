#!/usr/bin/python3

"""
    cmd module to call subclasses.
"""
import cmd
from models.base_model import BaseModel
from models import storage
from models import *
import datetime as DT


class HBNBCommand(cmd.Cmd):
    """ class name to define all the functions """
    
    obj_dict = {"BaseModel": BaseModel, "User": user.User, "City": city.City, "State": state.State,
                "Review": review.Review, "Place": place.Place}

    prompt = '(hbnb) ' #-----to display-----

    def do_EOF(self, line):
        """ exit programme """
        return True

    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def help(self):
        """ Customized help command """

        print(' The progamme commands are:')
        print(' EOF exit line.')
        print(' quit exits command.')

    def make(self, model):
        new = model()
        new.save()
        return new.id
    
    def do_create(self, line):
        """
            Create a model using the provided class.
            if the class is not provided print ** class name missing **
            and if the class is provided doesn't exist
            ** class doesn't exist **
        """
        
        if len(line) == 0:
            print("** class name missing **")

        elif line not in HBNBCommand.obj_dict.keys():
            print("** class doesn't exist **")
            return

        else:
            for key, value in HBNBCommand.obj_dict.items():
                if line == key:
                    self.make(value)

    def do_show(self, line):
        """
            Fetch the data using the Model and id from
            the file storage.
        """
        command = line.split(" ")

        if len(line) == 0:
            print("** class name missing **")
        
        elif command[0] not in HBNBCommand.obj_dict.keys():
            print("** class doesn't exist **")
            
        elif len(command) == 1:
            print("** instance id missing **")

        elif len(command[1]) != 36:
            print("** no instance found **")

        elif len(command) == 2:
            for key, value in storage.all().items():
                loc = f"{command[0]}.{command[1]}"
                if loc in key:
                    print(value.__str__())
                    return
            print("** no instance found **")

        else:
            print("Too much argument expected 2: Model and id")

    def do_destroy(self, line):
        """ delete data using the model and id from
            the file storage
        """
        command = line.split(" ")
        
        if len(line) == 0:
            print("** class name missing **")

        elif command[0] not in HBNBCommand.obj_dict.keys():
            print("** class doesn't exist **")
            
        elif len(command) == 1:
            print("** instance id missing **")
        
        elif len(command[1]) != 36:
            print("** no instance found **")

        elif len(command) == 2:
            for key in storage.all().keys():
                loc = f"{command[0]}.{command[1]}"
                if loc in key:
                    del storage.all()[key]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, line):
        """ print all the data in the storage file. """
        database = storage.all()
        database_all = [database[obj].__str__() for obj in database.keys()]

        if len(line) == 0:
            print(database_all)
        
        else:
            if line not in HBNBCommand.obj_dict.keys():
                print("** class doesn't exist **")
                return
            print(database_all)

    def do_update(self, line):
        """ update the data in the storage file. """

        command = line.split(" ")
        
        if len(line) == 0:
            print("** class name missing **")

        elif command[0] not in HBNBCommand.obj_dict.keys():
            print("** class doesn't exist **")
            
        elif len(command) == 1:
            print("** instance id missing **")
            
        elif len(command[1]) != 36:
            print("** no instance found **")

        elif len(command) == 2:      
            for key in storage.all().keys():
                loc = f"{command[0]}.{command[1]}"
                if loc in key:
                    print("** attribute name missing **")
                    return
            print("** no instance found **")

        elif len(command) == 3:         
            for key in storage.all().keys():
                loc = f"{command[0]}.{command[1]}"
                if loc in key:
                    print("** value missing **")
                    return
            print("** no instance found **")
            
        elif len(command) == 4:
            for key, value in storage.all().items():
                loc = f"{command[0]}.{command[1]}"
                if loc in key:
                    value.__dict__[command[2]] = command[3]
                    value.__dict__["updated_at"] = DT.datetime.now()
                    storage.save()
                    return
            print("** no instance found **")  

        else:
            print("Can't update more than one.")
                

if __name__ == '__main__':
	HBNBCommand().cmdloop()