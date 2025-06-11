print("welcome to my python project!!")
print("Let's start doing some Quiz!! ")

question_bank= [
    {"text": "Which state in India is known as the Land of the Rising Sun?" , "answer": "C"},
    {"text": "What is the largest city in India by population?","answer": "B"},
    {"text": "What is the capital of France?","answer": "D"},
    {"text": "How many continents are there in the world?","answer": "A"},
    {"text": "The name of the Artificial Intelligence system developed by Daniel Bobrow was?","answer": "C"},
    {"text":"The measure of performance of an AI agent is measured using?","answer":"A"}
]

options=[["A. Uttar pradesh" ,"B. Karnataka" ,"C. Arunachal pradesh" ,"D. Kerala "],
         ["A. Delhi" , "B. Mumbai" , "C. Hyderabad"," D. Banglore"],
         ["A.Berlin","B.Rome"," C.Madrid"," D.Paris"],
         ["A. 7","B. 6 "," C. 5" ," D. 8"],
         ["A. BACON" ," B. SIMD ", " C. STUDENT "," D. NONE OF THE ABOVE"],
         ["A. Learning Agent "," B. Changing Agent" , "C. Both A and B "," D. None of the above "]
]
score=0
def check_answer(user_guess,correct_answer):
    if user_guess==correct_answer:
       return True
    else:
        return False
        
for question_num in range(len(question_bank)):
    print("************************")
    print(question_bank[question_num]["text"])
    for i in options [question_num]:
        print(i)

    guess=input("enter your answer(A/B/C/D):").upper()
    is_correct=check_answer(guess, question_bank[question_num]["answer"])

    if is_correct:
       print("Correct answer")
       score += 1
    else:
       print("Incorrect answer")
       print(f"the correct answer is {question_bank[question_num]['answer']}")

print(f"You have given {score} correct answer")
print(f"Your Score is {(score/len(question_bank))*100}%")
