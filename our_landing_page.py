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

@app.route("/graph_page", methods=['POST']) 
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

@app.route("/thank_you", methods=['GET', 'POST'])
def send_simple_message():
    form_data = request.form
    email_address = form_data["email_address"]
    return request.form(
		"https://api.mailgun.net/v3/sandbox739f698ff783463b95d9f9ef8337ec54.mailgun.org/messages",
		auth=("api", "dcc9f76372aa327175f9b28e77dabc81-816b23ef-47c928a6"),
		    files=[("Your Graph", open(href="data:image/png;base64, {{ plot_url }}"))],
            data ={
            "from": "Graph Generator <mailgun@sandbox739f698ff783463b95d9f9ef8337ec54.mailgun.org>",
			"to": [int(form_data["email_address"])],
			"subject": "Your graph",
			"text": "Please find attached your graph!"})
    return render_template('thank_you.html'))

app.run(debug=True) #runs the app. the debug part - unlocks debugging feature.