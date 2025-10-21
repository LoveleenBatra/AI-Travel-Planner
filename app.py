import os
from fpdf import FPDF
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import google.generativeai as genai

# 🔹 Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "AI Travel Planner Backend is Running 🚀"

@app.route("/plan", methods=["POST"])
def plan_trip():
    data = request.get_json()
    destination = data.get("destination")
    days = data.get("days")
    budget = data.get("budget")
    pdf_needed = data.get("pdf", False)  # Check if user requested PDF

    if not destination or not days:
        return jsonify({"error": "Destination and days are required"}), 400

    prompt = f"""
    Create a detailed {days}-day student-friendly travel itinerary for {destination}.
    Include budget-friendly food, transport, and sightseeing recommendations.
    Total budget: ₹{budget if budget else 'not specified'}.
    """

    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(
            prompt,
            generation_config={"max_output_tokens": 1000},
            request_options={"timeout": 40}
        )


        if hasattr(response, "text") and response.text.strip():
            itinerary_text = response.text.strip()
        else:
            itinerary_text = "No itinerary text returned from Gemini."

        result = {"itinerary": itinerary_text}

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)





