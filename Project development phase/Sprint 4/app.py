from turtle import st
from markupsafe import escape
from flask import Flask, render_template, request, redirect, session,flash
import sqlite3 as sql


import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=ea286ace-86c7-4d5b-8580-3fbfa46b1c66.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31505;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=plq76207;PWD=ZmeqbSx0vyVOuxoG;","","")
print("connection successfully")

app = Flask(__name__)
app.secret_key = 'HIII'

@app.route('/')
def index():
   return render_template('signin.html')
 
@app.route('/signin')
def signin():
   return render_template('signin.html')

@app.route('/buy')
def buy():
   return render_template('buy.html')

@app.route('/cosmetics')
def cosmetics():
   return render_template('cosmetics.html')

@app.route('/minibytes')
def minibytes():
   return render_template('minibytes.html')

@app.route('/stationary')
def stationary():
   return render_template('stationary.html')

@app.route('/flour')
def flour():
   return render_template('flour.html')


@app.route('/signinpage')
def signinpage():
   return render_template('signinpage.html')

@app.route('/retail')
def retail():
   return render_template('retail.html')

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/signup')
def signup():
   return render_template('signup.html')

@app.route('/fruits')
def fruits():
   return render_template('fruits.html')

@app.route('/vegetables')
def vegetables():
   return render_template('vegetables.html')

@app.route('/oilitems')
def oilitems():
   return render_template('oilitems.html')

@app.route('/softdrinks')
def softdrinks():
   return render_template('softdrinks.html')

@app.route('/go to signup')
def go():
   return render_template('signup.html')

@app.route('/back')
def back():
   return render_template('signin.html')

@app.route('/data',methods = ['POST', 'GET'])
def data():
   if request.method == 'POST':
         
      name = request.form['name']          
      email = request.form['email']
      password = request.form['password']

      sql = "SELECT * FROM login WHERE email=?"
      stmt = ibm_db.prepare(conn, sql)
      ibm_db.bind_param(stmt,1,email)
      ibm_db.execute(stmt)
      account= ibm_db.fetch_assoc(stmt)
      print("account")
      
      if account:
         flash("You Have Already Account,Please Go To Login","danger")
        
      else:
         insert_sql = "INSERT INTO login VALUES (?,?,?)"
         prep_stmt = ibm_db.prepare(conn, insert_sql)
         ibm_db.bind_param(prep_stmt,1,name)
         ibm_db.bind_param(prep_stmt,2,email)
         ibm_db.bind_param(prep_stmt,3,password)
         ibm_db.execute(prep_stmt)
         flash("Register Successfully","success")

   return redirect("signup")

@app.route('/login',methods = [ 'GET', 'POST'])  
def login():
    if request.method == 'POST':
        name = request.form['email']
        password = request.form['password']

        sql = "SELECT * FROM login WHERE email = ? AND password = ?"
        stmt = ibm_db.prepare(conn, sql)

        ibm_db.bind_param(stmt,1,name)
        ibm_db.bind_param(stmt,2,password)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        print(account)
        if account:
            session['email'] = name
            return redirect("retail")
        else:
            flash("Invalid Username or Password")
    return redirect("signin")
   
@app.route('/logout')
def logout():
   session.clear()
   return render_template('signin.html')

@app.route('/cdata',methods = ['POST', 'GET'])
def cdata():
   if request.method == 'POST':
         
      name = request.form['name']          
      shopname= request.form['shopname']
      location = request.form['location']
      address = request.form['address']
      city = request.form['city']
      state = request.form['state']
      mobilenumber = request.form['mobile no']
      quantity = request.form['quantity']

      customer_sql = "INSERT INTO customerdetails VALUES (?,?,?,?,?,?,?,?)"
      prep_stmt = ibm_db.prepare(conn, customer_sql)
      ibm_db.bind_param(prep_stmt,1,name)
      ibm_db.bind_param(prep_stmt,2,shopname)
      ibm_db.bind_param(prep_stmt,3,location)
      ibm_db.bind_param(prep_stmt,4,address)
      ibm_db.bind_param(prep_stmt,5,city)
      ibm_db.bind_param(prep_stmt,6,state)
      ibm_db.bind_param(prep_stmt,7,mobilenumber)
      ibm_db.bind_param(prep_stmt,8,quantity)
      ibm_db.execute(prep_stmt)
   return render_template("buy.html")
   


if __name__ == '__main__':
   app.run(host='0.0.0.0',port=5000)