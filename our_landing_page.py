from flask import Flask, render_template, request
app = Flask("our_app") #making an app
@app.route("/")    #@ makes it a 'decorator'. line tells peple where to look inside flask framework. Decorators always followed by function.

def our_landing_page():
        return render_template("our_landing_page.html")

@app.route("/about")    #@ makes it a 'decorator'. line tells peple where to look inside flask framework. Decorators always followed by function.

def about():
        return render_template("about.html")

@app.route("/graph_page", methods=["GET"]) 
def graph_page():
       return render_template("graph_page.html")
        form_data = request.form
        import matplotlib.pyplot as plt
        time_passing = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        graph_line = ["value_1","value_2", "value_3", "value_4", "value_5", "value_6", "value_7", "value_8", "value_9", "value_10", "value_11", "value_12"]
        plt.plot(time_passing, graph_line, color='pink')
        plt.xlabel("x_axis")
        plt.ylabel("y_axis")
        plt.title("form_title")
        plt.show()
        imgplot = plt.imshow(img)
        plt.imshow(sample_image) 
        plt.show() 

app.run(debug=True) #runs the app. the debug part - unlocks debugging feature.