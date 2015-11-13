require "smashFunctions"

xCord=0x2EEF10
yCord=0x2EEE88
distance=0x18EB3C
p2Y=0x268984
p2X=0x268AC0

function mRecovery ()  -- Mario Recovery
  ledge()
  readAddressX()
   if (memory.read_s16_be(xCord)>5000 or memory.read_s16_be(xCord)<-5000 ) then 
    farRecovery()
  else
    if math.random()<0.50 then recoverLow(jUPb)
     else recoverHigh(jUPb) end
   end

  end

function farRecovery()    --runs when Mario is very far offstage
  if (memory.read_s16_be(yCord)<=(-15674) and memory.read_s16_be(yCord)>=(-15800))  and (memory.read_s16_be(xCord)>2200) then 
   button("P1 A Left")    --does a down B, jump then delayed up B
   downB("Left")
   timer(50)
   dUPb(80)
  end  
  if (memory.read_s16_be(yCord)<=(-15674) and memory.read_s16_be(yCord)>=(-15800)) and (memory.read_s16_be(xCord)<-2200) then   --checks y coordinate for left side
    button("P1 A Right")
    downB("Right")
    timer(50)
    dUPb(80)
  end
end

function readAddressX()
  if (memory.read_s16_be(xCord)>3500) then      --checks x coordinate for right side
    button("P1 A Left") 
  end
  if memory.read_s16_be(xCord)< (-3500) then  --checks x coordinate for left side
    button ("P1 A Right") 
  end
end

function recoverHigh(fun) --passes in recovery function specified
  if (memory.read_s16_be(yCord)<=(-15674) and memory.read_s16_be(yCord)>=(-15800))  and (memory.read_s16_be(xCord)>2000) then 
   button("P1 A Left")
   fun()
  end  
  if (memory.read_s16_be(yCord)<=(-15674) and memory.read_s16_be(yCord)>=(-15800)) and (memory.read_s16_be(xCord)<-2000) then   --checks y coordinate for left side
    button("P1 A Right")
    fun()
  end
end

function recoverLow(fun) --passes in recovery function specified
  
  if (memory.read_s16_be(yCord)<(0)) and  (memory.read_s16_be(yCord)>(-15180)) and (memory.read_s16_be(xCord)>0) then 
    button("P1 A Left")
    fun ()
  end  
  if (memory.read_s16_be(yCord)<(0)) and  (memory.read_s16_be(yCord)>(-15180)) and (memory.read_s16_be(xCord)<0) then   --checks y coordinate for left side
    button("P1 A Right")
    fun()
  end

end

function ledge()  --actions Mario performs when on the ledge
  if memory.read_s16_be(yCord)==(-15448) and (memory.read_s16_be(xCord)==(2399) or memory.read_s16_be(xCord)==(-2400))  then
    button("P1 A") end
end

function groundAttack()  --handles the attacks done when opponent is on the ground
  if (memory.read_s16_be(xCord)<2280 and memory.read_s16_be(xCord)>-2280) then
  if memory.read_s16_be(distance) < 580 and (memory.read_s16_be(p2Y)==(0)) then
    if math.random() <0.5 then SHAerial(30,"Down") else SmashAttack ("Forward") end
    end
  end
end

function airAttack() --handles the attacks done when opponent is in the air
  if (memory.read_s16_be(xCord)<2280 and memory.read_s16_be(xCord)>-2280) then
  if memory.read_s16_be(distance) < 650 and (memory.read_s16_be(p2Y)>(0)) then
    SmashAttack ("Up") end
  end
end

function stagePos()  --causes mario to move back near the center of the stage
   if (memory.read_s16_be(xCord)>1000) then
    button("P1 A Left") end
   if (memory.read_s16_be(xCord)<-1000) then
    button ("P1 A Right") end
  end

function platformCheck() --causes Mario to perform an action when on one of the platforms
  if (memory.read_s16_be(yCord)==17506) and ((memory.read_s16_be(xCord)>=-1820) and (memory.read_s16_be(xCord)<=-991)) then
    timer(5)
    button ("P1 A Down") end
  if (memory.read_s16_be(yCord)==17506) and ((memory.read_s16_be(xCord)>=991) and (memory.read_s16_be(xCord)<=1800)) then
    timer(5)
    button ("P1 A Down") end
  if (memory.read_s16_be(yCord)==17600) and ((memory.read_s16_be(xCord)>=-530) and (memory.read_s16_be(xCord)<=530)) then
    timer(5)
    button ("P1 A Down") end

end

while true do 
  platformCheck();
  stagePos();
  mRecovery();
  airAttack();
  groundAttack();
  emu.frameadvance();
end