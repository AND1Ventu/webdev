from flask import Flask, render_template, jsonify

app = Flask(__name__)

jobs = [
  {
    'id':1,
    'title':'Data analyst',
    'location':'Delhi, India',
    'salary':'Rs. 12,00,000'
  },
  {
    'id':2,
    'title':'Data analyst',
    'location':'Bangalore, India',
    'salary':'Rs. 15,00,000'
  },
  {
    'id':3,
    'title':'Data analyst',
    'location':'Mumbai, India',
    'salary':'Rs. 14,00,000'
  }
]

@app.route("/")
def hello_fun():
  return render_template('home.html',
                        jobs=jobs)

@app.route('/api/jobs')
def list_jobs():
  return jsonify(jobs)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)