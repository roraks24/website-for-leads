from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# Config — Natural Fitness Gym
GYM_NAME        = "Natural Fitness Gym"
GYM_NAME_SHORT  = "Natural Fitness"
GYM_CITY        = "Jaipur"
GYM_WHATSAPP    = "918890450309"   # country code + number, no +
GYM_PHONE       = "088904 50309"
GYM_ADDRESS     = "Office No. 2, Harchand Plaza, near NBC Rd, Kamla Nehru Nagar, Hasanpura, Jaipur, Rajasthan 302006"
GYM_TAGLINE     = "Transform Your Body, Transform Your Life"
GYM_RATING      = "4.7"
GYM_REVIEWS     = "29"
GYM_MEMBERS     = "500+"

@app.route("/")
def home():
    return render_template("index.html",
        gym_name=GYM_NAME,
        gym_name_short=GYM_NAME_SHORT,
        gym_city=GYM_CITY,
        whatsapp=GYM_WHATSAPP,
        phone=GYM_PHONE,
        address=GYM_ADDRESS,
        tagline=GYM_TAGLINE,
        rating=GYM_RATING,
        reviews=GYM_REVIEWS,
        members=GYM_MEMBERS,
        year=datetime.now().year
    )

@app.route("/lead", methods=["POST"])
def lead():
    """Simple lead capture endpoint"""
    data = request.json
    name  = data.get("name", "")
    phone = data.get("phone", "")
    goal  = data.get("goal", "")
    print(f"NEW LEAD: {name} | {phone} | {goal}")
    return jsonify({"status": "ok", "message": "Lead captured"})

if __name__ == "__main__":
    app.run(debug=True)
