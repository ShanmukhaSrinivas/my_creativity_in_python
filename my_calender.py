s = 0 #initializing a variable to add required values

day = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'] #storing weekdays in a list

lt = {'01':0,'02':3,'03':3,'04':6,'05':1,'06':4,'07':6,'08':2,'09':5,'10':0,'11':3,'12':5} #dictionary which stores values for each month

x=input('Enter the date in dd/mm/yyyy format: ') #getting input

s += int(x[:2])+lt[x[3:5]]+int(x[-2:])+int((int(x[-2:])/2)) #appling the logic

ce = int(x[-4:-2]) #storing century-1 value in a variable

s += {0:6,1:4,2:2,3:0}.get(ce,0) #switch-case in python

if (x[3:5]=='01' or '02') and (int(x[-4:])%4==0): #Leap year
    print(day[s%7])

else:                                             #Normal year
    print(day[(s%7)+1])
