#_*_coding:utf-8_*_
#Author：ymxowgk

age_of_boy = 23

count = 0

while count < 3:
    guess_age = int(input("guess age:"))
    if guess_age == age_of_boy:
        print("yes,you got it.")
        break
    elif guess_age > age_of_boy:
        print("think smaller...")
    elif guess_age < age_of_boy:
        print("think bigger...")
    count += 1
    if count == 3:
        continue_confirm = input("do you want to keep guessing..?")
        if continue_confirm != 'n':
            count = 0
#else:
#    print("you have tried too many times...fuck off")