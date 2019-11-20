from flask import Flask, render_template, request
app = Flask("our_app") #making an app
import matplotlib.pyplot as plt
x_value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y_value = [1, 2, 3, 4, 8, 6, 7, 8, 9, 13, 11, 12]
plt.plot(x_value, y_value, color='pink')
plt.xlabel("x")
plt.ylabel("y_axis")
plt.title("form_title")
plt.show()
s.plot.bar()
