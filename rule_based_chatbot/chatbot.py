import re
import random
import datetime

chat_responses = {
    "greeting": ["hey what's up!", "hello there!", "hi manidhar how are you?"],
    "time": ["wait checking time..."],
    "joke": [
        "why do programmers like dark mode? light attracts bugs haha",
        "my computer said it was cold... windows were open",
        "how many coders to change a bulb? none thats hardware problem"
    ],
    "weather": [
        "vijayawada is sunny today bro perfect for coding ☀️",
        "andhra weather is nice no rain just hot vibes"
    ],
    "help": ["i can say hi, tell time, crack jokes, talk weather... ask anything"],
    "thanks": ["no problem bro!", "you're welcome 😊"],
    "bye": ["bye  see you later!", "ok bye keep coding 💻"]
}

def chatbot_reply(message):
    message = message.lower().strip()
    
    if re.search(r'\b(hi|hello|hey|namaste)\b', message):
        return random.choice(chat_responses["greeting"])
    
    elif re.search(r'\b(time|clock|what time)\b', message):
        now = datetime.datetime.now()
        return f"right now its {now.strftime('%I:%M %p')}"
    
    elif re.search(r'\b(joke|funny|tell joke)\b', message):
        return random.choice(chat_responses["joke"])
    
    elif re.search(r'\b(weather|how is weather|rain)\b', message):
        return random.choice(chat_responses["weather"])
    
    elif re.search(r'\b(help|what can you|commands)\b', message):
        return random.choice(chat_responses["help"])
    
    elif re.search(r'\b(thanks|thank you|good|nice)\b', message):
        return random.choice(chat_responses["thanks"])
    
    elif re.search(r'\b(bye|goodbye|quit|see you)\b', message):
        return random.choice(chat_responses["bye"])
    
    else:
        return "sorry didnt get that... try hi, joke, time, weather or bye"

print("say hello to bot let well it reply....")
print("-" * 40)

while True:
    you_said = input("You: ")
    
    if not you_said.strip():
        continue
        
    answer = chatbot_reply(you_said)
    print("Bot:", answer)
    
    if re.search(r'\b(bye|goodbye|quit)\b', you_said.lower()):
        print("chat ended... thanks!")
        break