def decimal_to_binary(n):
    if n==0:
        return"0"
    binary=""
    while n >0:
         binary=str(n%2)+binary
         n=n//2
    return binary

decimal=int(input("enter a decimal number:"))
binary=decimal_to_binary(decimal)
print("binary (manual method):", binary)
        