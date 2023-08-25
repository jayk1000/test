# import sys
# sex = input()
# i = 0
# print(sys.argv)
# print(len(sys.argv))
# while i < len(sys.argv):
#     if sys.argv[len(sys.argv) - 1] == chr(123):
#         print('found')
#     i += 1
# run = len(sys.argv)
# print(f'run: {run}')
# d = [1, 2, 3, 4]
# file_name,  n_str, d1 = d[0:]
# def storing():
#     i = 0
#     while i < len(d):
#         a = d[i]
#         yield a
#         i += 1
# def main():
#         print(next(storing()))
#         print(next(storing()))
import time
import datetime
import os

# This will print out today's  date and time
print(time.asctime())

# Display date and time on 4 Feb 2022, 10:00:00
day = 4
month = 2
year = 2022
hour = 10
minute = '00'
second = 'no'
# start = datetime.datetime(year, month, day, hour, minute, second)
# sample = start.timetuple()
i = 0
process_text = ''
paths = [minute, second, 'day', 'night', 'day']
num = ['dye', 'night', 'day', 'night', 'day']
while i < 5:
    process_text +=  f'{paths[i]} is found!\n'
    i += 1
print(os.path.abspath('/home/master/') )
    

print(paths+num)
print(os.path.isabs('/home/animals.txt'))
try:
    print("Statement 1")
    print("Statement 2")
    x = 1 / 0
    print("Statement 3")
except ZeroDivisionError:
    print("An error occurred: division by zero")
        

# if __name__ == '__main__':
#     main()

    
