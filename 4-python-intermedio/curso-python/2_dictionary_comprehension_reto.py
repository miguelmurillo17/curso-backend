from __future__ import print_function
import math
#import statistics

def run():
    my_dict = {i: math.sqrt(i) for i in range(1,1001)}
    print(my_dict)
        

if __name__ == '__main__':
    run()