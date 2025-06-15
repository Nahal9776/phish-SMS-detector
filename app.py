from flask import Flask, render_template, request
from detector.classify import is_phishing

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        sms = request.form.get("sms")
        if sms:
            result = "Phishing ⚠️" if is_phishing(sms) else "Safe ✅"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
