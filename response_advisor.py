def suggest_strategy(emotion, intent):
    if emotion in ["anger", "disgust"]:
        tone = "calm, respectful, and solution-focused"
    elif emotion in ["fear", "sadness"]:
        tone = "reassuring and supportive"
    elif intent == "price negotiation":
        tone = "confident, value-focused, and polite"
    elif intent == "deadline pressure":
        tone = "clear, realistic, and professional"
    else:
        tone = "friendly and professional"

    return f"Recommended tone: {tone}"