import time
try:
    print("Please Enter less than 24 hours")
    Hour=int(input("Enter the time of the hour : "))
    Accurate =int(input("Enter the time in minutes :"))
    if Hour > 23 or Accurate > 59:
        print("Please enter less than 24 hours ❗")
    else:    
        for hour in range(Hour,0-1,-1):
            for x in range (Accurate    ,0-1,-1):
                for y in range (59,
                0,-1):
      
                    print("                "+str(hour)+":"+str(x)+":"+str(y),"",end="\r")
                    
                    time.sleep (1)
except:
    print("Please Enter time ⌚")
