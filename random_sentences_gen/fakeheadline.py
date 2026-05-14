import random
import json
from datetime import datetime

subjects = [
    "Shahrukh Khan",
    "Salman Khan",
    "Amir Khan",
    "Hrithik Roshan",
    "Ranbir Kapoor",
]

moods = {
    "funny": {
        "actions": [
            "is dancing badly",
            "is slipping",
            "is eating 20 burgers",
        ],
        "objects": [
            "in the bathroom",
            "on the road",
            "inside the mall",
        ]
    },

    "action": {
        "actions": [
            "is fighting villains",
            "is jumping from helicopters",
            "is chasing criminals",
        ],
        "objects": [
            "on the highway",
            "in Mumbai",
            "inside the jungle",
        ]
    },

    "romantic": {
        "actions": [
            "is singing for someone",
            "is proposing",
            "is writing love letters",
        ],
        "objects": [
            "in the rain",
            "at the beach",
            "under the moonlight",
        ]
    }
}

history = []
generated_sentences = set()

stats = {
    "funny": 0,
    "action": 0,
    "romantic": 0
}


def choose_mood():
    while True:

        mood = input(
            "\nChoose mood (funny/action/romantic): "
        ).lower()

        if mood in moods:
            return mood

        print("Invalid mood. Try again.")


def generate_sentence(mood):

    while True:

        subject = random.choice(subjects)
        action = random.choice(moods[mood]["actions"])
        obj = random.choice(moods[mood]["objects"])

        sentence = f"{subject} {action} {obj}."

        if sentence not in generated_sentences:

            generated_sentences.add(sentence)

            timestamp = datetime.now().strftime("%I:%M:%S %p")

            final_sentence = f"[{timestamp}] {sentence}"

            history.append({
                "mood": mood,
                "sentence": final_sentence
            })

            stats[mood] += 1

            print("\nGenerated Sentence:")
            print(final_sentence)

            break


def show_history():

    if not history:
        print("\nNo history found.")
        return

    print("\nSentence History:\n")

    for item in history:
        print(f"{item['mood'].upper()} -> {item['sentence']}")


def save_to_text():

    with open("history.txt", "a") as file:

        for item in history:
            file.write(
                f"{item['mood']} -> {item['sentence']}\n"
            )

    print("\nHistory saved to history.txt")


def save_to_json():

    with open("history.json", "w") as file:
        json.dump(history, file, indent=4)

    print("\nHistory saved to history.json")


def show_stats():

    print("\nStatistics:\n")

    total = sum(stats.values())

    print(f"Total Sentences: {total}")

    for mood, count in stats.items():
        print(f"{mood.capitalize()}: {count}")


def main():

    print("=== AI Sentence Generator ===")

    current_mood = choose_mood()

    while True:

        print("\n===== MENU =====")
        print("1. Generate Sentence")
        print("2. Show History")
        print("3. Save History to TXT")
        print("4. Save History to JSON")
        print("5. Show Statistics")
        print("6. Change Mood")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            generate_sentence(current_mood)

        elif choice == "2":
            show_history()

        elif choice == "3":
            save_to_text()

        elif choice == "4":
            save_to_json()

        elif choice == "5":
            show_stats()

        elif choice == "6":
            current_mood = choose_mood()

        elif choice == "7":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid choice.")


if __name__ == "__main__":
    main()
    