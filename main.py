
from memoryWatcher import MemoryWatcher;
from Controller import Controller;
import sys;
import os;
import cpu;
import time

def findDolphinPath():
    homePath = os.path.expanduser('~'); # this is the home path
    if sys.platform == "linux" or sys.platform == "linux2":
        path = homePath  # linux
        if (os.path.isdir(homePath + '/.local/share/dolphin-emu')): path += '/.local/share/dolphin-emu';
        else: path = homePath + '/.local/dolphin-emu';
        homePath = path;
    elif sys.platform == "darwin": homePath += "/Library/Application Support/Dolphin"

    print(homePath);
    if(not (os.path.isdir(homePath))):
        print("can not find path for dolphin, are you sure it is installed??");
        print("if it is already installed then can you please store the location to the dolphin config files in the environment variable XDG_DATA_HOME");
        print("example: export XDG_DATA_HOME='path to dolphin'");
        return "";
    ## return the home path
    return homePath;


# memWatcher = MemoryWatcher(findDolphinPath());
# controller = Controller(findDolphinPath());

# controller.test();
# memWatcher.test();

# print(findDolphinPath());



def initialSetup():
    return;

def main():
    initialSetup();
    # memWatcher = MemoryWatcher(findDolphinPath());
    controller = Controller(findDolphinPath());
    # memWatcher.startSocket();
    controller.test2();
    return;




if __name__ == '__main__':
    main();
