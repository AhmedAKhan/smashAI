import pipes
import time;
from memoryWatcher import MemoryWatcher

"""
    self.pipe = this is variable that is the pipe, you can write to it, or read to it and it will write to the file
    self.path = the location to where the dolphin folder is inside the computer
"""


# def findDolphinPath():
#     homePath = os.path.expanduser('~'); # this is the home path
#     if sys.platform == "linux" or sys.platform == "linux2":
#         path = homePath  # linux
#         if (os.path.isdir(homePath + '/.local/share/dolphin-emu')): path += '/.local/share/dolphin-emu';
#         else: path = homePath + '/.local/dolphin-emu';
#         homePath = path;
#     elif sys.platform == "darwin": homePath += "/Library/Application Support/Dolphin"
#     print(homePath);
#     if(not (os.path.isdir(homePath))):
#         print("can not find path for dolphin, are you sure it is installed??");
#         print("if it is already installed then can you please store the location to the dolphin config files in the environment variable XDG_DATA_HOME");
#         print("example: export XDG_DATA_HOME='path to dolphin'");
#         return "";
#     ## return the home path
#     return homePath;

# timer=MemoryWatcher(self.path)
# timer.startSocket();

class Controller:
    def __init__(self, path):
        self.path = path;
        pipeTemplate = pipes.Template()
        pipeTemplate.append('tr a-z A-Z', '--')
        self.pipe = pipeTemplate.open(self.path+'/Pipes/cpu-level-11', 'w')

    def test(self, txt):
        self.pipe.write(txt)
        time.sleep(2);
        print(self.pipe);
        print(type(self.pipe));
        self.pipe.flush();
        # self.pipe.close()


#call this at the end of every script
    def releaseButtons(self):
        pipeTemplate = pipes.Template()
        pipeTemplate.append('tr a-z A-Z', '--')
        pipe = pipeTemplate.open(self.path+'/Pipes/cpu-level-11', 'w')
        pipe.write("Set MAIN 0.5 0.5\n");
        pipe.write("SET C 0.5 0.5\n");
        pipe.write("SET L 0\n");
        pipe.write("SET R 0\n");
        pipe.write("RELEASE X\n");
        pipe.write("RELEASE A\n");
        pipe.write("RELEASE B\n");
        pipe.write("RELEASE Z\n");
        pipe.write("RELEASE L\n");
        pipe.write("RELEASE START\n");
        pipe.close();

    #this doesn't work because you can't seem to pass in variables in pipes
    """
        this function will press or release the given button for the given amount of time
        par1 = button2Press = the current button that needs to be pressed
        par2 = timeHeld = the time that the button needs to be held
        par3 = if you want the button to be released make pressOrReleased to False
    """
    def inputs(self,button2Press,pressOrRelease=True):

        pipeTemplate = pipes.Template()
        pipeTemplate.append('tr a-z A-Z', '--')
        pipe = pipeTemplate.open(self.path+'/Pipes/cpu-level-11', 'w')
        action = "PRESS";
        if(not pressOrRelease): action = "RELEASE";
        pipe.write(action + " "+button2Press+"\n")
        pipe.close();

    def inputAnalog(self,action,buttonXCord,buttonYCord,pressOrRelease=True):
        pipeTemplate = pipes.Template()
        pipeTemplate.append('tr a-z A-Z', '--')
        pipe = pipeTemplate.open(self.path+'/Pipes/cpu-level-11', 'w')
        if(not pressOrRelease): action = "RELEASE";
        pipe.write("Set"+" "+action+" "+buttonXCord+" "+buttonYCord+"\n")
        pipe.close();

    def triggerAnalog(self,action,buttonXCord,pressOrRelease=True):
        pipeTemplate = pipes.Template()
        pipeTemplate.append('tr a-z A-Z', '--')
        pipe = pipeTemplate.open(self.path+'/Pipes/cpu-level-11', 'w')
        if(not pressOrRelease): action = "RELEASE";
        pipe.write("Set"+" "+action+" "+buttonXCord+" "+"\n")
        pipe.close();
#pass in 2 frames for short hop, 3 or more for full hop
    def jump(self,pauseTime):
        pipeTemplate = pipes.Template()
        pipeTemplate.append('tr a-z A-Z', '--')
        pipe = pipeTemplate.open(self.path+'/Pipes/cpu-level-11', 'w')
        pipe.write("RELEASE X\n");
        pipe.write("PRESS X\n");
        pipe.close();
        timer=MemoryWatcher(self.path)
        timer.startSocket();
        timer.pauseForTime(pauseTime)
        pipe = pipeTemplate.open(self.path+'/Pipes/cpu-level-11', 'w')
        pipe.write("RELEASE X\n");
        pipe.close();

#still a work in progress
    def dashDance(self):

        timer=MemoryWatcher(self.path)
        timer.startSocket();
        timer.pauseForTime(12)

        self.inputAnalog("MAIN","0.5","0.5")
        x=15
        while (x>0):

            timer.pauseForTime(11)

            self.inputAnalog("MAIN","0","0.5")
            timer.pauseForTime(11)
            self.inputAnalog("MAIN","1","0.5")
            x=x-1
    # def walk (self):
    # def run (self):
    # def jab (self):
    def upB(self,xCord,yCord):
        pipeTemplate = pipes.Template()
        pipeTemplate.append('tr a-z A-Z', '--')
        self.inputAnalog("MAIN","0.5","1")
        self.inputs("B")
        timer=MemoryWatcher(self.path)
        timer.startSocket();
        timer.pauseForTime(2)
        self.inputAnalog("MAIN",xCord,yCord)
        timer.pauseForTime(76)


    def sideB(self,Shorten):
        timer=MemoryWatcher(self.path)
        timer.startSocket();
        self.inputAnalog("MAIN","0","0.5")
        timer.pauseForTime(1)
        self.inputs("B",1)
        timer.pauseForTime(1)
# 18
        if Shorten is True:
            self.releaseButtons()
            timer.pauseForTime(20)
            self.inputs("B")

        timer.pauseForTime(1)

#performs a jump cancelled up Smash
    def upSmash(self):
        timer=MemoryWatcher(self.path)
        timer.startSocket();

        self.inputAnalog("MAIN","0.5","1")
        timer.pauseForTime(1)
        self.inputs("A",1)
        timer.pauseForTime(3)

    def upTilt(self):

        timer=MemoryWatcher(self.path)
        timer.startSocket();
        self.inputAnalog("MAIN","0.5","0.6")
        timer.pauseForTime(1)
        self.inputs("A",1)
        timer.pauseForTime(3)

    def shield(self):
        self.triggerAnalog("L","1")

    def roll(self,dir):

        timer=MemoryWatcher(self.path)
        timer.startSocket();
        self.shield()
        timer.pauseForTime(14)
        print (dir)
        if dir=="right":
            self.inputAnalog("C","1","0.5")
        elif dir is "left":
            self.inputAnalog("C","0","0.5")
        timer.pauseForTime(1)

    def dashAttack(self,dir):

        timer=MemoryWatcher(self.path)
        timer.startSocket();
        if dir=="right":
            self.inputAnalog("MAIN","1","0.5")
        elif dir is "left":
            self.inputAnalog("MAIN","0","0.5")
        timer.pauseForTime(4)
        self.inputs("A")
        timer.pauseForTime(1)

    def waveDash(self,dir):

        timer=MemoryWatcher(self.path)
        timer.startSocket()
        if dir=="right": self.inputAnalog("MAIN","0","0.3")
        elif dir=="left": self.inputAnalog("MAIN","1","0.3")
        self.inputs("X")
        timer.pauseForTime(4)

        self.inputs("L")
        timer.pauseForTime(7)


    def test2(self):
        time.sleep(2)
        self.releaseButtons()
        # self.sideB(True);
        # self.upSmash()
        # self.shield()
        # self.roll("right")
        # self.upTilt()
        # self.upB("0","1")
        # self.dashAttack("left")
        # self.waveDash("right")
        # self.dashDance()

        # timer=MemoryWatcher(self.path)
        # timer.startSocket();
        # pipeTemplate = pipes.Template()
        # pipeTemplate.append('tr a-z A-Z', '--')
        # pipe = pipeTemplate.open(self.path+'/Pipes/cpu-level-11', 'w')
        # pipe.write("PRESS X\n")
        # pipe.close();
        # timer.pauseForTime(26)



        self.releaseButtons()
        return;


    def inputsFunctionTest(self):
        time.sleep(4);
        self.inputs("X",10);
        self.inputs("X",10, False);
        # self.inputs(self,"A",10);

