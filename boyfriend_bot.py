# boyfriend_bot.py

""" Boyfriend bot will be a terminal window game that 

1) Allows the user to set up multiple boyfriends for the user. Your persons name and age will be setup via inputs.  
2) Then suggests when the user should text them and counts the number of texts sent to the user. 

Future features

1) Attachment styles that suggest different texts and frequencies depending on their attachment style
2) GUI with a reminder to text boyfriend/girlfriend along with a copy/paste of the message.
3) Randomly generated words of affirmation to send to your significant other.
4) Adds love languages for boyfriends and suggests types of activities or texts for each love language.

"""


boyfriends = []
attachment_styles = []

class Boyfriend:
    """" Creating the boyfriend class """
    def __init__(self, name, age, attachment_style, texts_received = 0):
        """ Initializes boyfriend attributes """
        self.name = name
        self.age = age
        self.attachment_style = attachment_style
        self.texts_received = texts_received
    
    def get_descriptive_name(self):
        descriptive_name = (f"{name}, {age}, {attachment_style}.")

    def text_boyfriend(self):
        print("It's time to text yours boyfriends!")
        print("\nWhich boyfriend would you like to text?)
        print(boyfriends)
        # select a boyfriend via input
        # write that boyfriend a text
        texts_received += 1


def new_boyfriend():


def describe_boyfriend(self):
    """ Returns a neatly formatted description of our new boyfriend """
    print(f"Alright. So our newest boyfriend is {name} who is {age} years old and has a {attachment_style}. Well done.")



# Establishing some boyfriends with inputs
boyfriend_0 = Boyfriend('input', 'input', 'input')
boyfriend_1 = Boyfriend('input', 'input', 'input')


print("Welcome to boyfriend bot!")
print("\nIn this program we're going to ask you about your current boyfriends and ask you their attachment styles. From there, we'll suggest when to send some texts to your boyfriend. If you like the texts, feel free to copy and paste them into your iMessage ^_^ He'll never know!")
print("\nSo let's get started. Tell me about your boyfriend (or boyfriends!)")


add_boyfriend(name = input, age = input, attachment_style, text_received = 0)
    print("What's your boyfriend's name?")