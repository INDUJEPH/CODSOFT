def chatbot():
    print("ChatBot: Hello")
    print("ChatBot: I am simple chatbot")
    print("ChatBot: Type exit to stop\n")

    while True:
        user = input("You:").lower()

        if user == "exit":
            print("ChatBot:Bye")
            break

        elif "hello" in user or "hi" in user:
            print("ChatBot:Hello, how can I help")

        elif "how are you" in user:
            print("ChatBot:I am fine, thank you")

        elif "your name" in user:
            print("ChatBot:My name is ChatBot")

        elif "help" in user:
            print("ChatBot: You can ask simple questions")

        elif "bye" in user or "by" in user:
            print("ChatBot:Bye bye")
            break

        else:
            print("ChatBot:Sorry I not understand")


chatbot()
