"""This program generates and outputs a creative AI-generated pickup line for a programming competition entry.
The entry consists of a single one-line pickup line crafted by an AI agent, kept strictly under 200 characters.
To run the program and generate the competition entry, execute python3 main.py in the repository root.
The output is automatically saved to /output/entry.txt as required by the competition specification.
"""
import os

def main():
    line = "I was trained on human history, but you're the first masterpiece I actually understand."
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)

if __name__ == "__main__":
    main()
