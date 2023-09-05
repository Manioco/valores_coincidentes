def read_files(bigger_file, smaller_file):
    """Recives two .txt files and returns a list of each one.

    Args:
        bigger_file (str(path/file_name.txt) or file_name.txt): Intended to be the bigger file, with all the items
        smaller_file (str(path/file_name.txt) or file_name.txt): Intended to be the smaller file, with a few items
        **Must to be each item in a new line
    Returns:
        List: two lists with the content of each file
    """

    with open(f'{bigger_file}', 'r') as f:
        bigger = f.readlines()
    
    with open(f'{smaller_file}', 'r') as f:
        smaller = f.readlines()
    
    return bigger, smaller


def match_items(bigger, smaller):
    """Recives two lists and returns a list with the matches and a list with the not matches.

    Args:
        bigger (List): Intended to be the bigger list, with all the items
        smaller (List): Intended to be the smaller list, with a few items

    Returns:
        _type_: Two lists, one with the matches and one with the not matches.
        The not matches list is intended to be the list of items that are not in the bigger list. 
    """
    
    not_match = []
    matches = []
    for line in smaller:
        if line in bigger:
            matches.append(line)
        else:
            not_match.append(line)
    return matches, not_match


def run():
    bigger = str(input('Enter the name of the bigger file: '))
    smaller = str(input('Enter the name of the smaller file: '))
    matches, not_match = match_items(read_files(bigger,smaller))
    print(matches)
    print(not_match)

# if __name__ == "__main__":
#    run()
