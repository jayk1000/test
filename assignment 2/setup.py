'''
Write your solution for 6. PIAT: Check Setup here.

Author:Minjae Kim
SID:530009478
Unikey:mkim9138
'''
from datetime import datetime
import os
from os import listdir
from os.path import isdir, isfile
import sys
import shutil


def logging(logs: list, date: str, time_: str) -> None:
    '''
    Logging function uses a list of strings to write previous output into a
    log file.
    Parameters:
        logs: list, output from verification/installation in the form of list of
                    strings to write to logging file.
        date: str,  a string representing the date to generate the necessary
                    directory date must be in the format YYYY-MM-DD as seen in
                    the specs (ex: 2023-Mar-03 for March 3rd, 2023).
        time: str,  a string representing the time to generate the log file
                    time must be in the format HH_MM_SS as seen in the specs
                    (ex: 14_31_27 for 14:31:27).
    '''
    date_dir = os.path.join('/home/logs/', date)
    os.makedirs(date_dir, exist_ok=True)
    time_file = os.path.join(os.path.abspath(date_dir), f'{time_}.txt')
    with open(time_file, 'w') as opening:
        i = 0
        while i < len(logs):
            opening.write(f'{logs[i]}\n')
            i += 1


def get_paths(master: str) -> tuple:
    '''
    It extracts the paths of directories and files written in config file.
    Parameters:
        master:    str,  a string representing the absolute path to the master directory.
    Return:
        num_dir:    int, an integer representing the number of directories written in config file.
        dir_loc:    list, a list storing the paths of the directories written in config file.
        files_loc:  list, a list storing the paths of the files written in config file.
    '''
    with open(os.path.join(master, 'config.txt')) as reading:
        paths = reading.read().splitlines()
    i = 0
    num_dir = 0
    dir_loc = []
    files_loc = []
    while i < len(paths):
        if paths[i].startswith('/') and paths[i].endswith('/'):
            num_dir += 1
            dir_loc.append(paths[i])
            potential_files = paths[i+1:]
            a = 0
            while a < len(potential_files):
                if potential_files[a].startswith('/'):
                    break
                if potential_files[a].startswith('./') and not potential_files[a].endswith('/'):
                    files_loc.append(os.path.join(dir_loc[num_dir-1], potential_files[a].lstrip('./')).strip())
                a += 1
        i += 1
    return (num_dir, dir_loc, files_loc)


def compare_files(file: str, master_file: str) -> tuple:
    '''
    It reads the file and mater file and compare them and stores them. 
    It stops reading if the content is different.
    Parameters:
        file:    str,  a string representing the absolute path to the file in /home/.
        master_file:    str,  a string representing the absolute path 
        to the file in the master directory.
    Return:
        same_status
        content_print:    list, a list storing the lines of the file
        master_print:  list, a list storing the lines of the files written 
        in config file.
    '''
    content_print = []
    master_print = []
    same_status = True
    with open(file) as f, open(master_file) as f1:
        content = True
        master_content = True
        while content or master_content:
            content = f.readline().strip('\n')
            master_content = f1.readline().strip('\n')
            content_print.append(content)
            master_print.append(master_content)
            if content != master_content:
                same_status = False
                break
    return same_status, (content_print, master_print)


def verification(master: str, timestamp: str) -> list:
    '''
    Verification makes sure all files and directories listed in the config file
    are present and match the contents of the master files. 
    Parameters:
        master:    str,  a string representing the absolute path to the master directory.
        timestamp: str,  a string representing the time to insert into the output.
    Returns:
        output:    list, a list of strings generated from the verification process.
    '''
    try:
        output = []
        output.append(f'{timestamp} Start verification process.')
        output.append(f'{timestamp} Extracting paths in configuration file.')
        num_dir, dir_loc, files_loc = get_paths(master)
        output.append(f'Total directories to check: {num_dir}')
        output.append(f'{timestamp} Checking if directories exists.')
        num = 0
        placeholder = True
        while num < len(dir_loc) and placeholder:
            if isdir(dir_loc[num]):
                output.append(f'{dir_loc[num]} is found!')
            else:
                output.append(f'{dir_loc[num]} is NOT found!')
                placeholder = False
            num += 1
        if not placeholder:
            output.append('Abnormalities detected.')
            return output
        output.append(f'{timestamp} Extracting files in configuration file.')
        num = 0
        while num < len(files_loc):
            output.append(f'File to check: {files_loc[num]}')
            num += 1
        output.append(f'Total files to check: {len(files_loc)}')
        output.append(f'{timestamp} Checking if files exists.')
        num = 0
        placeholder = True
        while num < len(files_loc) and placeholder:
            if isfile(files_loc[num]):
                output.append(f'{files_loc[num]} found!')
            else:
                output.append(f'{files_loc[num]} NOT found!')
                placeholder = False
            num += 1
        if not placeholder:
            output.append('Abnormalities detected.')
            return output
        output.append(f'{timestamp} Check contents with master copy.')
        allmaster = all_master_files(master)
        locating, origin_path, destination = config_master_paths(files_loc, allmaster, master)
        i = 0
        placeholder = True
        while i < len(files_loc) and placeholder:
            # indexError raised due to difference in length of files_loc and origin_path if master copy does not exist
            same_status, content = compare_files(files_loc[i], origin_path[i])
            if same_status:
                output.append(f'{files_loc[i]} is same as {origin_path[i]}: True')
            else:
                a = 0
                while a < len(content):
                    output.append(f'File name: {files_loc[i]}, {content[0][a]}, {content[1][a]}')
                    a += 1
                placeholder = False
            i += 1
        if placeholder:
            output.append(f'{timestamp}  Verification complete.')
        else:
            output.append('Abnormalities detected...')
    except Exception:
        output.append('Abnormalities detected...')
    finally:
        return output


def all_master_files(master):
    master_dir = sorted(listdir(master))
    i = 0
    allmaster = []
    while i < len(master_dir):
        if isdir(os.path.join(master, master_dir[i])):
            master_list = sorted(listdir(os.path.join(master, master_dir[i])))
            a = 0
            while a < len(master_list):
                master_files = os.path.join(master, master_dir[i], master_list[a])
                allmaster.append(master_files)
                a += 1
        i += 1
    return allmaster


def config_master_paths(files_loc: list, allmaster: list, master: str, status: bool = False) -> tuple :
    i = 0
    locating = []
    origin_path =[]
    destination = []
    while i < len(files_loc):
        dir_path, file_name = os.path.split(files_loc[i])
        locating.append(file_name)
        config_filepath = files_loc[i].replace(os.path.dirname(dir_path), '')
        a = 0
        while a < len(allmaster):
            master_path, master_name = os.path.split(allmaster[a])
            master_filepath = allmaster[a].replace(os.path.dirname(master_path), '')
            if config_filepath == master_filepath:
                origin_path.append(f'{allmaster[a]}')
                destination.append(f'{files_loc[i]}')
                if status:
                    shutil.copy(allmaster[a], files_loc[i])
                break
            a += 1
        if a == len(allmaster):
            if status:
                filepath_without = config_filepath[1:]
                not_found_path = os.path.join(master, filepath_without)
                origin_path.append(f'{not_found_path} is not found.')
                break
        i += 1
    return locating, origin_path, destination


def installation(master: str, timestamp: str) -> list:
    '''
    Installation copies all required master files into the addresses listed by
    the config file.
    Parameters:
        master:    str,  a string representing the absolute path to the master directory.
        timestamp: str,  a string representing the time to insert into the output.
    Returns:
        output:    list, a list of strings generated from the installation process.
    '''
    try:
        output = []
        # open config file, read it and put the lines into the list
        output.append(f'{timestamp} Start installation process.')
        num_dir, dir_loc, files_loc = get_paths(master)
        output.append(f'{timestamp} Extracting paths in configuration file.')
        output.append(f'Total directories to create: {num_dir}')
        output.append(f'{timestamp} Create new directories.')
        num = 0
        while num < len(dir_loc):
            if isdir(dir_loc[num]):
                output.append(f'{dir_loc[num]} exists. Skip directory creation.')
            else:
                os.mkdir(dir_loc[num])
                output.append(f'{dir_loc[num]} is created successfully.')
            num += 1
        allmaster = all_master_files(master)
        output.append(f'{timestamp} Extracting paths of all files in {master}.')
        i = 0
        while i < len(allmaster):
            output.append(f'Found: {allmaster[i]}')
            i += 1
        output.append(f'{timestamp}  Create new files.')
        num = 0
        while num < len(files_loc):
            with open(files_loc[num], 'w') as opening:
                opening.write('')
            output.append(f'Creating file: {files_loc[num]}')
            num += 1
        locating, origin_path, destination = config_master_paths(files_loc, allmaster, master, status=True)
        output.append(f'{timestamp} Copying files.')
        i = 0
        while i < len(locating):
            output.append(f'Locating: {locating[i]}')
            output.append(f'Original path: {origin_path[i]}')
            # indexError appears here
            output.append(f'Destination path: {destination[i]}')
            i += 1
        output.append(f'{timestamp}  Installation complete.')
    except Exception:
        output.append('Installation error...')
    finally:
        return output


def config_check(master: str) -> bool:
    '''
    Checks if config file is valid or not.
    Parameters:
        master:    str,  a string representing the absolute 
        path to the master directory.
    Return:
        valid:    bool, a boolean representing if config file is valid or not
    '''
    with open(os.path.join(master, 'config.txt')) as reading:
        paths = reading.read().splitlines()
    i = 0
    valid = True
    while i < len(paths) and valid:
        if paths[i].startswith('/') and paths[i].endswith('/'):
            a = 0
            while a < len(paths[i]):
                if paths[i][a] == '.':
                    valid = False
                    break
                a += 1
            potential_files = paths[i+1:]
            a = 0
            while a < len(potential_files):
                if potential_files[a].startswith('/'):
                    break
                elif potential_files[a].startswith('./') and not potential_files[a].endswith('/'):
                    a += 1
                    continue
                else:
                    valid = False
                    break
        else:
            if paths[i].startswith('./') and not paths[i].endswith('/'):
                a = 0
                while a <= i:
                    if paths[i-a].startswith('/') and paths[i-a].endswith('/'):
                        j = 0
                        while j < len(paths[i-a]):
                            if paths[i-a][j] == '.':
                                valid = False
                                break
                            j += 1
                        break
                    a += 1
                if a > i:
                    valid = False
            else:
                valid = False
        i += 1
    return valid


def main(master: str, flags: str, timestamp: str):
    '''
    Ideally, all your print statements would be in this function. However, this is
    not a requirement.
    Parameters:
        master:    str, a string representing the absolute path to the master directory.
        flags:     str, a string representing the specified flags, if no flag is given
                        through the command line, flags will be an empty string.
        timestamp: str, a string representing the time to insert into the output.
                    in the format: DD MMM YYYY HH:MM:DD , ex: 10 Apr 2023 12:44:17
    '''
    printing = []
    if not (master.startswith('/') and master.endswith('/')):
        print('Invalid master directory.', file=sys.stderr)
    elif not (os.path.isdir(master) and isfile(os.path.join(master, 'config.txt'))):
        print('Invalid master directory.', file=sys.stderr)
    else:
        valid = config_check(master)
        if not valid:
            print('Invalid master directory.', file=sys.stderr)
        else:
            time_date = datetime.strptime(timestamp, "%d %b %Y %H:%M:%S")
            date = time_date.strftime("%Y-%b-%d").strip()
            time_ = time_date.strftime("%H_%M_%S").strip()
            if flags == '':
                printing = installation(master, timestamp)
                logging(printing, date, time_)
            elif flags.startswith('-'):
                if len(flags) == 2:
                    if flags[1] == 'i':
                        printing = installation(master, timestamp)
                    elif flags[1] == 'v':
                        printing = verification(master, timestamp)
                    elif flags[1] == 'l':
                        print('Invalid flag. Log can only run with install or verify.', file=sys.stderr)
                    else:
                        print("Invalid flag. Character must be a combination of 'v' or 'i' and 'l'.", file=sys.stderr)
                elif len(flags) > 2:
                    if flags[1] == flags[2]:
                        print('Invalid flag. Each character must be unique.', file=sys.stderr)
                        return
                    if flags == '-iv' or flags == '-vi':
                        print('Invalid flag. Choose verify or install process not both.', file=sys.stderr)
                        return
                    elif flags == '-vl' or flags == '-lv':
                        printing = verification(master, timestamp)
                    elif flags == '-il' or flags == '-li':
                        printing = installation(master, timestamp)
                    else:
                        print("Invalid flag. Character must be a combination of 'v' or 'i' and 'l'", file=sys.stderr)
                        return
                    logging(printing, date, time_)
            else:
                print("Invalid flag. Flag must start with '-'.", file=sys.stderr)
            if printing:
                i = 0
                while i < len(printing):
                    print(printing[i])
                    i += 1


if __name__ == "__main__":
    current_time = datetime.now()
    timestamp = current_time.strftime("%d %b %Y %H:%M:%S")
    if len(sys.argv) >= 3:
        main(sys.argv[1], sys.argv[2], timestamp)
    elif len(sys.argv) == 2:
        flags = ''
        main(sys.argv[1], flags, timestamp)
    elif len(sys.argv) < 2:
        print('Insufficient arguments.', file=sys.stderr)