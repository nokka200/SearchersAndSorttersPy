
def linearSearch(listToSearch: list, target)-> bool:
    
    for item in listToSearch:
        if (target == item):
            return True
    return False