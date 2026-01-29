"""
Run baseline evaluation of Mistral 7B on the MTG strategy test set.
This establishes the "before fine-tuning" baseline.
"""

import json
import os
from datetime import datetime
from pathlib import Path

from gpt4all import GPT4All

# Paths
PROJECT_ROOT = Path(__file__).parent.parent
MODEL_PATH = PROJECT_ROOT / "mistral-7b" / "mistral-7b-instruct-q4_0.gguf"
TEST_SET_PATH = PROJECT_ROOT / "data" / "eval" / "test_set.json"
RESULTS_DIR = PROJECT_ROOT / "data" / "eval" / "results"


def load_test_set():
    """Load the evaluation test set."""
    with open(TEST_SET_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def create_prompt(question: str) -> str:
    """Create a prompt for the model."""
    return f"""You are a Magic: The Gathering strategy expert. Answer the following question about MTG strategy and gameplay.

Question: {question}

Answer:"""


def run_evaluation():
    """Run all test questions through the model and save results."""

    # Load test set
    print("Loading test set...")
    test_data = load_test_set()
    questions = test_data["questions"]
    print(f"Loaded {len(questions)} questions")

    # Initialize model
    print(f"\nLoading model from {MODEL_PATH}...")
    model = GPT4All(
        model_name=str(MODEL_PATH),
        allow_download=False,
        device="cpu"  # Change to "gpu" if you have GPU support
    )
    print("Model loaded!")

    # Run evaluation
    results = {
        "metadata": {
            "model": "mistral-7b-instruct-q4_0",
            "timestamp": datetime.now().isoformat(),
            "test_set_version": test_data["metadata"]["version"],
            "type": "baseline"
        },
        "responses": []
    }

    print("\nRunning evaluation...")
    print("-" * 60)

    for i, q in enumerate(questions, 1):
        print(f"\n[{i}/{len(questions)}] Category: {q['category']}")
        print(f"Question: {q['question'][:80]}...")

        prompt = create_prompt(q["question"])

        # Generate response
        with model.chat_session():
            response = model.generate(
                prompt,
                max_tokens=500,
                temp=0.7
            )

        print(f"Response: {response[:100]}...")

        results["responses"].append({
            "id": q["id"],
            "category": q["category"],
            "question": q["question"],
            "model_response": response,
            "reference_answer": q["reference_answer"],
            "key_concepts": q["key_concepts"]
        })

    # Save results
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = RESULTS_DIR / f"baseline_{timestamp}.json"

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print("\n" + "=" * 60)
    print(f"Evaluation complete! Results saved to:\n{output_path}")

    return output_path


if __name__ == "__main__":
    run_evaluation()
