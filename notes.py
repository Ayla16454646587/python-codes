amount=int(input("Enter an amount"))
note1=amount//100
note2=(amount%100)//50
note3=((amount%100)%50)//10
print("notes of 100 rupees are",note1)
print("notes of 50 rupees are", note2)
print("notes of 10 rupees are",note3)
