from src.executor import (
    generate_study_notes,
    generate_study_plan,
    generate_quiz,
    generate_revision_recap
)

def plan_learning(topic: str) -> dict:
    """
    Breaks the user's goal into sub-tasks and runs the corresponding executors.
    Returns all results in a structured dictionary.
    """
    result = {
        "topic": topic,
        "study_plan": generate_study_plan(topic),
        "study_notes": generate_study_notes(topic),
        "quiz": generate_quiz(topic),
        "revision": generate_revision_recap(topic)
    }
    return result
