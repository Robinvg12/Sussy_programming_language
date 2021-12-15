from os import listdir, name, system
from os.path import isfile, join, realpath, dirname
from collections import defaultdict
def clear():
    command = 'clear'
    if name in ('nt', 'dos'): command = 'cls'
    system(command)
def editor(script, line_num):
    clear()
    print('Code editor: (type \'help\' for commands)')
    for i in range(0,len(script)):
        print(str(i+1)+'- '+script[i])
saves_path = dirname(realpath(__file__))+"\\saves"
filenames = [f for f in listdir(saves_path) if isfile(join(saves_path, f))]
clear()
script = defaultdict(list)
file_input = input('Do you want to (O)pen a file or make a (N)ew file? ')
if file_input.lower() == 'o':
    clear()
    print('Files:')
    for i in range(0, len(filenames)):
        if filenames[i].endswith('.txt'):
            print('- '+filenames[i][:len(filenames) - 6])
    open_file = input('\nWhat file do you want to open? ')
    if open_file+'.txt' in filenames: 
        clear()
        file = open(saves_path+'\\'+open_file+".txt")
        content = file.read()
        print(content)
elif file_input.lower() != 'n': exit()
print('Code editor: (type \'help\' for commands)')
line_num = 0
while line_num in range(0, 255):
    current_line = input(str(line_num+1)+'- ')
    if current_line == 'run':
        break
    elif current_line == 'help':
        clear()
        print('Commands:\n-run - to run the code\n-*line number* - to edit this line\n-save - to save the code')
        input('Press enter to continue...')
        line_num = line_num - 1
        editor(script, line_num)
    elif current_line.isnumeric():
        if int(current_line) in range(0, len(script)):
            editor(script, line_num)
            edit_input = input('*'+current_line+'- ')
            script[int(current_line)-1] = edit_input
        line_num = line_num - 1
        editor(script, line_num)
    elif current_line == 'save':
        save_name = input('Choose a file name (type \'exit\' to exit) ').replace(' ','_')
        if save_name in filenames:
            # vraag input yn
            # zo ja save in die file en ga terug naar editor
            # zo nee ga terug naar editor
        # als 'exit' ga terug naar editor
        # else save file
        
    else:
        script[line_num] = current_line
    line_num = line_num + 1





        
# print(script)
output = ''
for i in range(0, len(script)):
    output = output + script[i] + '\n'
print('\n'+output)

# [current_string[i:i+3] for i in range(0, len(current_string), 3)]