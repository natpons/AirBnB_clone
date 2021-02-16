#!/usr/bin/python3
"""Contains the entry point of the command interpreter"""
import cmd
import models
from models import storage
from models.base_model import BaseModel
from models.user import User

models_names = ['BaseModel', 'User']


class HBNBCommand(cmd.Cmd):
    """Command interpreter/Contains the functionality for the HBNB console"""
    prompt = '(hbnb) '

    def do_create(self, line):
        """CREATES a new instance of BaseModel, saves it to the JSON file and
        prints the id. Ex: $ create BaseModel
        - split input line, eval, save, id"""
        args = line.split(" ")
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] in models_names:
            model = eval(args[0] + "()")
            storage.save()
            print(model.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """PRINTS the string representation of an instance based on the
        class name and id.
        Ex: $ show BaseModel 1234-1234-1234"""

    def do_destroy(self, line):
        """DELETES an instance based on the class name and id
        (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234"""
        args = line.split()

    def do_EOF(self, line):
        """EOF command to exit the program"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Do none"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
