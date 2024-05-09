import sqlite3
from flask import Flask, request, render_template
import os.path

app = Flask(__name__)

def bd_request(filter_value):
    connection = sqlite3.connect("web.db")
    cursor = connection.cursor()
    key_skills_filter = []
    job_title_filter = []
    if filter_value["key_skills"] != "":
        if filter_value["job_title"] != "":
            cursor.execute('SELECT fio, job_title, work_time, city, key_skills, cv_link FROM workers WHERE job_title = ? AND key_skills like ?', (filter_value["job_title"], '%' + filter_value["key_skills"] + '%'))
            key_skills_filter = cursor.fetchall()
        else:
            cursor.execute('SELECT fio, job_title, work_time, city, key_skills, cv_link FROM workers WHERE key_skills like ?', ('%' + filter_value["key_skills"] + '%',))
            key_skills_filter = cursor.fetchall()

    elif filter_value["job_title"] != "":
        cursor.execute('SELECT fio, job_title, work_time, city, key_skills, cv_link FROM workers WHERE job_title = ?', (filter_value["job_title"],))
        job_title_filter = cursor.fetchall()
    
    result = key_skills_filter + job_title_filter
    return result

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = dict()
    job_title = request.form['job_title']
    key_skills = request.form['key_skills']
    data["job_title"] = job_title
    data["key_skills"] = key_skills
    return render_template('result.html', workers = bd_request(data))

if __name__ == '__main__':
    app.run(debug=True)

