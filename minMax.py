def minMax(arr:list):
    if arr or len(arr)==0:
       return None,None
     minval=arr[0]
     maxval=arr[0]
     for i in range(1, len(arr)):
        if arr[i]< arr[0]:
            minval=arr[i]
        if arr[i] > arr[0]:
            maxval=arr[i]
     return minval,maxval

minMax([29,4,50,9,44,3,98,2])
print("Minval=",minval "+" "maxval=",maxval)     
