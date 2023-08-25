'''
Answer for Question 5. Kids' Friendly.

Author:Minjae Kim
SID:530009478
Unikey:mkim9138
'''
import os


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
    if is_valid_length(name) and is_valid_start(name) and is_one_word(name):
        x = True
    else:
        x = False
    return x and not is_profanity(name)


def is_profanity(word: str, database='/home/files/list.txt', records='/home/files/history.txt') -> bool:
    '''
    Checks if `word` is listed in the blacklist `database`.
    Parameters:
        word:     str,  word to check against database.
        database: str,  absolute directory to file containing list of bad words.
        records:  str,  absolute directory to file to record past offenses by player.
    Returns:
        result:   bool, status of check.
    '''
    try:
        with open(database) as profane_file:
            data_check = profane_file.read().splitlines()
    except FileNotFoundError:
        print('Check directory of database!')
        return False
    i = 0
    while i < len(data_check):
        insensitive = word.strip().lower()
        if word == data_check[i]:
            if os.path.isfile(records):
                with open(records, 'a') as record_history:
                    record_history.write(f"{insensitive}\n")
                return True
            else:
                with open(records, 'x') as record_history:
                    record_history.write(f"{insensitive}\n")
                return True
        i += 1
    return False


def count_occurrence(word: str, file_records="/home/files/history.txt", start_flag=True) -> int:
    '''
    Count the occurrences of `word` contained in file_records.
    Parameters:
        word:         str,  target word to count number of occurences.
        file_records: str,  absolute directory to file that contains past records.
        start_flag:   bool, set to False to count whole words. True to count words 
                            that start with.
    Returns:
        count:        int, total number of times `word` is found in the file.
    '''
    i = 0
    a = 0
    if type(word) != str:
        print('First argument must be a string object!')
        return i
    elif word == '':
        print('Must have at least one character in the string!')
        return i
    elif os.path.isfile(file_records):
        insensitive = word.strip().lower()
        with open(file_records) as fil:
            data_og = fil.read().lower().splitlines()
        if not start_flag:
            i += data_og.count(insensitive)
            return i
        else:
            # try:
            while a < len(data_og):
                if data_og[a] == '':
                    if a == len(data_og) - 1:
                        break
                    else:
                        a += 1
                        continue
                first_char = data_og[a][0]
                if insensitive[0] == first_char:
                    i += 1
                a += 1
            return i
    else:
        print('File records not found!')
        return i


def generate_name(word: str, src='/home/files/animals.txt', past='/home/files/names.txt') -> str:
    '''
    Select a word from file `src` in sequence depending on 
    the number of times word occurs.
    Parameters:
        word:     str, word to swap
        src:      str, absolute directory to file that contains safe in-game names
        past:     str, absolute directory to file that contains past names 
                       auto-generated
    Returns:
        new_name: str, the generated name to replace word
    '''
    if type(word) != str:
        print('First argument must be a string object!')
        new_name = 'Bob'
    elif word == '':
        print('Must have at least one character in the string!')
        new_name = 'Bob'
    elif os.path.isfile(src):
        insensitive = word.strip().lower()
        fil = open(src)
        same_char = []
        while True:
            animal = fil.readline().splitlines()
            if not animal:
                break
            first_char = animal[0][0]
            if insensitive[0] == first_char:
                same_char.append(animal[0])
        fil.close()
        # checking the number of times the first character of the profanity occurs in the names.txt
        num = 0
        counting = 0
        if os.path.isfile(past):
            while num < len(same_char):
                counting += count_occurrence(same_char[num], past, False)
                num += 1
            num2 = counting % len(same_char)
            new_name = same_char[num2]
        else:
            new_name = same_char[0]
    else:
        print('Source file is not found!')
        new_name = 'Bob'
    if os.path.isfile(past):
        with open(past, 'a') as f:
            f.write(f'{new_name}\n')
    else:
        with open(past, 'x') as f:
            f.write(f'{new_name}\n')
    return new_name


def main():
    while True:
        naming = input('Check name: ').strip().lower()
        if naming == 's':
            return
        else:
            if is_valid_name(naming):
                print(f'{naming} is a valid name!')
            else:
                naming = generate_name(naming)
                print(f'Your new name is: {naming}')

if __name__ == "__main__":
    main()
