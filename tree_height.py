# python3
import numpy



def compute_height(n, parents):
    arr = numpy.array(range(n))
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
    # text = input()
    # if "I" in text:
    #     n= int(input())
    # elif "F" in text:
    #     pass
    # else:
    #     return()
    # parents= input()
    # result = compute_height(n, parents)
    # print(result)
    text = input()
    if "F" in text:
        text2 = input()
    else:
        return()
    if "a" in text2:
        return()
    with open ("test/"+text2, encoding="utf-8") as fails:
        n = int (fails.readline())
        parents = fails.readline()
    result = compute_height(n, parents)
    print(result)
main()
