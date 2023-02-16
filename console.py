#!/usr/bin/python3

"""
    cmd module to call subclasses.
"""

import cmd
from models.base_model import BaseModel
from models import storage
from models import *
import datetime as DT
import re, ast


class HBNBCommand(cmd.Cmd):
    """ class name to define all the functions """
    
    obj_dict = {"BaseModel": BaseModel, "User": user.User, "City": city.City, "State": state.State,
                "Review": review.Review, "Place": place.Place, "Amenity": amenity.Amenity}

    prompt = '(hbnb) ' #-----to display-----

    def do_EOF(self, arg):
        """ exit programme """
        return True

    def do_quit(self, arg):
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
    
    def do_create(self, arg):
        """
            Create a model using the provided class.
            if the class is not provided print ** class name missing **
            and if the class is provided doesn't exist
            ** class doesn't exist **
        """
        
        if len(arg) == 0:
            print("** class name missing **")

        elif arg not in HBNBCommand.obj_dict.keys():
            print("** class doesn't exist **")
            return

        else:
            for key, value in HBNBCommand.obj_dict.items():
                if arg == key:
                    print(self.make(value))
                    return


    def do_show(self, arg):
        """
            Fetch the data using the Model and id from
            the file storage.
        """
        command = arg.split(" ")

        if len(arg) == 0:
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

    def do_destroy(self, arg):
        """ delete data using the model and id from
            the file storage
        """
        command = arg.split(" ")
        
        if len(arg) == 0:
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

    def do_all(self, arg):
        """ print all the data in the storage file. """
        database = storage.all()
        database_all = [database[obj].__str__() for obj in database.keys()]

        if len(arg) == 0:
            print(database_all)
        
        else:
            if arg not in HBNBCommand.obj_dict.keys():
                print("** class doesn't exist **")
                return
            else:
                print([database[obj].__str__() for obj in database.keys() if arg in obj])

    def do_update(self, arg):
        """ update the data in the storage file. """

        command = arg.split(" ")
        
        if len(arg) == 0:
            print("** class name missing **")

        elif command[0] not in HBNBCommand.obj_dict.keys():
            print("** class doesn't exist **")
            
        elif len(command) == 1 or command[1] == "":
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


    def count(self, arg):
        database = storage.all()
        print(len([database[obj].__str__() for obj in database.keys() if arg in obj]))

                
    def default(self, arg):
        """
            If a known command is not entered then this function
            will execute. This creates an alternative way of using
            the console.
        """

        H_cmds = {"all": self.do_all, "count": self.count, 
                  "show": self.do_show, "destroy": self.do_destroy}

        obj_ext = re.search(r'[\w]*', arg)
        obj_name = obj_ext if obj_ext is None else obj_ext.group(0)
        if len(obj_name) == 0 or obj_name is None:
            print("** class doesn't exist **")
            return

        com = re.search(r'(?<=\.)[\w]*', arg)
        command = com if com is None else com.group(0)

        if command in ["all", "count"]:
            H_cmds[command](obj_name)
            return

        else:
            obj_id_ext = re.search(r'(?<=")[\w.+%@-]+(?=")', arg)
            obj_id = obj_id_ext if obj_id_ext is None else obj_id_ext.group(0)

            if command in ["show", "destroy"]:
                if obj_id is None:
                    H_cmds[command](obj_name)
                    return
                H_cmds[command](obj_name + " " + obj_id)

            elif command == "update":
                obj_dict_ext = re.search(r'{(.*?)}', arg)
                obj_dict = obj_dict_ext if obj_dict_ext is None else obj_dict_ext.group(0)
                if obj_dict is None:
                    details_list = re.findall(r'(?<=")[\w.+%@-]+(?=")', arg)
                    detail = " ".join(details_list)
                    self.do_update(obj_name + " " + detail)
                
                else:
                    try:
                        
                        obj_dict_conv = ast.literal_eval(obj_dict) \
                            if len(obj_dict) > 2 else ast.literal_eval(None)
                        for key, value in obj_dict_conv.items():
                            self.do_update(obj_name + " " + obj_id + " " + key + " " + str(value))

                    except ValueError or TypeError:
                        print('Wrong dictionary, "Format: {key: value, ...}"')

            else:
                print("invalid command")


if __name__ == '__main__':
	HBNBCommand().cmdloop()