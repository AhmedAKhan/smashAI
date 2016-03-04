import pipes
import time;
from memoryWatcher import MemoryWatcher

"""
    self.pipe = this is variable that is the pipe, you can write to it, or read to it and it will write to the file
    self.path = the location to where the dolphin folder is inside the computer
"""



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
        pipe.write("RELEASE X\n");
        pipe.write("RELEASE A\n");
        pipe.write("RELEASE B\n");
        pipe.write("RELEASE Z\n");
        pipe.write("RELEASE START\n");
        pipe.close();

#this doesn't work because you can't seem to pass in variables in pipes
    def inputs(self,button2Press,timeHeld):
        pipeTemplate = pipes.Template()
        pipeTemplate.append('tr a-z A-Z', '--')
        pipe = pipeTemplate.open(self.path+'/Pipes/cpu-level-11', 'w')
        pipe.write("RELEASE Y\n");
        pipe.write("RELEASE X\n");
        # pipe.write("PRESS X\n");
        print ("PRESS "+button2Press+"\n")
        print ("PRESS X\n")
        pipe.write("PRESS"+button2Press+"\n")
        timer=MemoryWatcher(self.path)
        timer.startSocket();
        timer.pauseForTime(timeHeld)
        # pipe.write("RELEASE "+button2Press+"\n");
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
        pipeTemplate = pipes.Template()
        pipeTemplate.append('tr a-z A-Z', '--')
        timer.pauseForTime(12)
        pipe = pipeTemplate.open(self.path+'/Pipes/cpu-level-11', 'w')
        pipe.write("Set MAIN 0.5 0.5\n");
        pipe.close();
        x=15
        while (x>0):

            timer.pauseForTime(11)
            pipe = pipeTemplate.open(self.path+'/Pipes/cpu-level-11', 'w')
            pipe.write("Set MAIN 0 0.5\n");
            pipe.close();

            timer.pauseForTime(11)
            pipe = pipeTemplate.open(self.path+'/Pipes/cpu-level-11', 'w')
            pipe.write("Set MAIN 1 0.5\n");
            pipe.close();
            x=x-1
    # def walk (self):
    # def run (self):
    # def jab (self):

    def sideB(self,Shorten):
        pipeTemplate = pipes.Template()
        pipeTemplate.append('tr a-z A-Z', '--')
        timer=MemoryWatcher(self.path)
        timer.startSocket();

        pipe = pipeTemplate.open(self.path+'/Pipes/cpu-level-11', 'w')
        pipe.write("Set MAIN 0 0.5\n");
        pipe.close();

        timer.pauseForTime(1)

        pipe = pipeTemplate.open(self.path+'/Pipes/cpu-level-11', 'w')
        pipe.write("PRESS B\n");
        pipe.close();
        timer.pauseForTime(1)

        if Shorten is True:
            pipe = pipeTemplate.open(self.path+'/Pipes/cpu-level-11', 'w')
            pipe.write("RELEASE B\n");
            pipe.close();
            timer.pauseForTime(18)
            pipe = pipeTemplate.open(self.path+'/Pipes/cpu-level-11', 'w')
            pipe.write("PRESS B\n");
            pipe.close();

        timer.pauseForTime(1)

#performs a jump cancelled up Smash
    def upSmash(self):

        pipeTemplate = pipes.Template()
        pipeTemplate.append('tr a-z A-Z', '--')
        timer=MemoryWatcher(self.path)
        timer.startSocket();
        pipe = pipeTemplate.open(self.path+'/Pipes/cpu-level-11', 'w')
        pipe.write("Set MAIN 0.5 1\n");
        pipe.close();

        timer.pauseForTime(1)

        pipe = pipeTemplate.open(self.path+'/Pipes/cpu-level-11', 'w')
        pipe.write("PRESS A\n");
        pipe.close();
        timer.pauseForTime(3)




    def test2(self):
        time.sleep(2)

       # self.dashDance()

        # timer=MemoryWatcher(self.path)
        # timer.startSocket();
        # pipeTemplate = pipes.Template()
        # pipeTemplate.append('tr a-z A-Z', '--')
        # pipe = pipeTemplate.open(self.path+'/Pipes/cpu-level-11', 'w')
        # pipe.write("Set MAIN 0 0.5\n")
        # pipe.close();
        # timer.pauseForTime(26)

        #self.sideB(True)


        self.releaseButtons()
        return;




