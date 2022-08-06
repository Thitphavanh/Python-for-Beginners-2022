print('Hello World')

# List
msg = 'Hello World'
print(msg)
bikes = ['trek', 'redline', 'giant']
# print(bikes[0])
# print(bikes[-1])

for bike in bikes:
    print(bike)

bikes = []
bikes.append('trek')
bikes.append('redline')
bikes.append('giant')

squares = []
# for x in range(1, 11):
#     squares.append(x**2)
# print(squares)

squares = [x**2 for x in range(1, 11)]
# print(squares)
# print(squares[:2])
# print(squares[:])

squares[1] = 99
# print(squares)

x = 30
x == 42
print(x == 42)
x != 42
print(x != 42)
x > 42
print(x > 42)
x >= 42
print(x >= 42)
x < 42
print(x < 42)
x <= 42
print(x <= 42)

game_active=True
if game_active:
    print('Is playing game')
    
# s playing game
def iftest(age):
    if age<4:
        ticket = 0
    elif age <18:
        ticket = 10
    else:
        ticket = 15
    print('Price : {} LAK'.format(ticket))
    
    
iftest(50)
iftest(5)
iftest(3)



        