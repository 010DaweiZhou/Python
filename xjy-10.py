import easygui as gui

gui.msgbox('hello ,welcom~')

msg = 'what do you want to learn?'
title = 'A little game'
choices = [1,2,3,4]

choice = gui.choicebox(msg, title, choices)
gui.msgbox('you choice ' + str(choice), 'result')
msg = 'do you wangt to play game ?'
title = 'please choice'

if gui.ccbox(msg, title):
    pass
else:
    exit(0)

