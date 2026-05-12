def detect_intent(text):
    text = text.lower()

    if any(word in text for word in ["price", "cost", "budget", "discount"]):
        return "price negotiation"

    if any(word in text for word in ["deadline", "urgent", "quickly", "delay"]):
        return "deadline pressure"

    if any(word in text for word in ["not satisfied", "unhappy", "problem", "issue"]):
        return "complaint"

    if any(word in text for word in ["deal", "agreement", "contract", "proposal"]):
        return "business negotiation"

    return "general conversation"