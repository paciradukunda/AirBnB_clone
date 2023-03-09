from models import storage
from models.base_model import BaseModel

import cmd


class HBNBCommand(cmd.Cmd):
    intro = "Welcome to MyShell. Type help or ? to list commands.\n"
    prompt = "(hbnb) "
    list_of_class = ["BaseModel"]
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
        if arg not in self.list_of_class:
            print("** class doesn't exist **")
            return None
        if arg == "BaseModel":
            obj = BaseModel()
            obj.save()
            print(obj.id)
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """Shows objects
        args:
            arg[0]: class
            arg[1]: id of object
        """
        arg = arg.split()
        if len(arg) == 2:
            if arg[0] in self.list_of_class:
                key = arg[0] + "." + arg[1]
                try:
                    value = self.obj_dict[key]
                    new_obj = BaseModel(**value)
                    print(new_obj)
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
            if arg[0] in self.list_of_class:
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

    def do_all(self, arg=None):
        """Prints list of string representation of objects
        args:
            arg: classname
        """
        all_list = []
        if arg not in self.list_of_class or len(self.obj_dict) == 0:
            print("** class doesn't exist **")
            return None
        for key, value in self.obj_dict.items():
            new_ob = BaseModel(**value)
            all_list.append(str(new_ob))
        print(all_list)

    def do_update(self, *args):
        """Updates given object
        args:
            arg[0]: class name
            arg[1]: id
            arg[2]: attribute name
            arg[3]: attribute value
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
