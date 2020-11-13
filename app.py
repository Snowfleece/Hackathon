from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.String(200), nullable=False)
	date_created = db.Column(db.DateTime, default=datetime.utcnow)

	def __repr__(self):
		return '<Task %r>' % self.id

@app.route('/mainpage', methods=['GET'])
def main():
	return render_template('mainpage.html')

@app.route('/aboutus', methods=['GET'])
def aboutus():
	return render_template('aboutus.html')

@app.route('/faq', methods=['GET'])
def faq():
	return render_template('faq.html')

@app.route('/faq2', methods=['GET'])
def faq2():
	return render_template('faq2.html')

@app.route('/faq3', methods=['GET'])
def faq3():
	return render_template('faq3.html')

@app.route('/faq4', methods=['GET'])
def faq4():
	return render_template('faq4.html')

@app.route('/', methods=['POST', 'GET'])
def index():
	if request.method == 'POST':
		task_content = request.form['content']
		new_task = Todo(content=task_content)

		try:
			db.session.add(new_task)
			db.session.commit()
			return redirect('/')
		except:
			return 'There was an issue adding your task'

	else:
		tasks = Todo.query.order_by(Todo.date_created).all()
		return render_template('index.html', tasks=tasks)
@app.route('/delete/<int:id>')
def delete(id):
	task_to_delete = Todo.query.get_or_404(id)
	try:
		db.session.delete(task_to_delete)
		db.session.commit()
		return redirect('/')
	except:
		return 'There was an issue deleting the task'

@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
	task = Todo.query.get_or_404(id)
	if request.method == 'POST':
		task.content = request.form['content']
		try:
			db.session.commit()
			return redirect('/')
		except:
			return 'There was an issue with updating the task'
	else:
		return render_template('update.html', task=task)

@app.route('/answer/<int:id>', methods=['POST', 'GET'])
def answer(id):
	task = Todo.query.get_or_404(id)
	if request.method == 'POST':
		task.content = request.form['content']
		try:
			db.session.commit()
			return redirect('/')
		except:
			return 'There was an issue with updating the task'
	else:
		return render_template('update.html', task=task)

if __name__ == "__main__":
	app.run(debug=True)
