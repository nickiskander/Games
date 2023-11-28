import time
import random
name = input("What is your name? ")
print ("Hey, " + name, "U gonna lose!")
time.sleep(1)
print ("Start guessing...\n")
time.sleep(0.5)
#words = ['colossal','blasphemy','shenanigan','tomfoolery','goonery','diabolical','buckaroo',
        # 'flabbergast', 'abracadabra']
words = ['goonery']
word = random.choice(words)
guesses = ''
turns = 5
while turns > 0:         
    failed = 0             
    for char in word:      
        if char in guesses:    
            print (char,end="")    
        else:
            print ("_",end=""),     
            failed += 1    
    if failed == 0:        
        print ("\nYou won this time") 
        break              
    guess = input("\nguess a letter:") 
    guesses += guess                    
    if guess not in word:  
        turns -= 1        
        print("\nLMAO try again")    
        print("\nYou have", + turns, 'more guesses') 
        if turns == 0:           
            print ("\nYou Lose Stupid")
      