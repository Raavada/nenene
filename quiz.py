import logging
import unittest
import sys

def print2largest(arr):   
    
    try: 
      logging.info("print2largest!")
      setFlag = True  
      arr_size = len(arr)
       # There should be atleast
        # two elements
      if (arr_size < 2):     
        #print(" Invalid Input ")
         logging.info("List is smaller!")
         return -1
        
     # arr = str_list_to_int_list(arr)   
      # Check for smae elements in the list
      arr = list(set(arr))
      if (len(arr) < 2):
        logging.info("list contains all repeated elements!")      
        return -1                     

      arr_size = len(arr)
      first = second = -9223372036854775807 
      for i in range(arr_size):

          if(len(arr[i])>1024):
                logging.info("Maximum length of a single element can be 1024 digits.")
                setFlag = False
                return 0
                #break             
      
          # If current element is
                  # smaller than first
          # then update both
                  # first and second
              
          elif (int(arr[i]) > first):
          
              second = first
              first = int(arr[i])
          
  
          # If arr[i] is in
                  # between first and
          # second then update second
          elif (int(arr[i]) > second and int(arr[i]) != first):
              second = int(arr[i])
    except Exception as e:   
          print(e)       
          logging.exception("Exception occurred")
     
    if (second == -2147483648):
        return -1
    elif setFlag:
        print("The second largest element is", second)
        logging.info("second largest number!",second)
        return second

results =  ["-214748364801","-214748364802"]
print2largest(results)