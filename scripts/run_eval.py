"""
Run the 20-question evaluation against the fine-tuned model.

Usage:
    conda activate mtg-llm
    cd C:\claude_projects\mtg-std-llm
    python scripts/run_eval.py
"""

import json
import torch
from datetime import datetime
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from peft import PeftModel

# Configuration
BASE_MODEL = "mistralai/Mistral-7B-Instruct-v0.2"
ADAPTER_PATH = "models/mtg-mistral-lora"
TEST_SET_PATH = "data/eval/test_set.json"
OUTPUT_DIR = "data/eval/results"


def load_model():
    """Load the fine-tuned model."""
    print("Loading fine-tuned model...")

    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16,
        bnb_4bit_use_double_quant=True,
    )

    tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL)
    tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        BASE_MODEL,
        quantization_config=bnb_config,
        device_map="auto",
    )

    model = PeftModel.from_pretrained(model, ADAPTER_PATH)
    print("Model loaded.")

    return model, tokenizer


def generate_response(model, tokenizer, question):
    """Generate a response to a question."""
    prompt = f"<s>[INST] {question} [/INST]"

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=300,
            temperature=0.7,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id,
        )

    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    if "[/INST]" in response:
        response = response.split("[/INST]")[-1].strip()

    return response


def run_evaluation(model, tokenizer):
    """Run evaluation on all test questions."""
    print(f"Loading test set from {TEST_SET_PATH}...")

    with open(TEST_SET_PATH, "r", encoding="utf-8") as f:
        test_data = json.load(f)

    questions = test_data["questions"]
    print(f"Running evaluation on {len(questions)} questions...\n")

    results = {
        "metadata": {
            "model": "mtg-mistral-lora (fine-tuned)",
            "base_model": BASE_MODEL,
            "adapter_path": ADAPTER_PATH,
            "timestamp": datetime.now().isoformat(),
            "test_set_version": test_data["metadata"]["version"],
            "type": "fine-tuned"
        },
        "responses": []
    }

    for i, q in enumerate(questions, 1):
        print(f"[{i}/{len(questions)}] {q['category']}: {q['question'][:50]}...")

        response = generate_response(model, tokenizer, q["question"])

        results["responses"].append({
            "id": q["id"],
            "category": q["category"],
            "question": q["question"],
            "model_response": response,
            "reference_answer": q["reference_answer"],
            "key_concepts": q["key_concepts"]
        })

        # Print response preview
        preview = response[:100] + "..." if len(response) > 100 else response
        print(f"    Response: {preview}\n")

    return results


def save_results(results):
    """Save evaluation results to JSON."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = f"{OUTPUT_DIR}/finetuned_{timestamp}.json"

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    print(f"Results saved to {output_path}")
    return output_path


def main():
    print("=" * 60)
    print("MTG Fine-Tuned Model Evaluation")
    print("=" * 60)

    if not torch.cuda.is_available():
        raise RuntimeError("CUDA not available")
    print(f"GPU: {torch.cuda.get_device_name(0)}\n")

    model, tokenizer = load_model()
    results = run_evaluation(model, tokenizer)
    output_path = save_results(results)

    print("\n" + "=" * 60)
    print("Evaluation complete!")
    print(f"Results: {output_path}")
    print("=" * 60)


if __name__ == "__main__":
    main()
