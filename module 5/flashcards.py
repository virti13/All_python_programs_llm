# Flashcards program

flashcards = {
    "What is the capital of India?": "New Delhi",
    "What is 2 + 2?": "4",
    "What is the color of the sky?": "Blue"
}

for question, answer in flashcards.items():
    print("Question:", question)
    user_answer = input("Your answer: ")

    if user_answer.lower() == answer.lower():
        print("Correct!")
    else:
        print("Wrong! The answer is", answer)

    print()