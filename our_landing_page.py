from flask import Flask, render_template, request
app = Flask("Myapp") #making an app
@app.route("/")    #@ makes it a 'decorator'. line tells peple where to look inside flask framework. Decorators always followed by function.
def hello():
        return "Hello World!"

@app.route("/<name>")
def hello_someone(name):
        return render_template("our_landing_page.html", name=name.title())

@app.route("/signup", methods=["POST"])
def sign_up():
        form_data = request.form
        print (form_data["email"])
        return "All OK"

app.run(debug=True) #runs the app. the debug part - unlocks debugging feature.