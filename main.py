import random
# Input statements
lowestnumber = int(input("Enter the Lowest Number: "))
largestnumber = int(input("Enter the Largest Number: "))
player_name = input("Please let me know your name. You can use an imaginary name as well. ")
number_of_guesses = int(input("How many Guesses do u need? "))
# random works
selectednumber = random.randint(lowestnumber, largestnumber)
# cannot find the title
print('okay! '+ player_name+ f' I am Guessing a number between {lowestnumber} and {largestnumber}')
noofguess = 0
# actual function
while noofguess <= number_of_guesses:
    guess = int(input())
    noofguess += 1
    if guess < selectednumber:
        print('Your guess is too low')
    if guess > selectednumber:
        print('Your guess is too high')
    if guess == selectednumber:
        break
if guess == selectednumber:
    print('You guessed the number in ' + str(noofguess) + ' tries!')
else:
    print('You failed. The number was ' + str(selectednumber))
