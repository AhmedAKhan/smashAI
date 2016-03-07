import pipes
import time;


class BasicCommands:
    def __init__(self, memoryWatcher, controller):
        self.memoryWatcher = memoryWatcher;
        self.controller = controller;
    def dashDance(self):
        timer=self.memoryWatcher;
        timer.pauseForTime(12)

        self.controller.inputAnalog("MAIN","0.5","0.5")
        x=15
        while (x>0):

            timer.pauseForTime(11)

            self.controller.inputAnalog("MAIN","0","0.5")
            timer.pauseForTime(11)
            self.controller.inputAnalog("MAIN","1","0.5")
            x=x-1
    # def walk (self):
    # def run (self):
    # def jab (self):
    def upB(self,xCord,yCord):
        timer= self.memoryWatcher;
        timer.pauseForTime(10)
        pipeTemplate = pipes.Template()
        pipeTemplate.append('tr a-z A-Z', '--')
        self.controller.inputAnalog("MAIN","0.5","1")
        timer.pauseForTime(30)
        self.controller.inputs("B")
        timer.pauseForTime(2)
        self.controller.inputAnalog("MAIN",xCord,yCord)
        timer.pauseForTime(76)


    def sideB(self,Shorten):
        timer=self.memoryWatcher;
        self.controller.inputAnalog("MAIN","0","0.5")
        timer.pauseForTime(1)
        self.controller.inputs("B",1)
        timer.pauseForTime(1)
    # 18
        if Shorten is True:
            self.controller.releaseButtons()
            timer.pauseForTime(20)
            self.controller.inputs("B")

        timer.pauseForTime(1)

    #performs a jump cancelled up Smash
    def upSmash(self):
        timer=self.memoryWatcher;

        self.controller.inputAnalog("MAIN","0.5","1")
        timer.pauseForTime(1)
        self.controller.inputs("A",1)
        timer.pauseForTime(3)

    def upTilt(self):

        timer= self.memoryWatcher;
        self.controller.inputAnalog("MAIN","0.5","0.6")
        timer.pauseForTime(1)
        self.controller.inputs("A",1)
        timer.pauseForTime(3)

    def shield(self):
        self.triggerAnalog("L","1")

    def roll(self,dir):

        timer = self.memoryWatcher;
        self.shield()
        timer.pauseForTime(14)
        print (dir)
        if dir=="right":
            self.controller.inputAnalog("C","1","0.5")
        elif dir is "left":
            self.controller.inputAnalog("C","0","0.5")
        timer.pauseForTime(1)

    def dashAttack(self,dir):

        timer = self.memoryWatcher;
        if dir=="right":
            self.controller.inputAnalog("MAIN","1","0.5")
        elif dir is "left":
            self.controller.inputAnalog("MAIN","0","0.5")
        timer.pauseForTime(4)
        self.controller.inputs("A")
        timer.pauseForTime(1)

    def waveDash(self,dir):

        timer = self.memoryWatcher;
        if dir=="right": self.controller.inputAnalog("MAIN","0","0.3")
        elif dir=="left": self.controller.inputAnalog("MAIN","1","0.3")
        self.controller.inputs("X")
        timer.pauseForTime(4)

        self.controller.inputs("L")
        timer.pauseForTime(7)


    #pass in 2 frames for short hop, 3 or more for full hop
    def jump(self,pauseTime):
        pipeTemplate = pipes.Template()
        pipeTemplate.append('tr a-z A-Z', '--')
        pipe = pipeTemplate.open(self.path+'/Pipes/cpu-level-11', 'w')
        pipe.write("RELEASE X\n");
        pipe.write("PRESS X\n");
        pipe.close();
        timer = self.memoryWatcher;
        timer.pauseForTime(pauseTime)
        pipe = pipeTemplate.open(self.path+'/Pipes/cpu-level-11', 'w')
        pipe.write("RELEASE X\n");
        pipe.close();

    def recover(self):
       while (True):
           currentX = self.memoryWatcher.getX();
           if ( 1120447161< currentX <1124447162 ):
               print ("this is the one:",currentX)
               self.upB("0","1")
               self.controller.releaseButtons()
           elif (currentX > 3268000000):
               print ("this is the one:",currentX)
               self.upB("1","1")
               self.controller.releaseButtons()

    def test2(self):
        time.sleep(1)
        self.controller.releaseButtons()

        # y=0
        # x = self.memoryWatcher;
        # while (y<1000):
        #     x.getX()
        #     y=y+1



        # y=0
        # hitstun=self.memoryWatcher;
        # while (y<1000):
        #     print (hitstun.getHitStun())
        #     y=y+1


        # self.sideB(True);
        # self.upSmash()
        # self.shield()
        # self.roll("right")
        # self.upTilt()
        # self.upB("0","1")
        # self.dashAttack("left")
        # self.waveDash("left")
        # self.dashDance()

        # timer=MemoryWatcher(self.path)
        # timer.startSocket();
        # pipeTemplate = pipes.Template()
        # pipeTemplate.append('tr a-z A-Z', '--')
        # pipe = pipeTemplate.open(self.path+'/Pipes/cpu-level-11', 'w')
        # pipe.write("PRESS X\n")
        # pipe.close();
        # timer.pauseForTime(26)



        self.controller.releaseButtons()
        return;




def main():
    print("inside the basic commands file");







if __name__ == '__main__':
    main();
