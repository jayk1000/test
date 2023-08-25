'''
Answer for Question 3 - Function

Name:Minjae Kim
SID:530009478
unikey:mkim9138

'''


def is_valid_length(name: str) -> bool:
    '''
    Checks if name has length between 1 and 9 (inclusive)
    Parameters:
        name:   str, a name
    Returns:
        Whether the length of the name is valid or not
    '''
    if len(name) >= 1 and len(name) < 10:
        return True
    else:
        return False


def is_valid_start(name: str) -> bool:
    '''
    Checks if name starts with an alphabet
    Parameters:
        name:   str, a name
    Returns:
        Whether the name starts with an alphabetical character or not
    '''
    if len(name) > 0 and str.isalpha(name[0]):
        return True
    else:
        return False


def is_one_word(name: str) -> bool:
    '''
    Checks if name is a single word
    Parameters:
        name:   str, a name
    Returns:
        Whether the name is one word or not
    '''
    if len(name) > 0 and name.find(' ') == -1:
        return True
    else:
        return False


def is_valid_name(name: str) -> bool:
    '''
    Checks if all of the previous requirements are met.
    '''
    return is_valid_length(name) and is_valid_start(name) and is_one_word(name)



