#!/usr/bin/python3
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.Review import Review
from models.state import State
from models.user import User

import cmd


class HBNBCommand(cmd.Cmd):
    intro = "Welcome to MyShell. Type help or ? to list commands.\n"
    prompt = "(hbnb) "
    dict_of_class = {
        "Amenity": Amenity,
        "BaseModel": BaseModel,
        "City": City,
        "Place": Place,
        "Review": Review,
        "State": State,
        "User": User,
    }
    obj_dict = storage.all()

    def do_EOF(self, arg):
        """Exits the command line"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program \n\n"""
        return True

    def do_help(self, arg: str) -> bool | None:
        """Prints all available commands"""
        return super().do_help(arg)

    def emptyline(self) -> None:
        """Handles empty entry"""
        return None

    """ My own functionarity """

    def do_create(self, arg):
        """Creates an object of given class"""
        if arg in self.dict_of_class:
            obj_cls = self.dict_of_class[arg]
            obj = obj_cls()
            obj.save()
            print(obj.id)
        else:
            print("** class doesn't exist **")
        if len(arg) == 0:
            print("** class name missing **")

    def do_show(self, arg):
        """Shows objects
        args:
            arg[0]: class
            arg[1]: id of object
        """
        arg = arg.split()
        if len(arg) == 2:
            if arg[0] in self.dict_of_class:
                key = arg[0] + "." + arg[1]
                try:
                    print(self.obj_dict[key])
                except KeyError:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        elif len(arg) == 1:
            if len(arg[0]) < 20:
                print("** instance id missing **")
            else:
                print("** class name missing **")
        else:
            print("** class name missing **")

    def do_destroy(self, arg):
        """Deletes objects
        args:
            arg[0]: class
            arg[1]: id of object
        """
        arg = arg.split()
        if len(arg) == 2:
            if arg[0] in self.dict_of_class:
                key = arg[0] + "." + arg[1]
                try:
                    self.obj_dict.pop(key)
                    storage.save()
                except KeyError:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")

        elif len(arg) == 1:
            if len(arg[0]) < 20:
                print("** instance id missing **")
            else:
                print("** class name missing **")
        else:
            print("** class name missing **")

    def do_all(self, arg):
        """Prints list of string representation of objects
        args:
            arg: classname
        """
        all_obj = []
        if arg in self.dict_of_class or len(arg) == 0:
            for _, value in self.obj_dict.items():
                all_obj.append(str(value))
            print(all_obj)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates given object
        args:
            arg[0]: class name
            arg[1]: id
            arg[2]: attribute name
            arg[3]: attribute value
        """
        arg = arg.split()
        if len(arg) == 4:
            if arg[0] in self.dict_of_class:
                key = arg[0] + "." + arg[1]
                try:
                    obj = self.obj_dict[key]
                    obj.__setattr__(arg[2], arg[3].strip('"'))
                    obj.save()
                except KeyError:
                    print("** no instance found **")
                except AttributeError:
                    print("** attribute doesn't exist")
            else:
                print("** class doesn't exist **")
        elif len(arg) == 2:
            print("** attribute name missing **")
        elif len(arg) == 3:
            print("** value missing **")
        elif len(arg) == 1:
            if len(arg[0]) < 20:
                print("** instance id missing **")
            else:
                print("** class name missing **")
        else:
            print("** class name missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
