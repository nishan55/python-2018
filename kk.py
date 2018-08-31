import random
import time

answer = True 
responses = ["it is certain.", "it is decidedly so.", "without a doubt.",
             "yes - definitely.", "you may reply on it.", "As i see it yes.",
             "Most likely.","Outlook good.", "Signs point to yes.", "Ask again later.",
             "Better not tell you now.", "Cannot Predict now.",
             "Concentrate and ask again.", "Don't count on it., My reply is no.",
             "my sources say no.", "Outlook not not so good.", "Very doubtful."]
name = input("What is your name?")
while True:
    question = input("Ask the magic 8 ball a question " + name + ")
