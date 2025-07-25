import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Create the Gemini model
model = genai.GenerativeModel(model_name="models/gemini-2.5-flash")


# === Agentic Gemini Executors ===

def generate_study_notes(topic: str) -> str:
    """
    Generate helpful conceptual notes or explanations for any topic, concept, or coding problem.
    """
    prompt = f"""
You're an intelligent agent. Provide a clear, concise explanation for the following topic or problem: '{topic}'.

Include:
- Key definitions or principles
- 1–2 examples (if applicable)
- Summary of key takeaways

Adapt the response based on the topic. If it's a coding or LeetCode problem, explain the logic, approach, and edge cases.
"""
    response = model.generate_content(prompt)
    return response.text.strip()

def generate_study_plan(topic: str) -> str:
    """
    Create a 3-day structured study or practice plan for the given topic.
    """
    prompt = f"""
Create a 3-day plan to help someone learn and apply the topic: '{topic}'.

Each day should include:
- 2–3 learning subgoals
- Suggested resources or exercises (e.g., videos, LeetCode, blog)
- Optional application/practice ideas
"""
    response = model.generate_content(prompt)
    return response.text.strip()

def generate_quiz(topic: str) -> str:
    """
    Generate a quiz tailored to the given topic or problem.
    """
    prompt = f"""
Generate a quiz to test understanding of the topic: '{topic}'.

Include:
- 3 multiple-choice questions
- 2 fill-in-the-blank questions
- Correct answers with brief explanations

If it's a technical or coding topic, include code-based questions.
"""
    response = model.generate_content(prompt)
    return response.text.strip()

def generate_revision_recap(topic: str) -> str:
    """
    Provide a recap summary and test knowledge retention for a topic.
    """
    prompt = f"""
You're a smart revision agent. Recap key ideas for the topic: '{topic}'.

Include:
- 3 bullet-point summary
- 3 review questions (mixed type)
- 1 tricky or higher-order thinking question
"""
    response = model.generate_content(prompt)
    return response.text.strip()

