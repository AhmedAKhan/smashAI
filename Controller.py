import pipes
import time;

"""
    self.pipe = this is variable that is the pipe, you can write to it, or read to it and it will write to the file
    self.path = the location to where the dolphin folder is inside the computer
"""

class Controller:
    def __init__(self, path):
        self.path = path;
        pipeTemplate = pipes.Template()
        pipeTemplate.append('tr a-z A-Z', '--')
        self.pipe = pipeTemplate.open(self.path+'/Pipes/cpu-level-11', 'w')

    def test(self, txt):
        self.pipe.write(txt)
        time.sleep(2);
        print(self.pipe);
        print(type(self.pipe));
        self.pipe.close()


def test():
    pipeTemplate = pipes.Template()
    pipeTemplate.append('tr a-z A-Z', '--')
    pipe = pipeTemplate.open('./testp','w', )
    time.sleep(2);
    # pipe.append("asasdsad");
    time.sleep(2);
    pipe.close();
    print("just closed the pipe");
    return;



if __name__ == '__main__':
    test();

