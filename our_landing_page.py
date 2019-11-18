from flask import Flask, render_template, request
app = Flask("our_app") #making an app
@app.route("/")    #@ makes it a 'decorator'. line tells peple where to look inside flask framework. Decorators always followed by function.
<<<<<<< Updated upstream
def home():
        return render_template("our_landing_page.html")
app.run(debug=True) #runs the app. the debug part - unlocks debugging feature.
=======
def main():
        return ("Welcome to our hashtag tracker!")

app.run(debug=True) #runs the app the debug part - unlocks debugging feature.
>>>>>>> Stashed changes
