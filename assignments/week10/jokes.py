import pyjokes
import cowsay
import helper

helper.greet("Turtle")
joke = pyjokes.get_joke(language='en')
cowsay.turtle (joke)

