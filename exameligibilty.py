medical_cause=input("did you have a medical cause Y or N:")
atten=int(input("Enter the attendance of the student:"))

if medical_cause=='Y':
    print("you are allowed")
else:
    if atten>=75:
        print("allowed")
    else:
        print("not allowed")