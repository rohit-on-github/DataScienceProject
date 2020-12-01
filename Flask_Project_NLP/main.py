from flask import Flask
from spellchecker import SpellChecker

app = Flask(__name__)

@app.route('/')
def hello_world():

    spell = SpellChecker()

# find those words that may be misspelled
    misspelled = spell.unknown(['something', 'is', 'hapenning', 'here'])

    for word in misspelled:
    # Get the one `most likely` answer
        b = spell.correction(word)

    # Get a list of `likely` options
        a = spell.candidates(word)


    return str(b)+"\n"+str(a)
