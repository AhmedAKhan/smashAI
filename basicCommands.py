from memoryWatcher import MemoryWatcher;
# from random import *;


class BasicCommands:
    def __init__(self, memoryWatcher, controller):
        self.memoryWatcher = memoryWatcher;
        self.controller = controller;
        self.p2x="00453F20"
        self.p2y="00453F24"
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

        self.memoryWatcher.pauseForTime(15)

        self.controller.inputs("B")
        self.memoryWatcher.pauseForTime(2)
        self.controller.inputAnalog("MAIN",xCord,yCord)
        self.memoryWatcher.pauseForTime(70)


    def sideB(self,Shorten,dirr):
        self.memoryWatcher.pauseForTime(3)
        if (dirr=="left"):self.controller.inputAnalog("MAIN","0","0.5")
        else: self.controller.inputAnalog("MAIN","1","0.5")
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
        self.memoryWatcher.pauseForTime(2)
        self.controller.inputs("A",1)
        self.memoryWatcher.pauseForTime(3)

    def shield(self):
        self.controller.triggerAnalog("L","1")

    def roll(self,dir):
        self.shield()
        self.memoryWatcher.pauseForTime(9)
        print (dir)
        if dir=="right":
            self.controller.inputAnalog("MAIN","1","0.5")
        elif dir is "left":
            self.controller.inputAnalog("MAIN","0","0.5")
        self.memoryWatcher.pauseForTime(1)

    def dashAttack(self,dir):
        if (dir=="right"):
            self.controller.inputAnalog("MAIN","1","0.5")
        elif (dir=="left"):
            self.controller.inputAnalog("MAIN","0","0.5")
        self.memoryWatcher.pauseForTime(9)
        self.controller.inputs("A")
        self.memoryWatcher.pauseForTime(1)

    def waveDash(self,dir):
        # timer = self.memoryWatcher;
        if dir=="left": self.controller.inputAnalog("MAIN","0","0.3")
        elif dir=="right": self.controller.inputAnalog("MAIN","1","0.3")
        self.controller.inputs("X")
        self.memoryWatcher.pauseForTime(4)
        self.controller.inputs("L")
        self.memoryWatcher.pauseForTime(7)


    #pass in 2 frames for short hop, 3 or more for full hop
    def jump(self,pauseTime,dirr):
        if (dirr=="right"): self.controller.inputAnalog("MAIN","1","0.5")
        elif (dirr=="left"): self.controller.inputAnalog("MAIN","0","0.5")
        self.controller.inputs("X");
        timer = self.memoryWatcher;
        self.controller.inputs("X");
        timer.pauseForTime(pauseTime)


    def recover(self):
       while (True):
           # self.memoryWatcher.getHitStun()
           print ("This is the X please print",self.memoryWatcher.getX())
           if (self.memoryWatcher.getHitStun()==0):
                # currentX = self.memoryWatcher.getX();
                if ( 1120447161< self.memoryWatcher.getX() <1124447162 ):
                    # print ("this is the one:",self.memoryWatcher.getX())
                    # print ("This is the other branch")
                    self.upB("0","1")
                    self.controller.releaseButtons()
                elif (self.memoryWatcher.getX() > 3268000000):
                    # print ("This is the X",currentX)
                    self.upB("1","1")
                    self.controller.releaseButtons()

    def test3(self):
               value = self.memoryWatcher.getHitStun();
               x=0
               counter = 0
               while (x<20):

                    if (self.memoryWatcher.getHitStun()!=-1):
                        # print (value)
                        counter=counter+1
                    else:
                        # print("no")
                        counter=counter-1
                    x=x+1
               print ("This is the counter",counter)
               return counter


    def recover2(self):
       while (True):
               value = self.memoryWatcher.getHitStun();
               currentX = self.memoryWatcher.getX(self.p2x);

               if ( self.test3()>= -16):
                        print (value)
                        self.controller.releaseButtons()
                        self.controller.inputAnalog("MAIN","0","0.5")
                        self.memoryWatcher.pauseForTime(2)
                        self.controller.inputAnalog("MAIN","1","0.5")
                        self.controller.releaseButtons()

               else:
                    # currentX = self.memoryWatcher.getX(self.p2x);
                    # currentY = self.memoryWatcher.getX(self.p2y);
                    curX = self.memoryWatcher.state['p2']['x'];
                    curY = self.memoryWatcher.state['p2']['y'];
                    print (curX)
                    if ( 88< curX <100 ):
                        self.recoveryHelper("left","left")
                    elif (curX < -88):
                        # if (randint(0,10)<5):
                        self.recoveryHelper("right","right")
                        # else:
                        if (curY>0): self.sideB(False,"right")
                        else: self.upB("1","0.5")

    def recoveryHelper(self,jumpDir,upBdir):
                self.memoryWatcher.pauseForTime(10)
                self.jump(2,jumpDir)
                # if (currentY>1000000000): self.sideB(False,"left")
                # else: self.upB("0","1")
                if upBdir=="left":self.upB("0","1")
                else: self.upB("1","1")
                self.controller.releaseButtons()

    def test2(self):
        self.memoryWatcher.pauseForTime(100)
        self.controller.releaseButtons()

        # while(True):
        #     self.memoryWatcher.getX()
        # while (True):
        # self.recover2()
            # self.memoryWatcher.getX()
            # self.test3()
            # self.recover()
            # print(self.memoryWatcher.getX(self.p2y))

        # self.jump(7,"right")
        # self.memoryWatcher.pauseForTime(20)
        # self.sideB("right",False);
        # self.upSmash()
        # self.shield()
        self.recover2()
        # self.roll("right")
        # self.upTilt()
        # self.upB("0","0")
        # self.dashAttack("right")
        # self.waveDash("right")
        # self.dashDance()

        self.controller.releaseButtons()
        return;




# def main():
#     print("inside the basic commands file");
# if __name__ == '__main__':
    # main();
