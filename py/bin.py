# bin.py
# Saranii Muller
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: Kate Maschmeyer & pythonfu
#   Implement a binary search as specified by the comments
       
#        This algorithm only works on sorted ArrayLists.
#   

# 	 create assign variables  representing the high, low and middle indices 
# 	 while we're not done:
# 	 if the item is at data.get(middle), return middle
# 	 otherwise, update high, low, and middle

#   
#   - step 1: Assume list is sorted
#   - step 2: set low, set high. find mid
#   - step 3: if # is more than mid, set middle +1 to low and find new mid like in 2 rinse repeat until middle low and high ar eall the same

#   sorting method called sort
# 
def binSearch(data, value):  
  low = 0; #setting low index to be 0
  
  high = len(data) - 1    #setting high to highest index of arraylist
  while(low != high):#creates loop until
    mid = int((high + low)/2) #sets mid continually
    if(data[mid] == value): #if the value we are looking for is the mid then return the mid - setting truth first
    
      return mid
    
    elif (data[mid] < value): #if the mid is less than the value, change the low to one above the current mid
      low = mid + 1
    
    else: 
      high = mid - 1 #for when value is less then mid, get rid of the high
  
  #exit loop
  if(data[high] == value):  #if high == value then the value exists in the array
    return high #return the index of the value
  
  return -1 #value does not exist in the array thus -1

dataTest = [1,6,7,9,12,16,19,25]
print (binSearch(dataTest,16)) 