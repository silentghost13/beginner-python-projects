import random
#https://www.youtube.com/watch?v=SqvVm3QiQVk&t=40s
def rpg(number, length):
    
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*?'
    
    for p in range (number):
        password = ''
        for l in range(length):
            password += random.choice(chars)
        print(password)

if __name__ == '__main__':
    print('Random Password Generator\n')
    
    number = input('Enter amount of password to generate: ')
    number = int(number)
    
    length = input('Enter length of password to generate: ')
    length = int(length)
    
    print('\nYour password: ')
    
    rpg(number, length)
    
   
    