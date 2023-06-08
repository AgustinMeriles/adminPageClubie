from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost:3306/flaskcontact'
mysql = MySQL(app)

@app.route('/')
def Index():
    return render_template('registro.html')

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        email = request.form['email']
        phone = request.form['phone']
        direcccion = request.form['direccion']
        # cur = mysql.connection.cursor()
        # cur.execute('INSERT INTO contacts (fullname, phone, email, direccion) VALUES (%s, %s, %s, %s)',
        #              (fullname, email, phone, direcccion))
        # mysql.connection.commit()
        print(fullname, email)
        return 'recived'

@app.route('/edit')
def edit_contact():
    return 'edit contact'

@app.route('/delete')
def delete_contact():
    return 'delete contact'

if __name__ == '__main__':
    app.run(port=5000, debug = True)