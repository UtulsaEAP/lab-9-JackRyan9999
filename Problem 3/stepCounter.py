def feet_to_steps(user_feet):
   #write your code here
   return int(user_feet /2.5) 

if __name__ == '__main__':
    #take input feet steps here
    #store it into the function
   user_feet = float(input("Enter number of feet walked:"))

   steps = feet_to_steps(user_feet)

  
   print(steps)