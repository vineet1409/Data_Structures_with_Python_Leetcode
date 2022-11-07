class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self,arr,D,N):
        p = 1
        while(p<=D):
            last = arr[0]
            for i in range(len(arr) -1):
                arr[i] = arr[i+1]
            arr[N-1] = last
            p+=1
        
        return arr