#python3

import sys
import threading
from array import array



def compute_height(n, parents):
    l = list(range(n))
    arr = array("i", l)
    parents = parents.split()
    parents = map(int, parents)
    parents = list(parents)
    s=0
    x=0
    height=1
    max_height=0
    for i in parents:
        arr[x] = i
        x=x+1
    x=0
    while(True):
        x=arr[x]
        
        if s==(n-1):
            max_height=max(max_height, height)
            return max_height
        elif x==-1:
            s=s+1
            max_height=max(max_height, height)
            height = 1
            x=s
            continue      
        else:
            height = height +1    




def main():
    text = input()
    if "I" in text:
        n= int(input())
        parents= input()
    elif "F" in text:
        text2 = input()
        if "a" in text2:
            return()
        with open ("test/"+text2, encoding="utf-8") as fails:
            n = int (fails.readline())
            parents = fails.readline()
    else:
        return()
    result = compute_height(n, parents)
    print(result)
# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()