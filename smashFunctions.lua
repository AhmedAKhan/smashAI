xCord=0x2EEF10
yCord=0x2EEE88
distance=0x18EB3C
p2Y=0x268984
p2X=0x2F3200
P1Dir=0x267DF6 
P2Dir=0x26942A


function button (n)  -- any game button (in quotations)
  local outputs = {}
  outputs[n]  = true
  joypad.set(outputs)
end

function timer(n)    --the number of frames you want to advance
  i = n
  while i>1 do
    i =i-1
    emu.frameadvance(); 
  end
end

function holdButton(n,b) --give the frames and the button press and it will execute it for that long
  i = n
  while i>1 do
    i =i-1
    emu.frameadvance(); 
    button(b)
  end
end

function SmashAttack(n)     --choose "Üp"" or "Down"
  holdButton (2,"P1 A "..n) -- if choose "forward" will do jabs
  button("P1 A")
end

function UPB()    --up B
  button("P1 A Up")
  button("P1 B")
end

function jUPb()   
  button ("P1 A Up")    --does a regular jump, then up B
  button("P1 A Left")
  timer(30)
  UPB()
end
                      
function dUPb(delay)   --Jumps and then delays by specified amount before up B
  button ("P1 A Up")
  button("P1 A Left")
  timer(delay)
  UPB()
end

function downB(dir)  --does a down B with max vertical height gain
  for i =1,10 do
    timer(5)
    button("P1 A Down")
    button("P1 A".. dir)
    button("P1 B")
  end
end

function dashAttack(dir)
  holdButton(10,dir)
  button("P1 A")
end


function SHAerial(n,dir) --specify which aerial you want Mario to do and when during the jump
  button("P1 C Up")
  timer(n)
  button("P1 A "..dir)
  button("P1 A")
  ZCancel()
end

function SHUpAir()
  button("P1 C Up")
  timer(4)
  button("P1 A Up")
  button ("P1 A")
end



function ZCancel ()      --reduces landing lag after an aerial to regular landing lag (4 frames)
  while memory.read_s16_be(yCord)>0 and memory.read_s16_be(yCord)<=18000 do
  if  memory.read_s16_be(yCord)>=17000 and memory.read_s16_be(yCord)<=17100 then
        button ("P1 Z") end
  emu.frameadvance() end
  timer(4)
end

function direction ()
  if memory.read_s16_be(xCord)>memory.read_s16_be(p2X) and memory.read_u16_be(P1Dir) <2 then
    button ("P1 A Left") 
  elseif memory.read_s16_be(xCord)<memory.read_s16_be(p2X) and memory.read_u16_be(P1Dir) >1000 then
    button ("P1 A Right") 
  end
end
