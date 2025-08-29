from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Chatbot replies (you can expand this later)
responses = {
    "hi": "Hello! How can I help you?",
    "hii": "Hello! How can I help you?",
    "hey": "Hello! How can I help you?",
    "hello": "Hello! How can I help you?",
    "admission": "Admissions are open and details are available on the college website.",
    "admission date": "Admissions are open and will continue till November",
    "fees": "Fees depend on the course, Please write course name before fees ,And for more detail please contact the admin office.",
    "btech fees": "General : 1,25,000 Rs || OBC : 75,000 Rs || VJ/NT : 30,000 Rs || SC/ST/Minority : 20,000 Rs",
    "mtech fees": "Please Contact The Admin Office",
    "bca fees": "Please Contact The Admin Office",
    "mba fees": "Please Contact The Admin Office",
    "library" : "We have a big library that have books, CDs, Magzins and Research books",
    "library location": "The library is near Admin Office",
    "library timing": "The library is open from 10 AM to 5 PM.",
    "hostel": "Hostel facilities are not available inside the college.",
    "exam date": "Exams start from 10th October.",
    "syllabus": "Syllabus will be given in the Induction Program and you can also check it on College Website ",
    "bye": "Goodbye! Have a great day.",
    "exit": "Goodbye! Have a great day.",
    "left": "Goodbye! Have a great day."
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_text = request.json.get("message").lower()
    return jsonify({"reply": responses.get(user_text, "Sorry, I don’t know that.")})

if __name__ == "__main__":
    app.run(debug=True)

