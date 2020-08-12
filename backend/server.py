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

@app.route("/new_data", methods=['GET', 'POST'])
def new_data():
    if request.method == 'POST':
        print(request.form)
        fp = open("static/new_data.txt", "a")
        fp.write(str(request.form) + "\n")
        fp.close()

        return str(request.form)

@app.route("/read_data")
def read_data():
    f = open("static/new_data.txt", "r")
    content = f.read()
    f.close()

    return content

if __name__ == "__main__":
    app.run(debug = True, threaded = True, host = "0.0.0.0", port = 5000)
