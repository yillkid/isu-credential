from flask import Flask, render_template
app = Flask(__name__)

from apps.tangle import write_data_to_tangle 

@app.route("/")
def issuer_form():
    return render_template('issuer.html')

@app.route("/write_data")
def write_data():
    result = write_data_to_tangle({"date":"2020-08-11"})
    return str(result)

if __name__ == "__main__":
    app.run(debug = True, threaded = True, host = "0.0.0.0", port = 5000)
