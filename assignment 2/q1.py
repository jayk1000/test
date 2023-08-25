'''
We will use the art by Joan Stark as the logo:
           ____()()
          /      @@
jgs `~~~~~\_;m__m._>o

Answer for Question 1 - Game Title

Name:Minjae Kim
SID:530009478
unikey:mkim9138

'''
author = 'An INFO1110/COMP9001 Student'
title = 'Mousehunt'
logo_line1 = '____()()'
logo_line2 = '/      @@'
logo_line3 = '`~~~~~\\_;m__m._>o'
x = ' '
logo = (f'\n{x*7}{logo_line1}\n{x*6}{logo_line2}\n{logo_line3}')
credits = f'''
Inspired by Mousehunt© Hitgrab
Programmer - {author}
Mice art - Joan Stark'''


def introdution():
    '''
    Prints the title, logo and credits
    '''
    print(title)
    print(logo)
    print(credits)


