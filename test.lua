
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


function donothing()
  i = ggg
  console.writeline("inside donothing")
end

console.writeline("going to print the event ")
console.writeline(event)
console.writeline('going to call onexit')
event.onexit(timer)

while true do 
  emu.frameadvance(); 
end 
