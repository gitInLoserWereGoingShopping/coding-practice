import math
import os
import random
import re
import sys

def function(m):
    if m % 2 != 0:
        return "Weird"
    if m % 2 == 0 and m >= 2 and m <= 5:
        return "Not Weird" 
        
    if m % 2 == 0 and m >= 6 and m <= 20:
        return "Weird"
    else:
        return "Not Weird"
    

if __name__ == '__main__':
    n = int(input().strip())
    
print(function(n))
