import pdfminer.high_level
import tempfile
import matplotlib.pyplot as plt
import os
import pickle

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))


# ---------------- PDF TEXT ----------------
def extract_text(file):
    file_bytes = file.read()

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(file_bytes)
        path = tmp.name

    return pdfminer.high_level.extract_text(path)


# ---------------- PREDICTION ----------------
def predict_personality(text):
    X = vectorizer.transform([text])
    preds = model.predict(X)[0]

    return {
        "Openness": int(preds[0] * 100),
        "Conscientiousness": int(preds[1] * 100),
        "Extraversion": int(preds[2] * 100),
        "Agreeableness": int(preds[3] * 100),
        "Emotional Stability": int(preds[4] * 100)
    }


# ---------------- ATS SCORE ----------------
def ats_score(text):
    text = text.lower()

    keywords = [
        "python", "machine learning", "data", "analysis",
        "project", "team", "communication", "sql",
        "ai", "deep learning", "flask"
    ]

    return min(sum(10 for k in keywords if k in text), 100)


# ---------------- GRAPH ----------------
def create_graph(data):
    plt.figure(figsize=(6,4))
    plt.bar(list(data.keys()), list(data.values()))
    plt.title("Personality Analysis (%)")
    plt.xticks(rotation=20)
    plt.tight_layout()

    os.makedirs("static", exist_ok=True)
    path = "static/graph.png"
    plt.savefig(path)
    plt.close()

    return path


# ---------------- EXPLANATION ----------------
def explain_prediction(result):
    return [
        "Creativity level detected.",
        "Work discipline analyzed.",
        "Communication skills evaluated.",
        "Team collaboration estimated.",
        "Stress handling capability inferred."
    ]


# ---------------- SUGGESTIONS ----------------
def resume_suggestions(text):
    text = text.lower()

    suggestions = []

    if "python" not in text:
        suggestions.append("Add Python skills.")

    if "machine learning" not in text:
        suggestions.append("Add ML projects.")

    if "project" not in text:
        suggestions.append("Add real projects.")

    if "github" not in text:
        suggestions.append("Add GitHub profile.")

    if "sql" not in text:
        suggestions.append("Add SQL/database skills.")

    if not suggestions:
        suggestions.append("Excellent ATS optimized resume!")

    return suggestions


# ---------------- SKILLS ----------------
def extract_skills(text):
    text = text.lower()

    skills_db = [
        "python", "java", "c++", "html", "css", "javascript",
        "machine learning", "deep learning", "ai",
        "sql", "mysql", "flask", "django",
        "pandas", "numpy"
    ]

    return [s for s in skills_db if s in text] or ["No strong skills detected"]


# ---------------- CHATBOT ----------------
def ai_career_chat(question):
    question = question.lower()

    if "improve" in question:
        return "Add projects, GitHub, and technical skills like Python & ML."

    if "ats" in question:
        return "ATS depends on keyword matching like Python, ML, SQL."

    if "job" in question:
        return "Build projects + internships + improve technical skills."

    if "skills" in question:
        return "Python, ML, SQL, Data Analysis, Flask are key skills."

    return "Ask about resume improvement, ATS, skills or jobs."