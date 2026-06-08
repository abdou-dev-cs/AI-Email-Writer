import os
from dotenv import load_dotenv
from google import genai

load_dotenv()


client = genai.Client(api_key=os.getenv("GENAI_API_KEY"))


def generate_email(content):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"Write a professional email about the following topic: {content} Return only the email without explanations.",
        )

        return response.text

    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    print(os.getenv("GENAI_API_KEY"))
    email_content = input(
        "Enter the content title that you want to generate an email for: "
    )
    email = generate_email(email_content)
    print(email)
