from langchain_google_genai import ChatGoogleGenerativeAI

def generate_quiz(text):

    model = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.5
    )

    prompt = f"""
    Generate 5 MCQ quiz questions from:

    {text}

    Include answers.
    """

    response = model.invoke(prompt)

    return response.content