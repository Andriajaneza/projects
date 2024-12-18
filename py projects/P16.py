# AI chatbot

import random
import time

def chatbot():
    print("Chatbot: Hi! How can I assist you today?")
    
    while True:
        user_input = input("You: ")
        
        time.sleep(0.4)

        if user_input in ["hi", "hello", "hey"]:
            responses = ["Hello!", "Hi there!", "Hey!"]
            print("Chatbot:", random.choice(responses))
        
        elif user_input in ["how are you", "how's it going"]:
            responses = ["I'm doing great, thanks!", "I'm good, how about you?"]
            print("Chatbot:", random.choice(responses))
        
        elif user_input in ["bye", "goodbye", "see you"]:
            responses = ["Goodbye!", "See you later!", "Take care!"]
            print("Chatbot:", random.choice(responses))
        
        elif user_input in ["what is your name", "who are you"]:
            responses = ["I'm a friendly chatbot!", "I'm janezGPT, here to help!"]
            print("Chatbot:", random.choice(responses))
        
        elif user_input in ["tell me a joke", "make me laugh"]:
            responses = [
                "Why don't skeletons fight each other? They don't have the guts!",
                "Why did the scarecrow win an award? Because he was outstanding in his field!"
            ]
            print("Chatbot:", random.choice(responses))
        
        elif user_input in ["what's up", "what's going on"]:
            responses = ["Not much, just chatting with you!", "Everything's good, how about you?"]
            print("Chatbot:", random.choice(responses))
        
        elif user_input in ["thank you", "thanks"]:
            responses = ["You're welcome!", "Glad I could help!"]
            print("Chatbot:", random.choice(responses))
        
        elif user_input in ["sorry", "my bad"]:
            responses = ["No worries!", "It's okay!"]
            print("Chatbot:", random.choice(responses))
        
        elif user_input in ["how old are you", "what's your age"]:
            responses = ["I don't age, I'm just a bot!", "I was created recently, so I'm new!"]
            print("Chatbot:", random.choice(responses))
        
        elif user_input in ["what can you do", "what are your abilities"]:
            responses = ["I can chat with you, tell jokes, and answer questions!", "I'm here to help with anything you need!"]
            print("Chatbot:", random.choice(responses))
        
        elif user_input in ["where are you from", "where do you live"]:
            responses = ["I live in the cloud!", "I exist online, not tied to a specific place."]
            print("Chatbot:", random.choice(responses))
        
        elif user_input in ["do you have a favorite color", "what's your favorite color"]:
            responses = ["I don't have a favorite, but blue seems popular!", "I think all colors are great!"]
            print("Chatbot:", random.choice(responses))
        
        elif user_input in ["can you sing", "do you sing"]:
            responses = ["I can't sing, but I can share lyrics!", "I don't have a voice, but I can tell you a song title!"]
            print("Chatbot:", random.choice(responses))
        
        elif user_input in ["can you dance", "do you know how to dance"]:
            responses = ["I don't have a body, but I can share dance moves in emoji!", "I can't dance, but I can share dance videos."]
            print("Chatbot:", random.choice(responses))
        
        elif user_input in ["good morning", "morning"]:
            responses = ["Good morning! How can I assist you?", "Morning! What's up?"]
            print("Chatbot:", random.choice(responses))
        
        elif user_input in ["good night", "night"]:
            responses = ["Good night! Sleep well!", "Sweet dreams!"]
            print("Chatbot:", random.choice(responses))
        
        elif user_input in ["what's the time", "tell me the time"]:
            from datetime import datetime
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print("Chatbot: The current time is", current_time)
        
        elif user_input in ["what is love", "define love"]:
            responses = ["Love is a deep emotional connection between people.", "Love is when you care for someone deeply."]
            print("Chatbot:", random.choice(responses))
        
        elif user_input in ["can you help me", "help me"]:
            responses = ["Of course! What do you need help with?", "I'm here to assist, just let me know!"]
            print("Chatbot:", random.choice(responses))
        
        else:
            print("Chatbot: Sorry, I didn't understand that. Could you try again?")
            
chatbot()
