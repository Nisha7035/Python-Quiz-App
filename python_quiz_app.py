                                                 # python quize app

def quiz_app():
    questions =[
        "What is keyword to define a function in python?",
        "Which data type is used to store True or False?",
        "What symbol is used to start a comment in python?",
        "Which function is used to get input from user ?",
        "What is the index of the first element in python list?"
    ]
    answers = [
        'def',
        'bool',
        '#',
        'input',
        '0'
    ]
    score = 0
    for q,a in zip(questions,answers):
        user_ans = input(f"❓ {q}\n👉 your answer:")
        if user_ans.lower() == a.lower():
            print("✅ correct!")
            score +=1
        else:
            print(f"❌wrong! correct answer: {a}\n")
    print(f"🎯 your final score: {score}/{len(questions)}")

    # bonus feedback

    if score == len(questions):
        print("feedback: Excellent! you are a python pro!")
    elif score >= len(questions) * 0.6:
        print("feedback: good job! keep practicing.")
    else:
     print("feedback: try again! practice makes perfect.")

   # option to play again
   
    again =(input("\n do you want to play again? (yes\no):")).strip().lower()
    if again == "yes":
        quiz_app()
    else:
        print("bye thanks for playing ")


quiz_app()