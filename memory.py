import json
import os

MEMORY_FILE = "data/memory.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}
    with open(MEMORY_FILE, "r") as f:
       data = json.load(f)
    
    if data is None:
        return {}
    
    return data
        
def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f)

def remember(key, value):
    memory = load_memory()

    if memory is None:
        memory = {}
        
    memory[key] = value
    save_memory(memory)

def recall(key):
    memory = load_memory()
    return memory.get(key, None)