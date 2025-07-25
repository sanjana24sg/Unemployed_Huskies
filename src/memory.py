import json
from datetime import datetime
import os

MEMORY_FILE = "learned_topics_log.json"

def log_learning_session(topic: str, summary: str):
    """
    Log the topic, summary, and timestamp to a JSON file.
    """
    entry = {
        "topic": topic,
        "summary": summary,
        "timestamp": datetime.now().isoformat()
    }

    # Load existing memory
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append(entry)

    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=2)

def get_memory():
    """
    Retrieve past learning logs.
    """
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    else:
        return []
