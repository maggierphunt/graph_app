from flask import Flask, render_template, request, Response
import matplotlib.pyplot as plt
import io
import base64

app = Flask("our_app") #making an app

@app.route("/")    #@ makes it a 'decorator'. line tells peple where to look inside flask framework. Decorators always followed by function.
def our_landing_page():
        return render_template("our_landing_page.html")

@app.route("/about")    #@ makes it a 'decorator'. line tells peple where to look inside flask framework. Decorators always followed by function.
def about():
    return render_template("about.html")

@app.route("/graph_page", methods=['GET', 'POST']) 
def graph_page():
    form_data = request.form

    title = form_data['form_title']
    xaxis = form_data['x_axis']
    yaxis = form_data['y_axis']

    x_value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    y_value = [int(form_data['value_1']), int(form_data['value_2']), int(form_data['value_3']), int(form_data['value_4']), int(form_data['value_5']), int(form_data['value_6']), int(form_data['value_7']), int(form_data['value_8']), int(form_data['value_9']), int(form_data['value_10']), int(form_data['value_11']), int(form_data['value_12'])]

    img = io.BytesIO()
    plt.plot(x_value, y_value, color='pink')
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    plt.title(title)
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    return render_template('graph_page.html', plot_url=plot_url)

app.run(debug=True) #runs the app. the debug part - unlocks debugging feature.