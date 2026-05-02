from flask import Flask, render_template, request, send_file, jsonify
import webbrowser

from utils import (
    extract_text,
    predict_personality,
    create_graph,
    ats_score,
    explain_prediction,
    resume_suggestions,
    extract_skills,
    ai_career_chat
)

app = Flask(__name__)


# ---------------- HOME ----------------
@app.route("/", methods=["GET", "POST"])
def index():

    result = None
    graph = None
    ats = None
    explanation = None
    suggestions = None
    skills = None

    if request.method == "POST":
        file = request.files["resume"]
        file.seek(0)

        text = extract_text(file)

        result = predict_personality(text)
        graph = create_graph(result)
        ats = ats_score(text)
        explanation = explain_prediction(result)
        suggestions = resume_suggestions(text)
        skills = extract_skills(text)

    return render_template(
        "index.html",
        result=result,
        graph=graph,
        ats=ats,
        explanation=explanation,
        suggestions=suggestions,
        skills=skills
    )


# ---------------- CHATBOT API ----------------
@app.route("/chat", methods=["POST"])
def chat():
    q = request.form["question"]
    answer = ai_career_chat(q)
    return jsonify({"answer": answer})


# ---------------- DOWNLOAD ----------------
@app.route("/download")
def download():
    return send_file("static/report.pdf", as_attachment=True)


# ---------------- RUN ----------------
if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:5000/")
    app.run(debug=True)