from flask import Flask, render_template, jsonify

app = Flask(__name__)


JOBS = [
    {
        "id":1,
        "title": "data analyst",
        "location": "Jgd",
        "salary":"30000"
    }, 
    {
        "id":2,
        "title": "eng",
        "location": "remote",
        "salary":"3000"
    }, 
]
@app.route("/")
def hello_world():
    return render_template("home.html", jobs=JOBS, company_name="Jovian")

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
