import pipes
import time;

def main():
    t = pipes.Template()
    t.append('tr a-z A-Z', '--')
    f = t.open('/Users/ahmed/Library/Application Support/Dolphin/Pipes/cpu-level-11', 'w')
    f.write('PRESS B\n')
    time.sleep(2);
    f.close()


if __name__ == '__main__':
    main();

