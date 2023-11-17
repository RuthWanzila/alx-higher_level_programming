#!/usr/bin/python3
"""
Base module that contain the first class Base
"""
import json
import csv
import turtle


class Base:
    """This class will be the base of all other classes in this project."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the Base instance."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Serialize a list of dictionaries to a JSON formatted string."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Serialize a list of objects to JSON and save it to a file.

        Args:
            list_objs: a list of instances that inherit from Base
        """
        filename = f"{cls.__name__}.json"
        list_dict = [obj.to_dictionary() for obj in list_objs]
        if list_objs else []
        with open(filename, mode='w', encoding='utf-8') as f:
            f.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """Deserialize a JSON string to a list of dictionaries."""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with attributes already set using a dictionary.

        Args:
            dictionary: a double pointer to a dictionary

        Returns:
            An instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Load instances from a JSON file.

        Returns:
            A list of instances
        """
        file_name = f"{cls.__name__}.json"
        try:
            with open(file_name, mode="r", encoding="utf-8") as f:
                list_instance = []
                list_dict = cls.from_json_string(f.read())
                for dic in list_dict:
                    new_inst = cls.create(**dic)
                    list_instance.append(new_inst)
                return list_instance
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serialize a list of objects to CSV and save it to a file.

        Args:
            list_objs: a list of instances that inherit from Base
        """
        file_name = f"{cls.__name__}.csv"
        with open(file_name, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=cls.get_csv_fieldnames())
            writer.writeheader()
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Load instances from a CSV file.

        Returns:
            A list of instances
        """
        file_name = f"{cls.__name__}.csv"
        list_instance = []
        with open(file_name, 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                instance = cls.create(**row)
                list_instance.append(instance)
        return list_instance

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draw rectangles and squares using the turtle module.

        Args:
            list_rectangles: a list of Rectangle instances
            list_squares: a list of Square instances
        """
        tur = turtle.Turtle()
        tur.color('yellow')
        tur.pensize(5)
        tur.speed(3)

        for rect in list_rectangles:
            tur.penup()
            tur.goto(rect.x, rect.y)
            tur.pendown()
            tur.forward(rect.width)
            tur.right(90)
            tur.forward(rect.height)
            tur.right(90)
            tur.forward(rect.width)
            tur.right(90)
            tur.forward(rect.height)
            tur.right(90)

        tur.color('red')

        for square in list_squares:
            tur.penup()
            tur.goto(square.x, square.y)
            tur.pendown()
            for _ in range(4):
                tur.forward(square.size)
                tur.right(90)

        turtle.done()
