/* ===================== main.js ===================== */

// ---------- Theme Toggle ----------
const themeBtn = document.getElementById('theme-toggle');
const body = document.body;

// Load saved theme
const saved = localStorage.getItem('nfg-theme') || 'dark';
body.setAttribute('data-theme', saved);

themeBtn.addEventListener('click', () => {
    const current = body.getAttribute('data-theme');
    const next = current === 'dark' ? 'light' : 'dark';
    body.setAttribute('data-theme', next);
    localStorage.setItem('nfg-theme', next);
});

// ---------- Nav scroll behaviour ----------
const nav = document.getElementById('navbar');
window.addEventListener('scroll', () => {
    nav.classList.toggle('scrolled', window.scrollY > 40);
});

// ---------- Hamburger mobile menu ----------
const hamburger = document.getElementById('nav-hamburger');
const mobileMenu = document.getElementById('mobile-menu');

hamburger.addEventListener('click', () => {
    mobileMenu.classList.toggle('open');
});

// Close mobile menu on link click
document.querySelectorAll('.mobile-link').forEach(link => {
    link.addEventListener('click', () => mobileMenu.classList.remove('open'));
});

// ---------- Scroll Animations (tiny AOS) ----------
const animEls = document.querySelectorAll('.aos-fade-up, .aos-fade-right, .aos-fade-left');

const observer = new IntersectionObserver((entries) => {
    entries.forEach(e => {
        if (e.isIntersecting) {
            e.target.classList.add('visible');
            observer.unobserve(e.target);
        }
    });
}, { threshold: 0.12 });

animEls.forEach(el => observer.observe(el));

// ---------- Smooth-scroll nav links ----------
document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
        const target = document.querySelector(a.getAttribute('href'));
        if (target) {
            e.preventDefault();
            const top = target.getBoundingClientRect().top + window.scrollY - 72;
            window.scrollTo({ top, behavior: 'smooth' });
        }
    });
});

// ---------- Active nav link on scroll ----------
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.nav-link');

window.addEventListener('scroll', () => {
    let current = '';
    sections.forEach(s => {
        if (window.scrollY >= s.offsetTop - 100) current = s.id;
    });
    navLinks.forEach(a => {
        a.classList.remove('active');
        if (a.getAttribute('href') === '#' + current) a.classList.add('active');
    });
});

// ---------- BMI Calculator ----------
function calcBMI() {
    const weight = parseFloat(document.getElementById('bmi-weight').value);
    const height = parseFloat(document.getElementById('bmi-height').value);
    const resultBox = document.getElementById('bmi-result');

    if (!weight || !height || weight <= 0 || height <= 0) {
        alert('Please enter valid weight and height.');
        return;
    }

    const bmi = weight / ((height / 100) ** 2);
    const score = document.getElementById('bmi-score');
    const category = document.getElementById('bmi-category');

    score.textContent = bmi.toFixed(1);

    if (bmi < 18.5)        category.textContent = '⬇️ Underweight — Build Muscle';
    else if (bmi < 25)     category.textContent = '✅ Normal Weight — Keep It Up!';
    else if (bmi < 30)     category.textContent = '⚠️ Overweight — Start Training';
    else                   category.textContent = '🔴 Obese — Consult Our Trainers';

    resultBox.style.display = 'flex';
}

// Expose to HTML onclick
window.calcBMI = calcBMI;

// ---------- Urgency counter (fake-live slots) ----------
// Randomly shows 5–9 to keep it looking dynamic
(function() {
    const slot = Math.floor(Math.random() * 5) + 5;
    document.querySelectorAll('.hero-urgency, .urgency-note, .plans-note').forEach(el => {
        el.textContent = el.textContent.replace(/\d+(?= trial slots| slots)/, slot);
    });
})();
