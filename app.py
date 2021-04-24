from flask import Flask,render_template,request
import mysql.connector
db = mysql.connector.connect(host='0.0.0.0',password='G0d!sgreat',user='root',database='sampledatabase')

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def hello():
	cursor=db.cursor()
	if request.method == 'POST':
		name = request.form.get('name')
		age = request.form.get('age')
		cursor.execute('insert into agetable values (%s,%s)',(name,age))
		db.commit()
		return "your name is "+name+" and your age is "+age
	return render_template('form.html')	

app.run(host='0.0.0.0')
