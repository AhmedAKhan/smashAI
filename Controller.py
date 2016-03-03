import pipes
import time;
from memoryWatcher import MemoryWatcher

"""
    self.pipe = this is variable that is the pipe, you can write to it, or read to it and it will write to the file
    self.path = the location to where the dolphin folder is inside the computer
"""

def testFun():
    print ("It works")
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



    def test2(self):
        time.sleep(3)
        testFun()
        pipeTemplate = pipes.Template()
        pipeTemplate.append('tr a-z A-Z', '--')

        pipe = pipeTemplate.open(self.path+'/Pipes/cpu-level-11', 'w')
        pipe.write("RELEASE Y\n");
        pipe.write("RELEASE X\n");
        pipe.write("PRESS X\n");
        pipe.close();

        timer=MemoryWatcher(self.path)
        timer.startSocket();
        timer.pauseForTime(2)


        pipe = pipeTemplate.open(self.path+'/Pipes/cpu-level-11', 'w')
        pipe.write("RELEASE X\n");
        pipe.close();


        return;




