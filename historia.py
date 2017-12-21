import logging
from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.launch
def new_history():
    welcome_msg = render_template('first')
    return question(welcome_msg).reprompt("Sorry I didn't get that. Are you a boy or a girl?")

@ask.intent("Segundo", convert={'gender':str})
def firstPart(gender):
	py_gender = format(gender)
	if py_gender == "girl":
		fmsg = render_template('girl')
	else :
		fmsg = render_template('boy')
	session.attributes['gender'] = py_gender
	return question(fmsg).reprompt("Sorry I didn't get that. What will you choose, Cotton Candy? Chocolate? Popsicles?")

@ask.intent("Tercero", convert={'candy':str})
def secPart(candy):
	py_candy = format(candy)
	session.attributes['candy'] = py_candy
	py_gender = session.attributes['gender']
	sec_part = render_template('selection', gender=py_gender, candy=candy)
	return question(sec_part).reprompt("Sorry I didn't get that. Did I ate them all or did I save some?")

@ask.intent("Cuarto", convert={'hunger':str})
def terPart(hunger):
	py_hunger = format(hunger)
	if py_hunger == 'some':
		ter_part = render_template('savesome')
	else :
		ter_part = render_template('alot')
	return statement(ter_part)

if __name__ == '__main__':
    app.run(debug=True)