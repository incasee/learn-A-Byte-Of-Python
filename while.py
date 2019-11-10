number = 23
running = True
while running:
    guess = int(input('guess a number:'))
    if guess== number:
        print('厉害了')
        running = False
    elif guess < number:
        print('a little higher number')
    else:
        print('a little lower number')
print('完成')