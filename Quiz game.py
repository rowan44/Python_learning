def new_game():

    guesses=[]
    correct_guesses = 0
    question_num = 1

    for key in question:
        print("------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess= input("Enter (A,B,C,D) : ")
        guess=guess.upper()
        guesses.append(guess)
        correct_guesses += check_answer(question.get(key),guess)
        question_num +=1
        display_score(correct_guesses,guesses)


def check_answer(answer,guess):

    if answer == guess:
        print("Correct")
        return 1
    else:
        print("Wrong!")
        return 0

def display_score(correct_guesses,guesses):
        print("-------------------")
        print("RESULTS")
        print("-------------------")
        print("Answer: " , end=" ")

        for i in question:
            print(question.get(i) , end=" ")
            print()


        print("Guesses: ", end=" ")
        for i in guesses:
            print(i , end=" ")
        print()


        score =int((correct_guesses/len(question))*100)
        print("Your score is :"+str(score)+"%")

def play_again():
    responce = input("Do you want to play again? (yes or no): ")
    responce =responce.upper()
    if responce == "YES":
        return True
    else:
        return False




question = {
"Who created Python ? :":"A",
"What year was python created ? :":"B",
"Python is tributed to which comedy group? : ":"C",
"Is the earth round?:":"A"
}

options =[["A. Guido Van Rossum","B.Elon Musk","C.Bill Gates","D.Mark Zuckerburg"],
         ["A.1989","B.1991","C.2000","D.2016"],
         ["A.Lonely Island","B.Smosh","C.Monty Python","D.SNL"],
          ["A.True","B.False","C.sometimes","D.What's earth?"]
         ]

new_game()
while play_again():
    new_game()

print("Byeeeeee!")