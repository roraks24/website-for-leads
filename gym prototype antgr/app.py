from flask import Flask, render_template
import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

app = Flask(__name__)

# ── Configuration ──────────────────────────────────────────────
GYM_NAME = "One Hour Fitness Club"
WHATSAPP_NUMBER = "919587899959"
WHATSAPP_MESSAGE = f"Hi, I want to join {GYM_NAME} Jaipur"
GYM_LOCATION = "DCM, Ajmer Road, Jaipur"
GOOGLE_MAPS_LINK = "https://maps.app.goo.gl/zkxETpYGaNMxhwWQ9"
GOOGLE_MAPS_EMBED = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3501.14!2d75.7389912!3d26.8915045!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x396db5532cc5ac97%3A0x3a883b10205739d4!2sOne%20Hour%20Fitness%20Club%20Jaipur!5e0!3m2!1sen!2sin!4v1"

# Pricing plans
PLANS = [
    {
        "name": "Basic",
        "price": "₹999",
        "period": "/month",
        "features": [
            "Full gym access",
            "Cardio & strength equipment",
            "Locker room access",
            "Free fitness assessment",
        ],
        "popular": False,
    },
    {
        "name": "Pro",
        "price": "₹1,999",
        "period": "/month",
        "features": [
            "Everything in Basic",
            "Group fitness classes",
            "Diet consultation",
            "Progress tracking",
            "1 personal training session",
        ],
        "popular": True,
    },
    {
        "name": "Personal Training",
        "price": "₹4,999",
        "period": "/month",
        "features": [
            "Everything in Pro",
            "Dedicated personal trainer",
            "Custom meal plans",
            "Weekly body composition analysis",
            "Priority booking",
            "24/7 WhatsApp support",
        ],
        "popular": False,
    },
]

# Testimonials
TESTIMONIALS = [
    {
        "name": "Hema Harchandani",
        "text": "I am having personal training with Vijendra. He is best trainer available here. Must try it.",
        "stars": 5,
    },
    {
        "name": "Juan Castaño",
        "text": "I was staying in Jaipur for two days and needed to hit the gym, I was very lucky to find this one!",
        "stars": 5,
    },
    {
        "name": "Arjun K.",
        "text": "The personal training plan changed my life. Went from skinny to fit in 6 months. The diet guidance was a game-changer. Highly recommend this gym!",
        "result": "Complete body transformation",
        "stars": 5,
    },
]

# Benefits
BENEFITS = [
    {"icon": "🏋️", "title": "Certified Trainers", "desc": "Expert trainers to guide you through every rep and set."},
    {"icon": "💪", "title": "Modern Equipment", "desc": "Top-of-the-line machines and free weights for every workout."},
    {"icon": "🥗", "title": "Diet Guidance", "desc": "Personalised nutrition plans to maximise your results."},
    {"icon": "🤝", "title": "Friendly Environment", "desc": "A welcoming, judgement-free zone for every fitness level."},
    {"icon": "📍", "title": "Prime Location", "desc": "Conveniently located in DCM, Ajmer Road — easy to reach from anywhere in Jaipur."},
    {"icon": "⏰", "title": "Flexible Timings", "desc": "Train at your convenience with extended hours."},
]

# Gallery images (filenames in static/images/)
GALLERY = [
    {"src": "gym-1.png", "alt": "Gym Equipment"},
    {"src": "gym-2.png", "alt": "Training Zone"},
    {"src": "gym-3.png", "alt": "Personal Training"},
    {"src": "gym-4.png", "alt": "Group Classes"},
    {"src": "gym-5.png", "alt": "Weight Section"},
    {"src": "gym-6.png", "alt": "Intense Workout"},
]


@app.route("/")
def index():
    return render_template(
        "index.html",
        gym_name=GYM_NAME,
        wa_number=WHATSAPP_NUMBER,
        wa_message=WHATSAPP_MESSAGE,
        plans=PLANS,
        testimonials=TESTIMONIALS,
        benefits=BENEFITS,
        gallery=GALLERY,
        gym_location=GYM_LOCATION,
        maps_link=GOOGLE_MAPS_LINK,
        maps_embed=GOOGLE_MAPS_EMBED,
    )



