# Rulebased AI Python ChatBot

import datetime
import time

name = input("Swagat h, enter your name : ")
presentHour = datetime.datetime.now().hour

if 5 <= presentHour <= 11:
    print("Good morining,", name)
elif 11 <= presentHour <= 17:
    print("Good afternoon, ", name)
elif 17 <= presentHour <= 20:
    print("Good evening ,", name)
else:
    print("Good night,",name)

print("Welcome to Rule Based ChatBot")
print("You can ask me basic questions. Type 'bye' to exit from the bot.")

# Chatbot Memory Creation (Dictionary of Responses)

responses = {
    "hello": "Hi! Welcome. How can I help you?",
    "how are you": "I am very fine. Thank you!",
    "who are you": "I am a smart AI chatbot.",
    "motivate me": "Keep going. Every bug in your project makes you better.",
    "happy": "Great to hear that!",
    "function kya hota hai": "Jakar Chapter 7 padho."
}

# Function to get response from chatbot

def getResponseOfBot(userQuestion):
    userQuestion = userQuestion.lower()

    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]

    return "I am not able to tell that yet. I will learn very soon."

# Take user input

while True:
    userInput = input("Please ask your question: ")

    # Exit condition
    if "bye" in userInput.lower():
        print("Bot Response: Goodbye! Have a nice day.")
        break

    reply = getResponseOfBot(userInput)
    print("Bot Response:", reply)