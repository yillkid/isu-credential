from flask import Flask, render_template, request
app = Flask(__name__)

from apps.tangle import write_data_to_tangle

@app.route("/")
def issuer_form():
    return render_template('issuer.html')

@app.route("/write_data", methods=['GET', 'POST'])
def write_data():
    if request.method == 'POST':
        result = write_data_to_tangle(request.form['message'])
        return str(result)

@app.route("/credential_editor")
def credential_editor():
    return render_template('credential_editor.html')

if __name__ == "__main__":
    app.run(debug = True, threaded = True, host = "0.0.0.0", port = 5000)
