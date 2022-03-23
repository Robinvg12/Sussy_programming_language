from os import listdir, name, system
from os.path import isfile, join, realpath, dirname
from collections import defaultdict
from re import findall
saves_path = dirname(realpath(__file__))+"\\saves"
def clear():
    command = 'clear'
    if name in ('nt', 'dos'): command = 'cls'
    system(command)
def editor(script, line_num, current_file):
    clear()
    print('-'+current_file+'\nCode editor:\n')
    for i in range(0,len(script)-1):
        print(str(i+1)+'- '+script[i])
def save(script, save_name):
    output = ''
    for i in range(0, len(script)):
        output = output + script[i] + '\n'
    with open(saves_path+'\\'+save_name+'.txt', 'w') as f:
        f.write(output)
def run_old(script):
    pos_ran = []
    run_list = defaultdict(list)
    for i in range(-256, 255):
        run_list[i] = 0
    pos = 0
    sample = '''
uuu SuS 
suS SuS SuS
suS SuS SuS
suS SuS SuS
suS SuS SuS
suS SuS SuS
suS SuS SuS
suS SuS SuS'''
    code_list = []
    # print(script)
    for i in range(0, len(script)):
        code_list = code_list + [i] + findall('...?', script[i].replace(' ',''))
    # code_list = findall('...',code)
    # print(code_list)
    code_line_num = 0
    for i in range(0, len(code_list)):
        if isinstance(code_list[i], int):
            code_line_num = code_list[i]
        elif code_list[i] == 'suS':
            pos = pos + 1
        elif code_list[i] == 'Sus':
            pos = pos - 1
        elif code_list[i] == 'SUS':
            print('test')
        elif code_list[i] == 'SuS':
            run_list[pos] = run_list[pos] + 1
        elif code_list[i] == 'SUs':
            run_list[pos] = run_list[pos] - 1
        elif code_list[i] == 'uuu':
            run_list[pos] = 0
        else:
            editor(script, code_line_num, current_file)
            print('\nThe program has an error in line '+str(code_line_num+1)+':\n'+str(code_line_num+1)+'- '+script[code_line_num])
            input('\nPress enter to go back to editor...')
            return

        if pos not in pos_ran:
            pos_ran = pos_ran + [pos]

    # print(run_list)

    # print(min(pos_ran))
    # print(max(pos_ran))
    # print('-----')
    clear()
    for p in range(min(pos_ran), max(pos_ran)+1):
        print(str(p)+'- '+str(run_list[p]))

    input('\nYour program has succesfully been executed.\nPress enter to go back to editor...')

def run(script):
    print(script)
    program = [0] * 10
    currentPos = 0
    programInputRaw = join(script)
    programInput = findall('.', programInputRaw)
    output = ''
    inputPos = 0
    while inputPos < len(programInput):
        # print('line:', inputPos, programInput[inputPos])
        if programInput[inputPos] == '0':
            program[currentPos] = 0
        elif programInput[inputPos] == '>':
            currentPos += 1
        elif programInput[inputPos] == '<':
            currentPos -= 1
        elif programInput[inputPos] == '+':
            program[currentPos] += 1
        elif programInput[inputPos] == '-':
            program[currentPos] -= 1
        elif programInput[inputPos] == '.':
            if program[currentPos] == 0:
                program[currentPos] = ord(input())
            else:
                output = output + chr(program[currentPos])
        elif programInput[inputPos] == '[':
            if program[currentPos] == 0:
                move = True
                while move:
                    inputPos += 1
                    # print(programInput[inputPos])
                    if programInput[inputPos] == ']':
                        move = False

        elif programInput[inputPos] == ']':
            print(program)
            # print(currentPos, program[currentPos])
            if program[currentPos] != 0:
                move = True
                while move:
                    inputPos -= 1
                    # print(programInput[inputPos])
                    if programInput[inputPos] == '[':
                        move = False
        inputPos += 1
    print(output)
    print(program)
filenames = [f for f in listdir(saves_path) if isfile(join(saves_path, f))]
clear()
script = ['']
file_input = input('Do you want to (O)pen a file or make a (N)ew file? ')
if file_input.lower() == 'o':
    clear()
    print('Files:')
    for i in range(0, len(filenames)):
        if filenames[i].endswith('.txt'):
            print('- '+filenames[i][:len(filenames[i]) - 4])
    open_file = input('\nWhat file do you want to open? ')
    if open_file+'.txt' in filenames: 
        file = open(saves_path+'\\'+open_file+".txt")
        content = file.read()
        content_byline = content.splitlines()
        num_lines = len(content_byline)
        for i in range(0,num_lines):
            script[i] = content_byline[i]
        print(script)
elif file_input.lower() == 'n':
    line_num = 0
    current_file = 'New File'
else:
    exit()
# print('Code editor: (type \'help\' for commands)')
recently_saved = True
while line_num in range(0, 255):
    editor(script, line_num, current_file)
    current_line = input(str(line_num+1)+'- ')
    if current_line == 'run':
        run(script)
        script.pop()
        line_num -= 1
        editor(script, line_num, current_file)
    elif current_line == 'help':
        clear()
        print('Commands:\n-run - to run the code\n-*line number* - to edit this line\n-save - to save the code')
        input('Press enter to continue...')
        script.pop()
        line_num -= 1
        editor(script, line_num, current_file)
    elif current_line.isnumeric():
        if int(current_line) in range(0, len(script)):
            editor(script, line_num, current_file)
            edit_input = input('*'+current_line+'- ')
            script[int(current_line)-1] = edit_input
        script.pop()
        line_num -= 1
        editor(script, line_num, current_file)
    elif current_line == 'save':
        editor(script, line_num, current_file)
        save_name = input('Choose a file name (type \'exit\' to exit) ').replace(' ','_')
        if save_name+'.txt' in filenames:
            yorn_correct = False
            while not yorn_correct:
                # vraag input yn
                yorn = input('The savefile \''+save_name+'\' allready exists. Do you want to overwrite? (y/n)')
                if yorn == 'y':
                    # zo ja save in die file en ga terug naar editor
                    save(script, save_name)
                    script.pop()
                    line_num -= 1
                    editor(script, line_num, current_file)
                    yorn_correct = True
                    recently_saved = True
                elif yorn == 'n':
                    # zo nee ga terug naar editor
                    yorn_correct = True
                    script.pop()
                    line_num -= 1
        
        # als 'exit' ga terug naar editor
        elif save_name == 'exit':
            script.pop()
            line_num -= 1
            editor(script, line_num, current_file)
        # else save file
        else:
            save(script, save_name)
            script.pop()
            line_num -= 1
            editor(script, line_num, current_file)
            recently_saved = True
    elif current_line == 'exit':
        if not recently_saved:
            # yorn_correct = False
            # while not yorn_correct:
            #     # vraag input yn
            #     yorn = input('You have not saved recently, do you want to save? (y/n)')
            #     if yorn == 'y':
            #         # zo ja save in die file en ga terug naar editor
            #         save(script, save_name)
            #         script.pop()
            #         line_num -= 1
            #         editor(script, line_num, current_file)
            #         yorn_correct = True
            #         recently_saved = True
            #     elif yorn == 'n':
            #         # zo nee ga terug naar editor
            #         yorn_correct = True
            #         script.pop()
            #         line_num -= 1




                save_name = input('Choose a file name (type \'exit\' to exit) ').replace(' ','_')
                if save_name+'.txt' in filenames:
                    yorn_correct = False
                    while not yorn_correct:
                        # vraag input yn
                        yorn = input('The savefile \''+save_name+'\' allready exists. Do you want to overwrite? (y/n)')
                        if yorn == 'y':
                            # zo ja save in die file en ga terug naar editor
                            save(script, save_name)
                            script.pop()
                            line_num -= 1
                            editor(script, line_num, current_file)
                            yorn_correct = True
                            recently_saved = True
                        elif yorn == 'n':
                            # zo nee ga terug naar editor
                            yorn_correct = True
                            script.pop()
                            line_num -= 1
                
            # als 'exit' ga terug naar editor
            elif save_name == 'exit':
                script.pop()
                line_num -= 1
                editor(script, line_num, current_file)
            # else save file
            else:
                save(script, save_name)
                script.pop()
                line_num -= 1
                editor(script, line_num, current_file)
                recently_saved = True

    else:
        print(line_num)
        script[line_num] = current_line
        recently_saved = False
    script += ['']
    line_num += 1





        
# print(script)
output = ''
for i in range(0, len(script)):
    output = output + script[i] + '\n'
print('\n'+output)

# [current_string[i:i+3] for i in range(0, len(current_string), 3)]