print("Enter marks obtained in 5 subjects")
mark1= int(input())
mark2= int(input())
mark3= int(input())
mark4= int(input())
mark5= int(input())

tot= mark1+mark2+mark3+mark4+mark5
avg=tot/5

if avg>=91 and avg <=100:
    print("Your grade is a1")
elif avg>=81 and avg<91:
    print("Your grade is a2")
elif avg>=71 and avg<81:
    print("your grade is B1")
else:
    print("your grade is B2")