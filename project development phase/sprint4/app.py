from flask import Flask, render_template, redirect, request, url_for,flash 

app = Flask(_name)

@app.route('/')
def addcalorie():
  return render_template('index.html') 

if __name_ == '_main_': 
  app.run(host='0.0.0.0',port=8080,debug=True)
