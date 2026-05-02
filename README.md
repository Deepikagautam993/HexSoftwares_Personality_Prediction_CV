# 🧠 Personality Prediction System Through CV Analysis

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-Web%20App-green.svg)
![Machine Learning](https://img.shields.io/badge/ML-NLP-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## 📌 Project Overview

The **Personality Prediction System Through CV Analysis** is an AI-powered web application that analyzes a candidate’s resume (CV) to predict their personality traits using Machine Learning and Natural Language Processing (NLP).

This system converts unstructured resume data into meaningful insights to help recruiters make **data-driven hiring decisions**.

---

## 🎯 Objectives

* Automate personality analysis from resumes
* Assist recruiters in candidate evaluation
* Apply NLP techniques on real-world data
* Build an end-to-end ML-powered web application

---

## 🚀 Key Features

* 📄 Resume PDF text extraction
* 🧠 Personality prediction using ML (OCEAN model)
* 📊 Graphical visualization of personality traits
* 📄 ATS (Applicant Tracking System) score
* 🧩 Skill extraction from resume
* 🎯 Job description matching system
* 🛠 AI-based resume suggestions
* 🤖 Integrated chatbot (career assistant)
* 🌐 Clean and professional dashboard UI

---

## 🧠 Personality Traits (OCEAN Model)

* Openness
* Conscientiousness
* Extraversion
* Agreeableness
* Emotional Stability

---

## 🏗️ System Architecture

Resume Upload
↓
Text Extraction (PDFMiner)
↓
Text Preprocessing
↓
TF-IDF Vectorization
↓
Machine Learning Model
↓
Personality Prediction
↓
Dashboard Visualization

---

## 🛠️ Tech Stack

| Technology     | Purpose                |
| -------------- | ---------------------- |
| Python         | Core programming       |
| Flask          | Web framework          |
| Scikit-learn   | Machine Learning       |
| PDFMiner       | Resume text extraction |
| Pandas / NumPy | Data processing        |
| Matplotlib     | Graph visualization    |
| HTML / CSS     | Frontend UI            |

---

## 📂 Project Structure

personality-cv-ai/
│
├── app.py
├── utils.py
├── model.pkl
├── vectorizer.pkl
├── dataset.csv
├── requirements.txt
│
├── templates/
│     └── index.html
│
├── static/
│     └── graph.png

---

## 📊 Machine Learning Model

* Algorithm: MultiOutput Naive Bayes
* Feature Extraction: TF-IDF (1-gram & 2-gram)
* Problem Type: Multi-label classification
* Input: Resume text
* Output: Personality traits (OCEAN)

---

## 📸 Screenshots

### 🔹 Dashboard UI

![Dashboard](static/dashboard.png)

### 🔹 Prediction Output

![Prediction](static/prediction.png)

### 🔹 Graph Visualization

![Graph](static/graph.png)

---

## 🎥 Demo Video

👉 Watch full working demo here:
🔗 https://github.com/your-username/personality-cv-ai/blob/main/demo.mp4


---

## 🚀 How to Run

pip install -r requirements.txt
python app.py

Then open:
http://127.0.0.1:5000/

---

## 🧪 Example Workflow

1. Upload a resume (PDF)
2. System extracts text
3. ML model predicts personality traits
4. Dashboard displays:

   * Personality scores
   * Graph
   * ATS score
   * Skills
   * Suggestions

---

## 📈 Future Enhancements

* Deep Learning (BERT-based model)
* Resume ranking system
* AI resume rewriting
* Interview question generator
* Cloud deployment

---

## 💼 Interview Explanation (IMPORTANT)

This project demonstrates an end-to-end AI pipeline:

* Handling unstructured resume data
* Applying NLP preprocessing
* Feature extraction using TF-IDF
* Multi-label classification using ML
* Deployment using Flask
* Integration of real-world features like ATS scoring and skill extraction

It showcases both **Machine Learning + Real-world application development skills**.

---

## 👩‍💻 Author

Deepika Gautam
B.Tech AIML Student
Skills: Python | Machine Learning | Flask | Web Development

---

## ⭐ Support

If you like this project, give it a ⭐ and connect on LinkedIn!
