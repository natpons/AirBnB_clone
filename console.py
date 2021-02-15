#!/usr/bin/python3
"""Contains the entry point of the command interpreter"""
import cmd
import models
from models import storage
from models.base_model import BaseModel
from models.use import User

models_names = ['BaseModel', 'User']


class HBNBCommand(cmd.Cmd):
    """Command interpreter/Contains the functionality for the HBNB console"""
    prompt = '(hbnb) '

    def do_create(self, line):
        """CREATES a new instance of BaseModel, saves it to the JSON file and
        prints the id. Ex: $ create BaseModel
        - split input line, check len, eval
        - while:
        - setattr, storage: new + save, print id"""
        items = line.split(" ")
        if len(items) == 0:
            print("** class name missing **")
            return
        if items[1] in models_names:
            inst = eval(items[1] + "()")
            i = 1

            while i < len(items):
                p = items[i]
                list_p = p.split("=")
                p1 = list_p[0]
                p2 = list_p[1]
                setattr(inst, p1, p2)
                i = i + 1

                storage.new(inst)
                storage.save()
                print(inst.id)
        else:
            print("** class doesn't exist **")

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
