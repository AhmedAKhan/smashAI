

p2yads = 0x268ac4
p2xads = 0x268ac0

function timer(n)    --the number of frames you want to advance
  i = n
  while i>1 do
    i =i-1
    emu.frameadvance(); 
  end
end

while true do 
  p2y = memory.read_s16_be(p2yads)
  p2IsJumping = bit.rshift(p2y, 14)
  p2YPos = bit.band(p2y, 0xFFF)	
  console.write('p2IsJumping: ', p2IsJumping, ' p2YPos: ', p2YPos, '\n');
  --timer(15)
  emu.frameadvance();
end