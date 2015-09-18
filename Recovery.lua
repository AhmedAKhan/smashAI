function upB ()
 local outputs = {}
  outputs ["P1 A Up"] =true
  joypad.set(outputs)
  outputs ["P1 B"] =true
  joypad.set(outputs)
end


function mRecovery ()  -- Mario Recovery

  local outputs = {}
  
  if (memory.read_s16_be(0x2EF050)>3500) then      --checks x coordinate for right side
    outputs["P1 A Left"]  = true
    joypad.set(outputs)
  end
  
  if (memory.read_s16_be(0x2EEFC8)<(0)) and  (memory.read_s16_be(0x2EEFC8)>(0-15180)) and (memory.read_s16_be(0x2EF050)>0) then 
    outputs["P1 A Left"]  = true    --checks Y co-ordinate for left
    joypad.set(outputs)
    upB()
  end
  
  if memory.read_s16_be(0x2EF050)< (0-3500) then  --checks x coordinate for left side
    outputs["P1 A Right"]  = true
    joypad.set(outputs)
  end
  
  if (memory.read_s16_be(0x2EEFC8)<(0)) and  (memory.read_s16_be(0x2EEFC8)>(0-15180)) and (memory.read_s16_be(0x2EF050)<0) then   --checks y coordinate for left side
    outputs["P1 A Right"]  = true  --checks Y co-ordinate for right
    joypad.set(outputs)
    upB()
  end


  
end



event.onframeend(mRecovery)
