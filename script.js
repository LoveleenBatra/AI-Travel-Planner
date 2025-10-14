// Emoji animation sequence
const emojiSequence = ["👕", "🎒", "🚌", "🏛️", "🍕"]; // clothes → bag → travel → building → food
let emojiIndex = 0;
let emojiInterval;

// Listen to form submit
document.getElementById("travelForm").addEventListener("submit", async function (e) {
  e.preventDefault();

  const destination = document.getElementById("destination").value;
  const budget = document.getElementById("budget").value;
  const days = document.getElementById("days").value;
  // Show loading and hide previous output
  document.getElementById("loading").style.display = "block";
  document.getElementById("output").style.display = "none";

  // Start emoji animation
  const emojiSpan = document.getElementById("emoji");
  emojiInterval = setInterval(() => {
    emojiSpan.textContent = emojiSequence[emojiIndex];
    emojiIndex = (emojiIndex + 1) % emojiSequence.length;
  }, 500); // change emoji every 0.5s

  try {
    const response = await fetch(" https://ai-travel-planner-1-qdnd.onrender.com", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ destination, budget, days, pdf: wantPDF }),
    });

    const data = await response.json();

    // Stop emoji animation
    clearInterval(emojiInterval);
    // Show final message with correct emoji
    document.getElementById("loading").textContent = "✅ Itinerary Generated! 🗺️✈️🍽️🏨";
    // Small delay to make transition smooth
    setTimeout(() => {
        document.getElementById("loading").style.display = "none";
        document.getElementById("output").style.display = "block";
    }, 2000);

    const itineraryDiv = document.getElementById("itinerary");
    if (data.itinerary) {
      // Convert Markdown-style text from Gemini to HTML
      let formatted = data.itinerary
        .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>")   // bold
        .replace(/\n### Day (\d+):/g, "<h3>📅 Day $1</h3>") // day headings
        .replace(/\n/g, "<br>");                             // line breaks

      itineraryDiv.innerHTML = formatted;

    } else {
      itineraryDiv.innerHTML = "⚠️ No itinerary received.";
    }

  } catch (error) {
    clearInterval(emojiInterval);
    emojiSpan.textContent = "❌";
    document.getElementById("loading").style.display = "none";
    alert("Error connecting to the backend. Please check if Flask is running.");
    console.error(error);
  }
});

