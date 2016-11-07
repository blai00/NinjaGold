from flask import Flask, redirect, request, session, render_template
import random

app = Flask(__name__)
app.secret_key = 'very secret'

data = {}

@app.route('/' , methods=['GET','POST'])
def index():
	session['gold']
	return render_template('index.html' , data = data)

@app.route('/process_money', methods=['GET','POST'])
def process_money():
	data = {}

	if request.form['location'] == 'farm':
		data ={'location': 'farm'}
		farm_gold = random.randint(10,20)
		session['gold'] += farm_gold
		return redirect ('/')

	elif request.form['location'] == 'cave':
		data ={'location': 'cave'}
		cave_gold = random.randint(10,20)
		session['gold'] += cave_gold
		return redirect ('/')

	elif request.form['location'] == 'house':
		data ={'location': 'house'}
		house_gold = random.randint(2,5)
		session['gold'] += house_gold
		return redirect('/')

	elif request.form['location'] == 'casino':
		data ={'location': 'casino'}
		casino_gold = random.randint(-50,50)
		session['gold'] += casino_gold
		return redirect('/')
if __name__ == "__main__":
    app.run(debug=True)




