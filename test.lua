
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

function SmashAttack(n)
  holdButton (2,"P1 A "..n)
  button("P1 A")
end


function donothing()
  i = ggg
  console.writeline("inside donothing")
end

function button1 ()  -- any game button (in quotations)
  if memory.read_s16_be(0x2EF050)>0 then 
    local outputs = {}
    outputs["P1 A Left"]  = true
    joypad.set(outputs)
  end
end

function button3 ()  -- any game button (in quotations)
  if memory.read_s16_be(0x2EF050)<0 then 
    local outputs = {}
    outputs["P1 A Right"]  = true
    joypad.set(outputs)
  end
end

function button2 ()  -- any game button (in quotations)
  
    local outputs = {}
    outputs["P1 A"]  = true
    joypad.set(outputs)
  
end

console.writeline(memory.read_s16_be(0x2EF050))

--button2()


event.onframeend(button1)
event.onframeend(button3)