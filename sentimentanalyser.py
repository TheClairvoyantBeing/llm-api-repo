"""
Groq API - Sentiment Analyser
"""

from groq import Groq

client = Groq(
    api_key = ""
)

def analyse_sentiment(text):
    """Analyse Sentiment of Text"""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role":"system",
                "content":"You are a sentiment analysis exprert. Classify the sentiment as positive, Negative or Neutral. Provide a confidence score."
            },
            {
                "role":"user",
                "content":f"Analyse the sentiment of {text}"
            }
        ],
        temperature=0.2
    )
    return response.choices[0].message.content

reviews = [
    "This product is amazing! I love it!",
    "Terrible quality, Waste of money.",
    "It's ok, nothing spcial."
]

for review in reviews:
    print(f"\nReview: {review}")
    print(f"Sentiment: {analyse_sentiment(review)}")
