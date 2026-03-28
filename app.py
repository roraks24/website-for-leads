from flask import Flask, render_template

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
        "name": "Basic",<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ gym_name }} — {{ gym_city }}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
</head>
<body>

<div class="noise"></div>

<!-- NAV -->
<nav class="nav">
    <div class="nav-inner">
        <div class="logo">{{ gym_name | upper }}</div>
        <a href="https://wa.me/{{ whatsapp }}?text=Hi%2C%20I%20want%20to%20book%20a%20free%20trial%20at%20{{ gym_name | urlencode }}"
           class="btn-nav" target="_blank">Book Free Trial →</a>
    </div>
</nav>

<!-- HERO -->
<section class="hero">
    <div class="hero-bg-text">FIT</div>
    <div class="container">
        <div class="hero-badge">✅ Trusted by 500+ members in {{ gym_city }}</div>
        <h1 class="hero-title">
            Join {{ gym_city }}'s Most<br>
            <span class="accent">Result-Driven Gym</span>
        </h1>
        <p class="hero-sub">
            Certified trainers, modern equipment &amp; real results.<br>
            Start your free trial today.
        </p>
        <p class="power-line">"Even 1 workout can change your routine — try free for 3 days."</p>

        <div class="hero-stats">
            <div class="stat">
                <span class="stat-num">500+</span>
                <span class="stat-label">Active members</span>
            </div>
            <div class="stat-divider"></div>
            <div class="stat">
                <span class="stat-num">4.6 ⭐</span>
                <span class="stat-label">Google · 200+ reviews</span>
            </div>
            <div class="stat-divider"></div>
            <div class="stat">
                <span class="stat-num">3</span>
                <span class="stat-label">Day free trial</span>
            </div>
        </div>

        <div class="hero-cta">
            <a href="https://wa.me/{{ whatsapp }}?text=Hi%2C%20I%20want%20to%20book%20a%20free%20trial%20at%20{{ gym_name | urlencode }}"
               class="btn-primary" target="_blank">
                <span class="wa-icon">💬</span> Book Free Trial on WhatsApp (Instant Reply)
            </a>
            <p class="cta-note">⚡ Only 7 trial slots left this week</p>
        </div>
    </div>
    <div class="hero-scroll-hint">↓ SCROLL</div>
</section>

<!-- HOW IT WORKS -->
<section class="how-section">
    <div class="container">
        <div class="section-label">HOW IT WORKS</div>
        <h2 class="section-title">Join in 3 Simple Steps</h2>
        <div class="steps">
            <div class="step" data-step="01">
                <div class="step-icon">💬</div>
                <h3>Message Us</h3>
                <p>Tap WhatsApp → Get instant reply from a trainer. No waiting, no forms.</p>
            </div>
            <div class="step-arrow">→</div>
            <div class="step" data-step="02">
                <div class="step-icon">🎯</div>
                <h3>Visit for Free</h3>
                <p>Come in for a free 3-day trial — see the gym, meet the trainers, feel the vibe</p>
            </div>
            <div class="step-arrow">→</div>
            <div class="step" data-step="03">
                <div class="step-icon">💪</div>
                <h3>Start Transforming</h3>
                <p>Pick your plan, lock in your spot, and start your fitness journey the very next day</p>
            </div>
        </div>
    </div>
</section>

<!-- PLANS -->
<section class="plans-section">
    <div class="container">
        <div class="section-label">MEMBERSHIP</div>
        <h2 class="section-title">Simple. Affordable. Results.</h2>
        <p class="plans-intro">Plans starting at just ₹999/month — no hidden charges</p>
        <div class="plans">
            <div class="plan">
                <div class="plan-tag">STARTER</div>
                <div class="plan-price">₹999<span>/mo</span></div>
                <ul class="plan-perks">
                    <li>✓ Full gym access</li>
                    <li>✓ Locker room</li>
                    <li>✓ Basic equipment</li>
                    <li>✓ Group sessions</li>
                </ul>
                <a href="https://wa.me/{{ whatsapp }}?text=Hi%2C%20I%20want%20to%20book%20a%20free%20trial%20at%20{{ gym_name | urlencode }}%20(Starter%20Plan)"
                   class="btn-plan" target="_blank">Book Free Trial on WhatsApp</a>
            </div>
            <div class="plan plan-featured">
                <div class="plan-badge">MOST POPULAR</div>
                <div class="plan-tag">PRO</div>
                <div class="plan-price">₹1,999<span>/mo</span></div>
                <ul class="plan-perks">
                    <li>✓ Everything in Basic</li>
                    <li>✓ Diet consultation</li>
                    <li>✓ Trainer check-ins</li>
                    <li>✓ Progress tracking</li>
                </ul>
                <a href="https://wa.me/{{ whatsapp }}?text=Hi%2C%20I%20want%20to%20book%20a%20free%20trial%20at%20{{ gym_name | urlencode }}%20(Pro%20Plan)"
                   class="btn-plan btn-plan-featured" target="_blank">Book Free Trial on WhatsApp</a>
            </div>
            <div class="plan">
                <div class="plan-tag">ELITE</div>
                <div class="plan-price">₹3,999<span>/mo</span></div>
                <ul class="plan-perks">
                    <li>✓ Personal trainer</li>
                    <li>✓ Custom meal plan</li>
                    <li>✓ Weekly check-ins</li>
                    <li>✓ Body composition</li>
                </ul>
                <a href="https://wa.me/{{ whatsapp }}?text=Hi%2C%20I%20want%20to%20book%20a%20free%20trial%20at%20{{ gym_name | urlencode }}%20(Elite%20Plan)"
                   class="btn-plan" target="_blank">Book Free Trial on WhatsApp</a>
            </div>
        </div>
        <p class="plans-note">⚡ Only <strong>7 trial slots</strong> left this week</p>
    </div>
</section>

<!-- FREE TRIAL CTA BLOCK -->
<section class="lead-section">
    <div class="container">
        <div class="lead-box lead-box-centered">
            <div class="section-label">FREE TRIAL</div>
            <h2>Try 3 Days. Zero Risk.</h2>
            <p>No commitment. No contract. Just show up, work out, and decide after.</p>
            <div class="lead-benefits">
                <span>✓ Free 3-day trial visit</span>
                <span>✓ No paperwork</span>
                <span>✓ Instant WhatsApp reply</span>
            </div>
            <a href="https://wa.me/{{ whatsapp }}?text=Hi%2C%20I%20want%20to%20book%20a%20free%20trial%20at%20{{ gym_name | urlencode }}"
               class="btn-primary" target="_blank" style="margin-top: 28px;">
                <span class="wa-icon">💬</span> Book Free Trial on WhatsApp (Instant Reply)
            </a>
            <p class="cta-note" style="margin-top: 12px;">⚡ Only 7 trial slots left this week</p>
        </div>
    </div>
</section>

<!-- BENEFITS -->
<section class="benefits-section">
    <div class="container">
        <div class="section-label">WHY US</div>
        <h2 class="section-title">Built Different</h2>
        <div class="benefits-grid">
            <div class="benefit">
                <div class="benefit-icon">🏋️</div>
                <h3>Certified Trainers</h3>
                <p>Every trainer is certified with real experience in body transformation</p>
            </div>
            <div class="benefit">
                <div class="benefit-icon">📊</div>
                <h3>Progress Tracking</h3>
                <p>Monthly measurements, photos, and reports so you see real results</p>
            </div>
            <div class="benefit">
                <div class="benefit-icon">🥗</div>
                <h3>Diet Guidance</h3>
                <p>Custom meal plans aligned with your fitness goals and budget</p>
            </div>
            <div class="benefit">
                <div class="benefit-icon">⚡</div>
                <h3>Modern Equipment</h3>
                <p>Latest machines maintained regularly — no outdated, broken gear</p>
            </div>
            <div class="benefit">
                <div class="benefit-icon">🕐</div>
                <h3>Flexible Hours</h3>
                <p>Early mornings to late evenings — fits your college or work schedule</p>
            </div>
            <div class="benefit">
                <div class="benefit-icon">💬</div>
                <h3>WhatsApp Support</h3>
                <p>Ask questions anytime. Your trainer replies on WhatsApp directly</p>
            </div>
        </div>
    </div>
</section>

<!-- TESTIMONIALS -->
<section class="testimonials-section">
    <div class="container">
        <div class="section-label">RESULTS</div>
        <h2 class="section-title">Real People. Real Results.</h2>
        <div class="testimonials">
            <div class="testi">
                <div class="testi-stars">★★★★★</div>
                <p>"Lost 9kg in 3 months. The trainers here actually care about your progress. Best decision I made."</p>
                <div class="testi-author">
                    <div class="testi-avatar">RK</div>
                    <div>
                        <strong>Rahul K.</strong>
                        <span>Lost 9kg • 3 months</span>
                    </div>
                </div>
            </div>
            <div class="testi">
                <div class="testi-stars">★★★★★</div>
                <p>"Gained 5kg muscle in 4 months with their Elite plan. Diet plan + trainer = game changer."</p>
                <div class="testi-author">
                    <div class="testi-avatar">AS</div>
                    <div>
                        <strong>Arjun S.</strong>
                        <span>Gained 5kg muscle • 4 months</span>
                    </div>
                </div>
            </div>
            <div class="testi">
                <div class="testi-stars">★★★★★</div>
                <p>"Joined through WhatsApp, got a reply in minutes. Started next day. No BS, just results."</p>
                <div class="testi-author">
                    <div class="testi-avatar">PM</div>
                    <div>
                        <strong>Priya M.</strong>
                        <span>Member since 2024</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- FINAL CTA -->
<section class="final-cta">
    <div class="container">
        <div class="cta-bg-text">NOW</div>
        <h2>Stop Waiting.<br>Start Today.</h2>
        <p>Every day you delay is a day your body doesn't change.</p>
        <a href="https://wa.me/{{ whatsapp }}?text=Hi%2C%20I%20want%20to%20book%20a%20free%20trial%20at%20{{ gym_name | urlencode }}"
           class="btn-primary btn-large" target="_blank">
            💬 Book Free Trial on WhatsApp (Instant Reply)
        </a>
        <p class="urgency">⚡ Only 7 trial slots left this week</p>
    </div>
</section>

<!-- FOOTER -->
<footer class="footer">
    <div class="container">
        <div class="footer-inner">
            <div class="logo">{{ gym_name | upper }}</div>
            <p>{{ gym_city }}, India</p>
            <a href="https://wa.me/{{ whatsapp }}" target="_blank" class="footer-wa">
                💬 Chat on WhatsApp
            </a>
        </div>
        <p class="footer-copy">© {{ year }} {{ gym_name }}. All rights reserved.</p>
    </div>
</footer>

<!-- FLOATING WHATSAPP BUTTON -->
<a href="https://wa.me/{{ whatsapp }}?text=Hi%2C%20I%20want%20to%20book%20a%20free%20trial%20at%20{{ gym_name | urlencode }}"
   class="wa-float" target="_blank">
    <span class="wa-float-icon">💬</span>
    <span class="wa-float-text">Chat on WhatsApp</span>
</a>

<script src="{{ url_for('static', filename='js/main.js') }}"></script>
</body>
</html>

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


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
