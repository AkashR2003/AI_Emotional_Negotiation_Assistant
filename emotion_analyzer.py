from transformers import pipeline

emotion_model = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    top_k=1
)

def analyze_emotion(text):
    result = emotion_model(text)[0][0]
    return {
        "emotion": result["label"],
        "confidence": round(result["score"], 2)
    }