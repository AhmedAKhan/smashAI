
from pymouse import PyMouse
from pykeyboard import PyKeyboard
from time import sleep

m = PyMouse()
k = PyKeyboard()

## i placed a text editor in the middle of the screen and this clicked the text editor and then wrote hello world
##x_dim, y_dim = m.screen_size()
##m.click(x_dim/2, y_dim/2, 1) ## makes it so it clicks the middle of the screen
##k.type_string('Hello, World!') ##write hello world


##x_dim, y_dim = m.screen_size()
##m.click(x_dim/2, y_dim/2, 1) 
##k.press_key('o')
##print 'pressed the middle of the screen going to wait 1 seconds'
##sleep(1)
##print 'going to press the key d'
##k.tap_key('d')



##x_dim, y_dim = m.screen_size()
print ('about to click')
m.click(131, 289) ##x_dim/2, y_dim/2, 1) 
m.click(131, 289) ##x_dim/2, y_dim/2, 1) 
print ('going to press the key D')
k.tap_key('O')
sleep(1)
k.release_key('D')
sleep(2)
k.release_key('D')
print ('ending code')
