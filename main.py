"""
License: Apache
Organization: UNIR
"""

import os
import sys

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False
DEFAULT_ASCENDING = True


def sort_list(items, ascending=True):
    if not isinstance(items, list):
        raise RuntimeError(f"Cannot sort {type(items)}")

    return sorted(items, reverse=(not ascending))


def remove_duplicates_from_list(items):
    return list(set(items))


def parse_cli_args(args):
    if len(args) != 4:
        print("Se debe indicar el fichero como primer argumento")
        print("El segundo argumento indica si se quieren eliminar duplicados (yes|no)")
        print("El tercer argumento indica el orden (asc|desc)")
        sys.exit(1)

    filename = args[1]

    remove_duplicates_arg = args[2].lower()
    if remove_duplicates_arg not in ("yes", "no"):
        print("El segundo argumento debe ser yes o no")
        sys.exit(1)
    remove_duplicates = remove_duplicates_arg == "yes"

    sort_order_arg = args[3].lower()
    if sort_order_arg not in ("asc", "desc"):
        print("El tercer argumento debe ser asc o desc")
        sys.exit(1)
    ascending = sort_order_arg == "asc"

    return filename, remove_duplicates, ascending


if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    ascending_order = DEFAULT_ASCENDING
    filename, remove_duplicates, ascending_order = parse_cli_args(sys.argv)
    if len(sys.argv) == 4:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
    else:
        print("You must provide the file as the first argument")
        print("The second argument indicates whether duplicates should be removed")
        sys.exit(1)

    print(f"The words will be read from file {filename}")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"The file {filename} does not exist")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)

    print(sort_list(word_list, ascending_order))
