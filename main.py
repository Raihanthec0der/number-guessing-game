import random
select_number=random.randint(1,10)
while True:
    guess=int (input("Enter your guess: "))
    if guess < select_number:
        print("Too L...O...W!")
    elif guess > select_number:
        print("Too H...I...G...H")
    else:
        print("Y***o***u W***I***N")
        break