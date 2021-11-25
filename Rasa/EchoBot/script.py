import random
import re



bot_template = 'BOT : {0}'
user_template = 'USER : {0}'

# Define variables
name = "Greg"
weather = "cloudy"

# Define a dictionary with the predefined responses
responses = {
  "what's your name?": "my name is {0}".format(name),
  "what's today's weather?": "the weather is {0}".format(weather),
  "default": "default message"
}

# define a fuction tht responds to a user's message: respond
def respond(message):
    # concatenate the user's message to the end of standard bot response
    bot_message = 'I can hear you! you said : ' + message
    return bot_message

# Define a function that sends a message to the bot: send_message
def send_message(message):
    # Print user_template including the user_message
    print(user_template.format(message))
    # Get the bot's response to the message
    response = respond(message)
    # Print the bot template including the bot's response.
    print(bot_template.format(response))


def respond(message):
    # Check for a question mark
    if message.endswith("?"):
        # Return a random question
        return random.choice(responses["statement"])
    # Return a random statement
    return random.choice(responses["question"])


# Send messages ending in a question mark
send_message("what's today's weather?")
send_message("what's today's weather?")

# Send messages which don't end with a question mark
send_message("I love building chatbots")
send_message("I love building chatbots")