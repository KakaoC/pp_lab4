import os
import shutil
import csv
import random
from iterator import Iterator
import get_way


def create_annotation(name_class: str, number: int) -> None:
    '''
    создаёт csv файл-аннотацию(абсолютный путь/относительный путь/тег класса)
    '''
    with open("dataset_number.csv", "a", newline='', encoding='utf8') as file:
        printer = csv.writer(file, delimiter=";")
        printer.writerow(
            [os.path.abspath(get_way.create_number_relative_way(number)),
             get_way.create_number_relative_way(number),
             name_class])


def create_copy_of_dataset(name_class: str) -> None:
    '''
    создаёт копии в новой папке
    '''
    iterat = Iterator("dataset.csv", name_class)
    for elem in iterat:
        if elem != None:
            if os.path.isfile(str(elem)) == True:
                new_number = random.randint(0, 10001)
                while os.path.isfile(get_way.create_number_relative_way(new_number)) == True:
                    new_number = random.randint(0, 10001)
                shutil.copyfile(
                    str(elem), get_way.create_number_relative_way(new_number))
                create_annotation(name_class, new_number)


def start_copy():
    if not os.path.isdir("dataset/dataset_number"):
        os.mkdir("dataset/dataset_number")
    else:
        shutil.rmtree("dataset/dataset_number")
        os.mkdir("dataset/dataset_number")

    with open("dataset_number.csv", "w", newline='') as file:
        printer = csv.writer(file, delimiter=";")
        printer.writerow(["The Absolute Way", "Relative Way", "Class"])

    create_copy_of_dataset("zebra")
    create_copy_of_dataset("bay horse")


if __name__ == "__main__":
    start_copy()
