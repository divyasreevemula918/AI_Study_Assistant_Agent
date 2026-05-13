from langchain_google_genai import ChatGoogleGenerativeAI

def generate_summary(text):

    model = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.3
    )

    prompt = f"""
    Summarize the following text clearly:

    {text}
    """

    response = model.invoke(prompt)

    return response.content