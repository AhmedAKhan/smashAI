from memoryWatcher import MemoryWatcher;
from random import *;
from math import *;



class BasicCommands:
    def __init__(self, memoryWatcher, controller):
        self.memoryWatcher = memoryWatcher;
        self.controller = controller;
        self.p2x="00453F20"
        self.p2y="00453F24"
        self.rightlock = False
        self.leftlock = False
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
            self.memoryWatcher.pauseForTime(19)
            self.controller.inputs("B")
        self.memoryWatcher.pauseForTime(1)

    #performs a jump cancelled up Smash
    def upSmash(self):
        self.controller.inputAnalog("MAIN","0.5","1")
        self.memoryWatcher.pauseForTime(1)
        self.controller.inputs("A",1)
        self.memoryWatcher.pauseForTime(1)

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
        # print("not okay!!!!!!!!!!!")


    def recover(self):
       while (True):
           # self.memoryWatcher.getHitStun()
           # print ("This is the X please print",self.memoryWatcher.getX())
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
               # print ("This is the counter",counter)
               return counter



    def recover2(self):
               value = self.memoryWatcher.getHitStun();
               self.controller.inputAnalog("MAIN","0.5","0.7")
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
                    print("curX: ",curX)
                    if ( curX>81 ):
                        # self.recoveryHelper("left","left")
                        self.jump(2,"left")
                        self.memoryWatcher.pauseForTime(10)
                        curY = self.memoryWatcher.state['p2']['y'];
                        if (curY>-10):
                            if (randint(0,10)<7):self.sideB(False,"left")
                            else: self.upB("0","0.8")
                        else: self.upB("0","1")
                    elif (curX < -81):
                        self.jump(2,"right")
                        self.memoryWatcher.pauseForTime(10)
                        curY = self.memoryWatcher.state['p2']['y'];
                        if (curY>-10):
                            if (randint(0,10)<7):self.sideB(False,"right")
                            else: self.upB("1","0.8")
                        else: self.upB("1","1")

                    self.controller.releaseButtons();


    def recoveryHelper(self,jumpDir,upBdir):
                self.memoryWatcher.pauseForTime(10)
                self.jump(2,jumpDir)
                # if (currentY>1000000000): self.sideB(False,"left")
                # else: self.upB("0","1")
                if upBdir=="left":self.upB("0","1")
                else: self.upB("1","1")
                self.controller.releaseButtons()

    def shdl(self):
            self.jump(2, "")
            self.controller.releaseButtons();
            self.memoryWatcher.pauseForTime(2);
            self.controller.inputs("B",True);
            self.memoryWatcher.pauseForTime(1);
            self.controller.releaseButtons();
            self.memoryWatcher.pauseForTime(5);
            self.controller.inputs("B",True);
            self.memoryWatcher.pauseForTime(5);
            self.controller.releaseButtons();
            self.memoryWatcher.pauseForTime(13)


    def shortHopAerial(self):

            self.jump(2, "")
            self.controller.releaseButtons();
            self.memoryWatcher.pauseForTime(2);
            # self.controller.inputs("A",True);
            self.memoryWatcher.pauseForTime(11);
            # curYCPU = self.memoryWatcher.state['p2']['y'];
            # print("Before the L cancel",curYCPU)
            self.controller.releaseButtons();


            x=0


            self.memoryWatcher.readMemory();

            curYCPU = self.memoryWatcher.state['p2']['y'];
            # self.memoryWatcher.pauseForTime(1);
            print("This is the current Y",curYCPU)
            while True:
                self.memoryWatcher.pauseForTime(1);
            #     curYCPU = self.memoryWatcher.state['p2']['y'];

            # for i in range(200):
                # self.memoryWatcher.readMemory();
                previousValue = self.memoryWatcher.state['p2']['y'];
                if (x==1): print ("The fastfall while loop",previousValue)

                if (curYCPU>previousValue):
                    self.controller.inputAnalog("MAIN","0.5","0")
                    print("Fast fall now",previousValue)
                    break;

                x=x+1
                # print ("The current Y value of the CPU ",curYCPU)
                # previousValue = curYCPU;



                self.memoryWatcher.pauseForTime(30);

                # if (curYCPU<11 and curYCPU>9):
                #     self.controller.inputAnalog("MAIN","0.5","0")
                #     print("Fast fall now",curYCPU)
                #     break;


            # self.memoryWatcher.pauseForTime(4);
            self.controller.releaseButtons();
            # self.LCancel()
            # self.dashAttack("left")
            # self.controller.inputs("A",True);
            # self.memoryWatcher.pauseForTime(3);
            # self.upSmash()
            self.controller.releaseButtons();

    def LCancel(self):

        # while(True):
            # self.jump(2, "")
            # self.controller.releaseButtons();
            # self.memoryWatcher.pauseForTime(25);
            curY = self.memoryWatcher.state['p2']['y'];
            # print(curY)

            while ( curY>8 or curY<0 ):
                curY = self.memoryWatcher.state['p2']['y'];
                self.memoryWatcher.readMemory();
                # self.memoryWatcher.pauseForTime(1);
                print ("L cancel while loop")
            # self.memoryWatcher.pauseForTime(1);
            # print("Before the L cancel",curY)
            self.shield()
            self.memoryWatcher.pauseForTime(8);
            self.controller.releaseButtons();
            # self.memoryWatcher.pauseForTime(11);



    def facePlayer(self,curXPlayer,curXCPU):
                # rightlock = False;
                # leftlock  = False;

                # while True:

                    # curXPlayer = self.memoryWatcher.state['p1']['x'];
                    # curXCPU = self.memoryWatcher.state['p2']['x'];
                    self.memoryWatcher.pauseForTime(1)

                    if (curXPlayer > curXCPU and self.rightlock == False):
                        self.controller.inputAnalog("MAIN","0.6","0.5")
                        self.memoryWatcher.pauseForTime(2)
                        self.controller.releaseButtons()
                        self.rightlock = True
                        self.leftlock = False
                    elif (curXPlayer < curXCPU and self.leftlock == False):
                        self.controller.inputAnalog("MAIN","0.4","0.5")
                        self.memoryWatcher.pauseForTime(2)
                        self.controller.releaseButtons()
                        self.leftlock = True
                        self.rightlock = False




    def SHAerial(self,x):
              print("starting the SHAerial function y value: ", self.memoryWatcher.state['p2']['y']);
              pAx = self.memoryWatcher.state["p1"]['isOnGround']
              # self.memoryWatcher.readMemory();
              self.memoryWatcher.pauseForTime(1);
              # print(pAx)
              # print(x)
              if (pAx==True):
                  x=1;
              elif (pAx==False and x==1):
                  self.jump(2,"")
                  self.controller.releaseButtons();
                  self.memoryWatcher.pauseForTime(2);
                  self.controller.inputs("A",True)
                  self.memoryWatcher.pauseForTime(2);
                  self.controller.releaseButtons();
                  x=2
                  freezeCounter=0

                  print("SHAerial, y value: ", self.memoryWatcher.state['p2']['y']);
                  while True:
                    curYCPU = self.memoryWatcher.state['p2']['y'];
                    if( -0.01 <= curYCPU <= 0.01):
                        print("already hit the ground, to late");
                        break;
                    else:
                        print("y value: ", self.memoryWatcher.state['p2']['y'], " lower then 0.01: ", self.memoryWatcher.state['p2']['y']<= 0.01, " greater then -0.01", self.memoryWatcher.state['p2']['y'] >= -0.01);
                    # print("This is the previous Y", curYCPU)
                    self.memoryWatcher.readMemory()
                    curYCPU2 = self.memoryWatcher.state['p2']['y'];
                    if(curYCPU2 != curYCPU):
                        # print("this is the current Y", curYCPU2)
                        print("CHAnged previous current y: ", curYCPU, " current y: ", curYCPU2);


                    # freezeCounter=freezeCounter+1
                    # if (freezeCounter>500):
                    #     x=1
                    #     print ("it got stuck arieal")
                    #     raise ("arieal exception")
                        # break;
                    # print ("Getting stuck here?",pAx)
                    if (curYCPU>curYCPU2):
                        self.controller.inputAnalog("MAIN","0.5","0")
                        self.memoryWatcher.pauseForTime(2)
                        self.controller.releaseButtons();
                        self.LCancel()
                        while(pAx==True):
                            y=2
                        self.memoryWatcher.pauseForTime(5);
                        break;
              print("ending the SHAerial function ");


    def test2(self):
        self.memoryWatcher.pauseForTime(52)
        self.controller.releaseButtons()
        # self.controller.inputAnalog("MAIN","0.5","0")
        # self.memoryWatcher.pauseForTime(52)

        # while True:
        #     self.jump(2, "")
        #     self.controller.releaseButtons();
            # self.memoryWatcher.pauseForTime(13);
        #     # self.controller.inputs("A",True);
        #     # self.memoryWatcher.pauseForTime(12);

        #     for i in range(200):

        #         self.memoryWatcher.readMemory();
        #         curYCPU = self.memoryWatcher.state['p2']['y'];
        #         print (curYCPU)

        # x=1
        # while True:
        #       pAx = self.memoryWatcher.state["p1"]['isOnGround']
        #       # self.memoryWatcher.readMemory();
        #       self.memoryWatcher.pauseForTime(2);
        #       print(pAx)
        #       print(x)
        #       if (pAx==True):
        #           x=1;
        #       elif (pAx==False and x==1):
        #           self.memoryWatcher.pauseForTime(3);
        #           self.jump(2,"")
        #           self.controller.releaseButtons();
        #           self.memoryWatcher.pauseForTime(2);
        #           self.controller.inputs("A",True)
        #           self.memoryWatcher.pauseForTime(2);
        #           self.controller.releaseButtons();
        #           x=2
        #           freezeCounter=0
        #           while True:
        #             curYCPU = self.memoryWatcher.state['p2']['y'];
        #             self.memoryWatcher.pauseForTime(1)
        #             # self.memoryWatcher.readMemory()
        #             curYCPU2 = self.memoryWatcher.state['p2']['y'];
        #             print ("Getting stuck here?")
        #             freezeCounter=freezeCounter+1
        #             if (freezeCounter>20):
        #                 x=1
        #                 # self.memoryWatcher.pauseForTime(56);
        #                 break
        #             if (curYCPU>curYCPU2):
        #                 self.controller.inputAnalog("MAIN","0.5","0")
        #                 self.memoryWatcher.pauseForTime(1)
        #                 self.controller.releaseButtons();
        #                 self.LCancel()
        #                 break;

        # while True:
        #     pAx = self.memoryWatcher.state[player]['speedAttackX']
        #     pAy = self.memoryWatcher.state[player]['speedAttackY']
        #     self.memoryWatcher.pauseForTime(4)
        #     print (pAx)
        #     print (pAy)

        while True:
            x=1
            curXPlayer = self.memoryWatcher.state['p1']['x'];
            curXCPU = self.memoryWatcher.state['p2']['x'];
            # print ("this is curXCPU",curXCPU)
            self.memoryWatcher.pauseForTime(1)
            self.facePlayer(curXPlayer,curXCPU)
            if (curXCPU>61 or curXCPU <-61): self.recover2()
            else:
                self.memoryWatcher.pauseForTime(1)
                distance = (abs(curXPlayer-curXCPU))
                if (distance>40):
                    self.shdl()
                else:
                    if (curXPlayer > curXCPU and curXCPU<=62 and curXCPU>=-62):
                        self.controller.inputAnalog("MAIN","1","0.5")
                        self.memoryWatcher.pauseForTime(3)
                        self.controller.releaseButtons()
                        self.SHAerial(x)
                        self.controller.releaseButtons()
                    if (curXPlayer < curXCPU and curXCPU>=-62 and curXCPU<=62):
                        self.controller.inputAnalog("MAIN","0","0.5")
                        self.memoryWatcher.pauseForTime(3)
                        self.controller.releaseButtons()
                        self.SHAerial(x)
                        self.controller.releaseButtons()

            # self.shdl()
            # self.dashDance()
            # self.shortHopAerial()
            # self.controller.releaseButtons()
            # self.memoryWatcher.pauseForTime(13)

        # # while(True):
        # self.jump(2, "")
        # self.controller.releaseButtons();
        # self.memoryWatcher.pauseForTime(5)
        # self.controller.inputs("A",True)
        # self.memoryWatcher.pauseForTime(8);
        # self.controller.releaseButtons()
        # # curY = self.memoryWatcher.state['p2']['y'];
        # # print(curY)
        # while ( self.memoryWatcher.state['p2']['y']>4.5 or   self.memoryWatcher.state['p2']['y']<0 ):
        #     curY = self.memoryWatcher.state['p2']['y'];
        #     self.memoryWatcher.pauseForTime(1);
        #     print(curY)
        #     # print ("Ok")
        # self.shield()
        # self.memoryWatcher.pauseForTime(2);
        # self.controller.releaseButtons();
        # self.memoryWatcher.pauseForTime(6);

        # while(True):
        #     self.memoryWatcher.getX()
        # while (True):
        # self.recover2()
            # self.memoryWatcher.getX()
            # self.test3()
            # self.recover()
            # print(self.memoryWatcher.getX(self.p2y))


            # self.memoryWatcher.pauseForTime(100);

        # self.memoryWatcher.pauseForTime(20)
        # self.sideB(True,"left");
        # self.upSmash()
        # self.shield()
        # self.recover2()
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
