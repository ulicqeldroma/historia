import logging
from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session, request, audio, current_stream

app = Flask(__name__)
ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.launch
def new_history():
    welcome_msg = render_template('first')
    return question(welcome_msg).reprompt("Sorry I didn't get your made up name. Please tell me your made-up name.")

@ask.intent("Name_Intent", convert={'name':str})
def nameFunction(name):
	py_name = format(name)
	session.attributes['name'] = py_name
	fmsg = render_template('name', name=py_name)
	return question(fmsg).reprompt("My bad. I didn't get that. Are you a boy or a girl?")

@ask.intent("Segundo", convert={'gender':str})
def genderFunction(gender):
	py_gender = format(gender)
	py_name = session.attributes['name']
	if py_gender == "girl":
		fmsg = render_template('girl', name=py_name)
	else :
		fmsg = render_template('boy', name=py_name)
	session.attributes['gender'] = py_gender
	return question(fmsg).reprompt("Sorry I didn't get that. Which story do you want to hear ? Spooky or just normal ?")

@ask.intent("story_selection", convert={'story':str})
def story_selectionFunction(story):
	py_story = format(story)
	if py_story == "spooky":
		fmsg = render_template('spooky')
	else :
		fmsg = render_template('normal')
	session.attributes['story'] = py_story
	return question(fmsg).reprompt("Sorry I didn't get that. Which story do you want to hear ? Spooky or just normal ?")

@ask.intent("Tercero", convert={'candy':str})
def fourthPart(candy):
	py_candy = format(candy)
	session.attributes['candy'] = py_candy
	py_gender = session.attributes['gender']
	sec_part = render_template('selection', gender=py_gender, candy=candy)
	return question(sec_part).reprompt("Sorry I didn't get that. Did I ate them all or did I save some?")

@ask.intent("Cuarto", convert={'hunger':str})
def fifthPart(hunger):
	py_hunger = format(hunger)
	if py_hunger == 'some':
		ter_part = render_template('savesome')
	else :
		ter_part = render_template('alot')
	return statement(ter_part)

if __name__ == '__main__':
    app.run(debug=True)