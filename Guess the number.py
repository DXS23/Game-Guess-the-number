import random
count = 0

print('Добро пожаловать в числовую угадайку!')
p = int(input('Введите правую границу диапазона: '))
print('Попробуйте угадать число от 1 до', p)
x = random.randint(1, p)
def is_valid(num):
    if num.isdigit() and 1 <= int(num) <= p:
        return True
    else:
        return False
    
while True: 
    s = input('Введите целое число: ')
    
    if is_valid(s) == False:
        print('А может быть все-таки введем целое число от 1 до', p, '?')
    else:
        n = int(s)
        if n < x:
            count += 1
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif n > x:
            count += 1
            print('Ваше число больше загаданного, попробуйте еще разок')
        elif n == x:
            count += 1
            print('Вы угадали, поздравляем!')
            print('Число попыток:', count)
            new_game = input('Хотите сыграть в новую игру? (да или нет) ')
            if new_game.lower() == 'да' or new_game.lower() == 'yes':
                is_valid(s)
            else:
                print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
                break
    
    
    
        
        
        