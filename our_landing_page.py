from flask import Flask, render_template, request
app = Flask("our_aapp") #making an app
@app.route("/")    #@ makes it a 'decorator'. line tells peple where to look inside flask framework. Decorators always followed by function.

app.run(debug=True) #runs the app. the debug part - unlocks debugging feature.