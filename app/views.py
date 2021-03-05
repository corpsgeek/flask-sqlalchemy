from app import app, db
from flask import render_template, request
from app.forms import ContactForm
from app.models import User

@app.route("/")
def index():
    return "Hello world"

@app.route("/register", methods=["GET", "POST"])
def register():
    #check the request method to ensure the handling of POST request only
    if request.method == "POST":
        #store the form value
        user_name = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        user = User(username = user_name, user_email = email, user_password = password)
        db.session.add(user)
        db.session.commit()
        
        return 'User registration successful'

    return render_template('register.html')


@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data 
        email = form.email.data   
        message = form.message.data   

        return name + "<br /> " + email + "<br /> " + message

    return render_template('contact.html', form=form)