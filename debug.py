from classes.Core import Core
import os

def main():
    core = Core(os.path.split(os.path.realpath(__file__))[0])
    while True:
        command = input('> ').strip().split()
        if (len(command) == 0):
            print('Invalid command')
        elif (command[0] == 'exit'):
            break
        elif (command[0] == 'scripts'):
            print('\n'.join([k for k in core.scripts.keys()]))
        elif (len(command) == 1):
            print('Invalid command')
        elif (command[0] == 'add'):
            script = ' '.join(command[1:])
            core.addScript(script)
            print('Project for \'' + script + '\' has been created')
        elif (command[0] == 'run'):
            script = ' '.join(command[1:])
            n = str(len(core.scripts[script].testCases))
            print('Running ' + n + ' cases against \'' + script + '\'...')

            core.runScript(script)
            
            passes = 0
            for test in core.scripts[script].testCases:
                s = test.getStatus()
                passes += s == 'PASSED'
                print(test.name + ' ' + test.getStatus())
            print(str(passes) + '/' + n + ' test cases passed')
        elif (command[0] == 'open'):
            script = ' '.join(command[1:])
            print('Opening ' + script + ' in IDLE...')
            core.openScript(script)
        else:
            print('Invalid command')

if (__name__ == '__main__'):
    main()
