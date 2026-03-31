from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# Config - change these
GYM_NAME = "VIEWSONIC FITNESS"
GYM_CITY = "Jaipur"
GYM_WHATSAPP = "917877169982"  # country code + number, no +
GYM_TAGLINE = "Get 10+ New Members Every Month"

@app.route("/")
def home():
    return render_template("index.html",
        gym_name=GYM_NAME,
        gym_city=GYM_CITY,
        whatsapp=GYM_WHATSAPP,
        tagline=GYM_TAGLINE,
        year=datetime.now().year
    )

@app.route("/lead", methods=["POST"])
def lead():
    """Simple lead capture endpoint"""
    data = request.json
    name = data.get("name", "")
    phone = data.get("phone", "")
    goal = data.get("goal", "")
    # In production: save to DB or send email
    print(f"NEW LEAD: {name} | {phone} | {goal}")
    return jsonify({"status": "ok", "message": "Lead captured"})

if __name__ == "__main__":
    app.run(debug=True)
