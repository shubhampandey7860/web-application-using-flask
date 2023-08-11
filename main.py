from flask import Flask, render_template, jsonify , request 
from database import load_jobs_from_db , load_job_from_db,add_application_to_db
from flask_api import status


app = Flask(__name__)


@app.route("/")
def home():
  jobs = load_jobs_from_db()
  return render_template("home.html", jobs=jobs) 


@app.route("/api/jobs")
def listjob():
  jobs = load_jobs_from_db()
  return jsonify(jobs)

@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)
  if not job:
    return "Not found",status.HTTP_404_NOT_FOUND
  return render_template("jobtitle.html",job = job)
@app.route("/contact/")
def contact():
  return render_template("contact.html")


@app.route("/job/<id>/apply", methods =['post'])
def apply_to_job(id):
  data = request.form
  job = load_job_from_db(id)
  return render_template('application_submitted.html',application = data,job=job) 



if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
