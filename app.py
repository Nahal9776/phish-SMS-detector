from flask import Flask, render_template, request
from detector.classify import is_phishing

app = Flask(__name__)

translations = {
    "en": {
        "title": "Phish SMS Detector",
        "label": "Paste an SMS message:",
        "button": "Analyze",
        "phishing": "Phishing ⚠️",
        "safe": "Safe ✅"
    },
    "fa": {
        "title": "شناسایی پیامک مشکوک",
        "label": "پیامک خود را وارد کنید:",
        "button": "تحلیل کن",
        "phishing": "مشکوک ⚠️",
        "safe": "ایمن ✅"
    },
    "it": {
        "title": "Rilevatore di SMS di phishing",
        "label": "Inserisci il messaggio SMS:",
        "button": "Analizza",
        "phishing": "Phishing ⚠️",
        "safe": "Sicuro ✅"
    }
}

@app.route("/", methods=["GET", "POST"])
def index():
    lang = request.args.get("lang", "en")
    t = translations.get(lang, translations["en"])

    result = None
    if request.method == "POST":
        sms = request.form.get("sms")
        if sms:
            result = t["phishing"] if is_phishing(sms) else t["safe"]

    return render_template("index.html", result=result, t=t)
