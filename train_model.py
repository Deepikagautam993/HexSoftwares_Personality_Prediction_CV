import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.multioutput import MultiOutputClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle

# Load dataset
df = pd.read_csv("dataset.csv")

# Features
X_text = df["text"]

# Labels
y = df[
    [
        "openness",
        "conscientiousness",
        "extraversion",
        "agreeableness",
        "emotional_stability"
    ]
]

# TF-IDF (GOOD CONFIG FOR NLP)
vectorizer = TfidfVectorizer(
    ngram_range=(1, 2),
    stop_words="english",
    max_features=1000
)

X = vectorizer.fit_transform(X_text)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# ✅ BETTER MODEL (IMPORTANT FIX)
model = MultiOutputClassifier(LogisticRegression(max_iter=200))

# Train
model.fit(X_train, y_train)

# Accuracy (better way)
score = model.score(X_test, y_test)
print("Model Accuracy:", score)

# Save model
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model trained successfully!")