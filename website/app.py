import sqlite3
from flask import Flask, render_template

app = Flask(__name__)



GROUP_MEMBER_DETAILS = [
    {'name': "Antash Devani", "student_id":"0873039"},
    {'name': "Aum Bimalbhai Gajjar", "student_id":"0872864"},
    {'name': "Rajdeepsinh Gohil", "student_id":"0867997"},
    {'name': "Priyanka Sharma", "student_id":"0872992"},
]

@app.route("/")
def home():
    return render_template('index.html', title="Home | GROUP 2")

@app.route("/data")
def data():
    conn = sqlite3.connect('../database/data.db')
    data = conn.execute("SELECT * FROM sales_history")
    return render_template('data.html', title="Data Page | GROUP 2",data=data)

@app.route('/about')
def about():
    return render_template('about.html', title="About Us | GROUP 2", GROUP_MEMBER_DETAILS=GROUP_MEMBER_DETAILS)

if __name__ == "__main__":
    app.run(debug=True)

