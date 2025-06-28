from flask import Flask, jsonify, render_template

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 10,00,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Delhi, India',
        'salary': 'Rs. 15,00,000'
    },
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'Remote',
        'salary': 'Rs. 12,00,000'
    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'San Francisco, USA',
    },
    {
        'id': 5,
        'title': 'Full Stack Engineer',
        'location': 'Remote',
        'salary': '$150,000'
    },
    {
        'id': 6,
        'title': 'DevOps Engineer',
        'location': 'Remote',
        'salary': '$130,000'
    },
]


@app.route('/')
def Hello_World():
  return render_template('home.html', jobs=JOBS, company_name="WebSI")


@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
