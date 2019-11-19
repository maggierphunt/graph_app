from flask import Flask, render_template, request
app = Flask("our_app") #making an app
@app.route("/")    #@ makes it a 'decorator'. line tells peple where to look inside flask framework. Decorators always followed by function.

def main():
        return render_template("our_landing_page.html")
app.run(debug=True) #runs the app. the debug part - unlocks debugging feature.

