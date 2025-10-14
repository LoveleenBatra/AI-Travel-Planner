# 🎒 AI Travel Planner for Students

An AI-powered web application that generates **budget-friendly travel itineraries for students** using Google Gemini API. Users can input their destination, budget (in INR), and number of days, and get a detailed, interactive itinerary.

---

## 🔹 Problem Statement

Planning a trip on a budget can be challenging for students. Traditional travel guides may not provide personalized or cost-efficient suggestions. This project aims to **automate travel planning** by leveraging AI to create personalized itineraries based on user inputs.

---

## 🔹 System Development Approach (Technology Used)

| Component | Technology / Library |
|-----------|--------------------|
| Backend | Python, Flask, Flask-CORS |
| AI Model | Google Gemini API (gemini-2.5-flash) |
| Frontend | HTML, CSS, JavaScript |
| Deployment | Render.com |
| PDF/Text Export | Skipped (planned but not included due to API limitations) |
| Database (Optional) | SQLite (for storing previous itineraries) |

---

## 🔹 Algorithm & Deployment (Step-by-Step Procedure)

### 1️⃣ Backend (Flask + Gemini API)
1. Configure Gemini API key using environment variables.
2. Expose a POST endpoint `/plan` that accepts:
   - `destination`
   - `budget`
   - `days`
3. Generate a prompt for Gemini API:
4. Call Gemini API to get itinerary text.
5. Return JSON response to frontend.

### 2️⃣ Frontend (HTML + JS)
1. Form to input destination, budget, and days.
2. Emoji animation displayed while itinerary is being generated:
- 👕 → 🎒 → 🚌 → 🏛️ → 🍕
3. Display generated itinerary **below the form** without hiding it.
4. Convert Markdown-style Gemini output to HTML for better readability.

### 3️⃣ Deployment (Render.com)
1. Create a Render web service.
2. Set environment variable `GEMINI_API_KEY`.
3. Deploy backend as Flask app (`app.py`).
4. Serve frontend as static HTML/CSS/JS (option B: separate HTML file).
5. Ensure CORS is enabled to allow frontend to communicate with backend.

---

## 🔹 Result

- Successfully generates interactive itineraries for student travelers.
- Loading animation provides visual feedback during AI response generation.
- The form remains visible after generating the itinerary.
- Emoji feedback shows successful completion:
- ✅ Itinerary Generated! 🗺️✈️🍽️🏨

---

## 🔹 Conclusion

- AI-based travel planning for students is achievable with Gemini API and Flask.
- The system provides **budget-conscious, personalized itineraries** quickly.
- Interactive UI and emoji feedback enhance user experience.

---

## 🔹 Future Scope (Optional)

- Include **PDF or TXT download** of the itinerary.
- Save itineraries to a database for historical reference.
- Add **user authentication** to personalize suggestions.
- Extend to **multi-language support** for international students.

---

## 🔹 References

1. [Flask Documentation](https://flask.palletsprojects.com/)
2. [Google Generative AI (Gemini) API](https://developers.generativeai.google/)
3. [Render Deployment Guide](https://render.com/docs)
4. [FPDF Documentation](https://pyfpdf.github.io/fpdf2/)
5. JavaScript Fetch API – MDN Web Docs

---

## 🔹 How to Run Locally

# Install dependencies
pip install -r requirements.txt

# Set environment variabl
set GEMINI_API_KEY=YOUR_API_KEY       # Windows

# Run Flask app
python app.py

# Open frontend in browser (HTML file)
