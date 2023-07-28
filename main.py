from flask import Flask, render_template, jsonify

app = Flask(__name__)

Jobs = [{
  "id": 1,
  "title": "Data analytics",
  "location": "Bangalore , India",
  "salary": "10,00,000"
}, {
  "id": 2,
  "title": "Data Science",
  "location": "Delhi , India",
  "salary": "15,00,000"
}, {
  "id": 3,
  "title": "Frontend Engineer",
  "location": "Remote",
  "salary": "12,00,000"
}, {
  "id": 4,
  "title": "Backend Engineer",
  "location": "San Francisco",
  "salary": "$120,000"
}]


@app.route("/")
def home():
  return render_template("home.html", jobs=Jobs)


@app.route("/api/jobs")
def listjob():
  return jsonify(Jobs)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
