from textblob import TextBlob
from emotion_analyzer import analyze_emotion
from intent_detector import detect_intent
from response_advisor import suggest_strategy

def analyze_message(text):
    sentiment_score = TextBlob(text).sentiment.polarity

    if sentiment_score > 0:
        sentiment = "positive"
    elif sentiment_score < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    emotion_result = analyze_emotion(text)
    intent = detect_intent(text)
    advice = suggest_strategy(emotion_result["emotion"], intent)

    return {
        "input_message": text,
        "sentiment": sentiment,
        "sentiment_score": round(sentiment_score, 2),
        "emotion": emotion_result["emotion"],
        "emotion_confidence": emotion_result["confidence"],
        "intent": intent,
        "advice": advice
    }

if __name__ == "__main__":
    user_text = input("Enter negotiation message: ")
    result = analyze_message(user_text)

    print("\n--- Analysis Result ---")
    for key, value in result.items():
        print(f"{key}: {value}")