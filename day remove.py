import pandas as pd
# the date is like (mm.dd.yyyy)

df=pd.read_csv(r"")

#The month you want to work whith it:
monthwork=input("enter the month :")

user_input=""
user_input_list=[]

while user_input !="q":
    user_input=input("enter a day to remove to quit press q: ")

    if user_input=="q":
        break
    user_input_list.append(str(user_input))


# input a day to start: you can't start from a removed day 
list1=[]
total= int(input("enter a day to start: "))
list1.append(str(total))

for i in range(0,6): 
   total += 1 
   list1.append(str(total))

result = [x for x in list1 if x not in user_input_list]

# add zero to the list
size = 7-len(result) 

for _ in range(size):
    result.append("0")
result1=int(result[0])
# print the lists to see which day you work whith: 
print(user_input_list)
print(list1)
print(result)
print(size)

# This just to avoid error in the first 10 days:
if result1<=10:
    df1 = df[df["DATE"]==f"{monthwork}.0{result[0]}.2026" ]  
    df2 = df[df["DATE"]==f"{monthwork}.0{result[1]}.2026" ]
    df3 = df[df["DATE"]==f"{monthwork}.0{result[2]}.2026" ]
    df4 = df[df["DATE"]==f"{monthwork}.0{result[3]}.2026" ]
    df5 = df[df["DATE"]==f"{monthwork}.0{result[4]}.2026" ]
    df6 = df[df["DATE"]==f"{monthwork}.0{result[5]}.2026" ]
    df7 = df[df["DATE"]==f"{monthwork}.0{result[6]}.2026" ]
else :
    df1 = df[df["DATE"]==f"{monthwork}.{result[0]}.2026" ]  
    df2 = df[df["DATE"]==f"{monthwork}.{result[1]}.2026" ]
    df3 = df[df["DATE"]==f"{monthwork}.{result[2]}.2026" ]
    df4 = df[df["DATE"]==f"{monthwork}.{result[3]}.2026" ]
    df5 = df[df["DATE"]==f"{monthwork}.{result[4]}.2026" ]
    df6 = df[df["DATE"]==f"{monthwork}.{result[5]}.2026" ]
    df7 = df[df["DATE"]==f"{monthwork}.{result[6]}.2026" ]