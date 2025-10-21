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

    prompt = (
        f"You are an expert travel planner. Create a safe, family-friendly, detailed {days}-day travel itinerary "
        f"for {destination}. Include day-wise plan, travel tips, and estimated daily budget in USD ({budget}). "
        f"Ensure the response is professional, polite, and does not include any unsafe or restricted content."
    )


    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(prompt)
    
        itinerary_text = None
    
        # Try standard .text property first
        if hasattr(response, "text") and response.text and response.text.strip():
            itinerary_text = response.text.strip()
    
        # Try extracting from candidate parts
        elif hasattr(response, "candidates") and len(response.candidates) > 0:
            parts = response.candidates[0].content.parts
            itinerary_text = " ".join(p.text for p in parts if hasattr(p, "text"))
    
        # If still empty, check for finish_reason
        if not itinerary_text:
            finish_reason = getattr(response.candidates[0], "finish_reason", None)
            if finish_reason == 2:
                itinerary_text = "⚠️ Gemini stopped early due to content filters. Try a different destination or prompt."
            else:
                itinerary_text = "⚠️ No itinerary received from Gemini. Please try again."
    
    except Exception as e:
        itinerary_text = f"Error reading Gemini response: {str(e)}"
    
    result = {"itinerary": itinerary_text}
    return jsonify(result)


    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)







