number = 23
guess = int(input('enter a number:'))
if guess == number:
    print('厉害了')
elif guess < number:
    print('a little higher number')
else:
    print('a little lower number')
print('Done')