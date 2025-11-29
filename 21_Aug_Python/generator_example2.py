square_numbers = (i*i for i in range(1,7))
print(next(square_numbers))
print(next(square_numbers))
print("With loop")
for i in square_numbers:
    print(i)

