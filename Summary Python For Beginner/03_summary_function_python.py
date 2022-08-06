
def money(m):
    for i in range(10):
        mv = input('Enter money')
        if int(mv) > 100000 :
            print('Can buy anymore things')
        else:
            print('Can buy 5 cups of coffee')
'''        
# money('')
current_value = 1
while current_value <=5:
    print(current_value)
    current_value += 1
    print(current_value)
    
msg=''
while msg != 'quit':
    msg = input('What is your message?')
    print(msg)
'''   
    
def greet_user():
    print('Hello')
    
greet_user()

def greet_user(friend):
    print('Hello'+friend)
    
# greet_user('Hery')

def make_pizza(topping='bacon'):
    print('Have a ' + topping + 'pizza')

