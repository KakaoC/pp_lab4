import os
import csv
import get_way


def write(name_class: str, number: str) -> None:
    '''
    запись в csv-файл(абсолютный путь/относительный путь/тег класса)
    '''
    with open("dataset.csv", "a", newline='', encoding='utf8') as file:
        printer = csv.writer(file, delimiter=";")
        printer.writerow(
            [os.path.abspath(get_way.create_download_relative_way(name_class, number)),
             get_way.create_download_relative_way(name_class, number),
             name_class]
        )


def to_annotation(folderpath: str) -> None:
    '''
    создание csv-файла
    поочерёдная запись класса zebra в файл-аннотацию из папки download_data
    '''
    with open("dataset.csv", "w", newline='') as file:
        printer = csv.writer(file, delimiter=";", )
        printer.writerow(["The Absolute Way", "Relative Way", "Class"])
    for i in os.listdir(f"{folderpath}/zebra"):
        way = f"{folderpath}/zebra/{i}"
        if os.path.isfile(way):
            write("zebra", i)
    for i in os.listdir(f"{folderpath}/bay horse"):
        way = f"{folderpath}/bay horse/{i}"
        if os.path.isfile(way):
            write("bay horse", i)


if __name__ == "__main__":
    path = "dataset/download_data"
    if os.path.exists(path):
        pass
    else:
        print(os.getcwd() + path + " - no have")
    to_annotation(path)
