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

