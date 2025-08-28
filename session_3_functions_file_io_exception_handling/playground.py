
# Generate list
# process list data

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = []
for num in l1 :
    squares.append(num*num)
print(squares)

squares = [num*num for num in l1]
print(squares)

squares = [num*num for num in l1 if num%2==0]
print(squares)

squares = [num*num if num % 2 == 0 else num+num for num in l1]
print(squares)

squares = [num if num in (2, 3, 5, 7)
            else num*num if num % 2 == 0
            else num + num
           for num in l1]
print(squares)












