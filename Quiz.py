#QUIZ APPLICATION

guesses=[]
correct_guesses=0
question_optn=1



questions={"Q1- which is the largest building in the world?: ": "C",
           "Q2-Dead Sea is located between which two countries?: ": "B",
           "Q3-who is the first indian to win a Nobel prize?: ": "A",
           "Q4-which country is also known as the 'Land of Rising sun'?: ": "D",
           "Q5-In which country, white elephant is found?:": "C",}


options=[["A.Shanghai Tower, B.Mardeka 118, C.Burj khalifa, D.Makkah Royal clock Tower"],
         ["A.Jordan and sudan, B.Jordan and israel, C.Turkey and UAE, D.UAE and Egypt"],
         ["A.Rabindranath Tagor, B.cv Raman, C.Mother Theresa, C.Hargobind Khorana"],
         ["A.New Zealand, B.Fijii, C.china, D.Japan",],
         ["A.Sri lanka, B.India, C.Thailand, D.Malaysia"]
        ]


for key in questions:
    print("*************")
    print(key)
    for choices in options[question_optn-1]:
        print(choices)
        question_optn=question_optn+1
        guess=input("Enter your choice of (instruction:A,B,C OR D):")
        guess=guess.upper()
        if guess==questions.get(key):
            correct_guesses=correct_guesses+20
            print("your score is out of 100:",+correct_guesses)

        else:
            print("please enter valid options")
            if correct_guesses==0:
                print("your score is Zero")





















