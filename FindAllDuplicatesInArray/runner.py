from os import dup


def find_all_duplicates_in_array(array):
    duplicates_map = {}

    for element in array:
        if element in duplicates_map.keys():
            duplicates_map[element] = True
        else:
            duplicates_map[element] = False

    return list(filter(duplicates_map.get, duplicates_map))

if __name__ == "__main__":
    array = [3,4,9,4,0,-1,3]
    duplicates = find_all_duplicates_in_array(array)
    print(duplicates)