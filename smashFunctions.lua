
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


