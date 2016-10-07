# import random library

import random

# All of the fortune tellers response

response = ['Working on something will focus your thoughts.',
            'Look on google, there the answer will lie.', 'Ask someone you know.',
            'Let your mind wander.',
            'New hobbies will occupy your time.',
            'No reason to stress.',
            'Getting started, as soon as possible.', 'Tomorrow sometimes is better than today.',
            'There in the essence is life, focus on the future.',
            'Find another reason, and move accordingly.', 'Assume nothing, you will do better that way.',
            'Those close can always help when asked.',
            'Somethings are better left unknown.', 'Be positive, change your perspective.', 'Nothing to do but wait and see.',
            'Being present is all that is required.', 'Today...whatever it means to you.', 'Unlikely anything could be so precise.', 'Within yourself more will be found.']


# print instructions and choose response

print("This program is a fortune teller. Ask a question...find your fortune.\n")

question = raw_input("What is your question?\n")

print(random.choice(response))
