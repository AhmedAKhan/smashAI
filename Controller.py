import pipes
import time;


class Controller:
    def __init__(self, path):
        self.path = path;
        print("inside the constructor");

    def test(self):
        t = pipes.Template()
        t.append('tr a-z A-Z', '--')
        f = t.open(self.path+'/Pipes/cpu-level-11', 'w')
        f.write('PRESS B\n')
        time.sleep(2);
        f.close()


# if __name__ == '__main__':
    # main();

