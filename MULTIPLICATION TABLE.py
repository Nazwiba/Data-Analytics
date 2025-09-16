num = int(input("Enter the number of which you want the multiplication table: "))
print("Multiplication Table for", num)
for i in range(1,11):
    result = num * i
    print(num, "*",i, "=" , result)
