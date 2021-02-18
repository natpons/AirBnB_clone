#!/usr/bin/python3
"""Contains the entry point of the command interpreter"""
import cmd
import models
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter/Contains the functionality for the HBNB console"""
    prompt = '(hbnb) '
    classes = {'BaseModel': BaseModel, 'User': User,
               'State': State, 'City': City,
               'Amenity': Amenity, 'Place': Place, 'Review': Review}

    def do_create(self, line):
        """CREATES a new instance of BaseModel, SAVE IT to the JSON file and
        prints the id.
        Ex: $ create BaseModel"""
        if len(line) < 1:
            print("** class name missing **")
            return
        if line in HBNBCommand.classes:
            model = eval(line + "()")
            model.save()
            print(model.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """PRINTS the string representation of an instance based on the
        class name and id.
        Ex: $ show BaseModel 1234-1234-1234"""
        args = line.split(" ")
        all_models = storage.all()
        if len(args) < 1:
            print("**class name missing**")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key_name = args[0] + '.' + args[1]
        try:
            print(all_models[key_name])
        except:
            print("** no instance found **")

    def do_destroy(self, line):
        """DELETES an instance based on the class name and id
        (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234"""
        args = line.split(" ")
        all_models = storage.all()
        if len(args) < 1:
            print("**class name missing**")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key_name = args[0] + '.' + args[1]
        try:
            del(all_models[key_name])
        except:
            print("** no instance found **")

    def do_all(self, line):
        """ PRINTS all string representation of all instances based
        or not on the class name
        Ex: $ all BaseModel or $ all"""
        all_models = storage.all()
        if len(line) < 1:
            for model_id in all_models.keys():
                print("{}", format(all_models[model_id]))
        else:
            if line not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                for key, value in all_models.items():
                    if key.split(".")[0] == line:
                        print("{}", format(all_models[key]))

    def do_update(self, line):
        """Updates an instance based on the class name
        and id by adding or updating attribute
        Ex: $ update BaseModel 1234-1234-1234
        email "aibnb@holbertonschool.com
        Usage:update <class name> <id> <attribute name>
        "<attribute value>"""""
        args = line.split(" ")
        all_models = storage.all()
        if len(args) < 1:
            print("**class name missing**")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")

    def do_EOF(self):
        """EOF command to exit the program"""
        print()
        return True

    def do_quit(self):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Do none"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
