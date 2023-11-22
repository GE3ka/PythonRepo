# Basic - Print all integers from 0 to 150.
print("Basic - Print all integers from 0 to 150")
for i in range(151):
    print(i)

#Multiples of Five - Print all the multiples of 5 from 5 to 1,000
print("Multiples of Five - Print all the multiples of 5 from 5 to 1,000")
for i in range(1,1001):
    if i%5==0:
        print(i)
    else:
        continue    

#Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, 
# print "Coding" instead. If divisible by 10, print "Coding Dojo".
print("Counting, the Dojo Way")
for i in range (1,101):
    if i%5==0:
        if i%10==0:
            print ("Coding Dojo")
            continue
        print("Coding")    
    else:
        print (i)    

#Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
print ("Whoa. That Sucker's Huge")
sum=0
for i in range(500001):
    if i%2==0:
        sum += i
        continue
    else:
        continue
print("the sum of all odd integers from 0 to 500,000 = ", sum )

# Countdown by Fours: Print positive numbers starting at 2018, counting down by fours.
print("Countdown by Fours")
for i in range(2018,0,-4):
    print(i)

#Flexible Counter
#Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. 
# For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

print("Flexible Counter")
lowNum=2
highNum=9
mult=3

for i in range (lowNum,highNum+1,1):
    if i%mult==0:
        print(i)
