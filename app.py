from flask import Flask, render_template, send_from_directory

app = Flask(__name__)
app.secret_key = "replace later"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/gles3")
def download_gles3():
    return send_from_directory('static', filename="files/OmniBall_GLES3.zip", as_attachment=True)

@app.route("/gles2")
def download_gles2():
    return send_from_directory('static', filename="files/OmniBall_GLES2.zip", as_attachment=True)


if __name__ == "__main__":
    app.run()