#------------------ WARNING ----------------------#
# PLEASE DO NOT TRY TO ADJUST THIS CODE ELSE YOU
# WILL FACE ISSUES, PLEASE CONTACT THE PROGRAMMER
# VICTOR WILKIS @ +2348165335909 IF YOU WANT SOME
# CHANGES OR AN UPGRADE TO BE DONE.
#-------------------------------------------------#
name= input(f'''
|-----------------------------------------------|
    Please Enter Your Name To Proceed For 
    Your Maths Test
|-----------------------------------------------|
''')
print(f'''
---------------------------------------------
    WELCOME {name.upper()}
    wish you best of luck in your maths test
---------------------------------------------
''')
time_taken=[]
no_correct=[]
not_correct= []
start=1
from datetime import datetime
from random import randrange
while start<=5:
    num1=randrange(10,100)
    num2=randrange(10,100)
    begin= datetime.now()
    feedback= int(input(f'{num1} + {num2} = ?\n'))    
    end= datetime.now()
    dif= end-begin
    if feedback==num1+num2:
        time_taken.append(dif.seconds)
        no_correct.append(1)
    else:
        time_taken.append(20)
        no_correct.append(0)
        not_correct.append(1)
    start+=1
res= (f''''
                [ {name.upper()} TEST RESULT ]
|-------------------------------------------------------|
    you answered => Five questions
    Number of Correct Answers => {sum(no_correct)}
    Number of InCorrect Answers => {sum(not_correct)}
    Time Taken => {sum(time_taken)} Seconds
|-------------------------------------------------------|
''')
file_w = open('TEST RESULT.txt','w')
file_w.write(res) 
file_w.close()

print(res)

#==========================================================#
   #DATE CREATED: 4TH DECEMBER 2020
#==========================================================#
input()