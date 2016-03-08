import time;


class BasicCommands:
    def __init__(self, memoryWatcher, controller):
        self.memoryWatcher = memoryWatcher;
        self.controller = controller;
    def dashDance(self):
        self.memoryWatcher.pauseForTime(12)

        self.controller.inputAnalog("MAIN","0.5","0.5")
        x=15;
        while (x>0):
            self.memoryWatcher.pauseForTime(11)
            self.controller.inputAnalog("MAIN","0","0.5")
            self.memoryWatcher.pauseForTime(11)
            self.controller.inputAnalog("MAIN","1","0.5")
            x=x-1
    # def walk (self):
    # def run (self):
    # def jab (self):
    def upB(self,xCord,yCord):
        # self.memoryWatcher.pauseForTime(10)
        self.controller.inputAnalog("MAIN","0.5","1")
        self.memoryWatcher.pauseForTime(30)
        self.controller.inputs("B")
        self.memoryWatcher.pauseForTime(2)
        self.controller.inputAnalog("MAIN",xCord,yCord)
        self.memoryWatcher.pauseForTime(70)


    def sideB(self,Shorten):
        self.controller.inputAnalog("MAIN","0","0.5")
        self.memoryWatcher.pauseForTime(1)
        self.controller.inputs("B",1)
        self.memoryWatcher.pauseForTime(1)
        # 18
        if Shorten is True:
            self.controller.releaseButtons()
            self.memoryWatcher.pauseForTime(20)
            self.controller.inputs("B")

        self.memoryWatcher.pauseForTime(1)

    #performs a jump cancelled up Smash
    def upSmash(self):
        self.controller.inputAnalog("MAIN","0.5","1")
        self.memoryWatcher.pauseForTime(1)
        self.controller.inputs("A",1)
        self.memoryWatcher.pauseForTime(3)

    def upTilt(self):
        self.controller.inputAnalog("MAIN","0.5","0.6")
        self.memoryWatcher.pauseForTime(1)
        self.controller.inputs("A",1)
        self.memoryWatcher.pauseForTime(3)

    def shield(self):
        self.controller.triggerAnalog("L","1")

    def roll(self,dir):
        self.shield()
        self.memoryWatcher.pauseForTime(14)
        print (dir)
        if dir=="right":
            self.controller.inputAnalog("C","1","0.5")
        elif dir is "left":
            self.controller.inputAnalog("C","0","0.5")
        self.memoryWatcher.pauseForTime(1)

    def dashAttack(self,dir):
        if dir=="right":
            self.controller.inputAnalog("MAIN","1","0.5")
        elif dir is "left":
            self.controller.inputAnalog("MAIN","0","0.5")
        self.memoryWatcher.pauseForTime(4)
        self.controller.inputs("A")
        self.memoryWatcher.pauseForTime(1)

    def waveDash(self,dir):
        # timer = self.memoryWatcher;
        if dir=="right": self.controller.inputAnalog("MAIN","0","0.3")
        elif dir=="left": self.controller.inputAnalog("MAIN","1","0.3")
        self.controller.inputs("X")
        self.memoryWatcher.pauseForTime(4)

        self.controller.inputs("L")
        self.memoryWatcher.pauseForTime(7)


    #pass in 2 frames for short hop, 3 or more for full hop
    def jump(self,pauseTime):
        self.controller.inputs("X");
        timer = self.memoryWatcher;
        timer.pauseForTime(pauseTime)
        self.controller.releaseButtons();

    def recover(self):
       while (True):
           # self.memoryWatcher.getHitStun()
           value = 0;
           while(True):
               value = self.memoryWatcher.getHitStun();
               if( value != -1): break
           # print (value)
           if (value < 1000):
                currentX = self.memoryWatcher.getX();
                print ("This is the current X",currentX)
                if ( 1120447161< self.memoryWatcher.getX() <1124447162 ):
                    print ("this is the one:",self.memoryWatcher.getX())
                    print ("This is the other branch")
                    self.upB("0","1")
                    self.controller.releaseButtons()
                elif (self.memoryWatcher.getX() > 3268000000):
                    print ("This is the X",currentX)
                    self.upB("1","1")
                    self.controller.releaseButtons()

    def test2(self):
        time.sleep(1)
        self.controller.releaseButtons()

        # while(True):
        #     self.memoryWatcher.getX()

        self.recover()

        # self.sideB(True);
        # self.upSmash()
        # self.shield()
        # self.roll("right")
        # self.upTilt()
        # self.upB("0","0")
        # self.dashAttack("left")
        # self.waveDash("left")
        # self.dashDance()

        self.controller.releaseButtons()
        return;




def main():
    print("inside the basic commands file");







if __name__ == '__main__':
    main();
