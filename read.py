import argparse
import platform
import subprocess
import time



name_Os = platform.system()

print(name_Os)
if name_Os == 'Windows':
    parser = argparse.ArgumentParser()
    parser.add_argument("timeOfLive",type=int, help="display a square of a given number")
    parser.add_argument("-n", "--verbose", action="store_true", help="increase output verbosity")
    parser.add_argument("-path", action = 'append', help="display a square of a given number")

    args = parser.parse_args()
    timelive = args.timeOfLive

    if timelive > 100 or timelive < 0:
        print('Error')
    else:
        print("oK")
    run = args.path
    p = subprocess.Popen(run, shell=False)
    
    print('Run pid = ', p.pid)
    time.sleep(timelive)
    p.kill()
    

#answer = args.ti
#if args.verbose:
    #print("the square of {} equals {}".format(args.timeOfLive, answer))
#else:
    #print(answer)