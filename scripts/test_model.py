"""
Test the fine-tuned MTG model vs base Mistral.

Usage:
    conda activate mtg-llm
    cd D:\claude_projects\mtg-std-llm
    python scripts/test_model.py
"""

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from peft import PeftModel

# Configuration
BASE_MODEL = "mistralai/Mistral-7B-Instruct-v0.2"
ADAPTER_PATH = "models/mtg-mistral-lora"

# Test questions
TEST_QUESTIONS = [
    "What is card advantage?",
    "What is mana screw?",
    "How does deathtouch interact with trample?",
    "When should a player chump block?",
    "What is the difference between aggro and control decks?",
]


def load_model(use_adapter=True):
    """Load model with or without the fine-tuned adapter."""
    print(f"Loading model (adapter={'ON' if use_adapter else 'OFF'})...")

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

    if use_adapter:
        model = PeftModel.from_pretrained(model, ADAPTER_PATH)

    return model, tokenizer


def generate_response(model, tokenizer, question):
    """Generate a response to a question."""
    prompt = f"<s>[INST] {question} [/INST]"

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=200,
            temperature=0.7,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id,
        )

    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    # Extract just the response part (after [/INST])
    if "[/INST]" in response:
        response = response.split("[/INST]")[-1].strip()

    return response


def main():
    print("=" * 60)
    print("Testing Fine-Tuned MTG Model")
    print("=" * 60)

    # Load fine-tuned model
    model, tokenizer = load_model(use_adapter=True)

    print("\n" + "=" * 60)
    print("FINE-TUNED MODEL RESPONSES")
    print("=" * 60)

    for i, question in enumerate(TEST_QUESTIONS, 1):
        print(f"\n--- Question {i} ---")
        print(f"Q: {question}")
        response = generate_response(model, tokenizer, question)
        print(f"A: {response}")
        print()

    print("=" * 60)
    print("Testing complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
