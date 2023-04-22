from flask import Flask, render_template

#Kreirana Flask istanca
app= Flask(__name__)


"""#Kreiranje Flask ruta
@app.route('/')
def index():
	return "<h1>Hello World</h1>"
"""

"""
###FILTERI
safe - 
capitalize
lower
upper
title
trim
striptags
"""

#Renderovanje templeta kroz kod
@app.route('/')
def index():
	first_name="Petar"
	stuff= "This is <b> Bold </b> Text"
	favorite_pizza=["Pica sa Šunkom", "Pica sa Gljivama",'Pica sa sirom',41]
	return render_template('index.html', first_name=first_name,stuff=stuff,favorite_pizza=favorite_pizza)

# loclalhost:5000/user/petar -treba da ispise Hello petar(odnosno sta god da upises posle user/   /)
@app.route('/user/<name>')
def user(name):
	return render_template('user.html', name=name)

#Kreirati stranicu za Error Strane!

#Nepostojeći URL
@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

#Greška Unutar Servera
@app.errorhandler(500)
def page_not_found(e):
	return render_template("500.html"), 500