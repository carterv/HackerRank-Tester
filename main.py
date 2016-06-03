from classes.MainWindow import MainWindow
from classes.Core import Core
import os

def main():
    #Program core, handles all the file management and testing
    core = Core(os.path.split(os.path.realpath(__file__))[0])
    core.loadScripts()

    #Testing values until GUI is working
    #script = 'Sherlock and The Beast'
    #core.addScript(script)
    #core.runScript(script)

    #GUI
    #app = MainWindow(core)
    #app.master.title("HackerRank Tester")
    #app.mainloop()
    


if (__name__ == '__main__'):
    main()
