# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def study_chatbot():
    print("Hi! I am your study chatbot.")
    print("You can talk to me about studying.")
    print("Type bye when you want to leave.")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("Bot: Hi! How is your study going?")

        elif user == "how is my study":
            print("Bot: Keep practicing and try to study a little every day.")

        elif user == "i need help":
            print("Bot: Sure! Tell me which subject you want to study.")

        elif user == "i am tired":
            print("Bot: Take a short break and then continue your study.")

        elif user == "what should i study":
            print("Bot: You can start with the subject you find difficult.")

        elif user == "thank you":
            print("Bot: You are welcome. Good luck with your studies!")

        elif user == "bye":
            print("Bot: Bye! Good luck with your studies.")
            break

        else:
            print("Bot: I don't have an answer for that yet.")


study_chatbot()