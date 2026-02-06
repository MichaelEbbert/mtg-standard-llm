"""
Fine-tune Mistral 7B on MTG strategy reasoning using QLoRA.

Usage:
    conda activate mtg-llm
    cd C:\claude_projects\mtg-std-llm
    python scripts/finetune.py
"""

import json
import torch
from datasets import Dataset
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
)
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from trl import SFTTrainer, SFTConfig

# =============================================================================
# Configuration
# =============================================================================

# Model to fine-tune
MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.2"

# Training data
TRAINING_DATA_PATH = "data/processed/finetune/training_pairs.json"

# Output directory for the fine-tuned adapter
OUTPUT_DIR = "models/mtg-mistral-lora"

# LoRA configuration
LORA_R = 16              # Rank - higher = more capacity, more memory
LORA_ALPHA = 32          # Scaling factor
LORA_DROPOUT = 0.05      # Regularization

# Training configuration
EPOCHS = 3
BATCH_SIZE = 1           # Small batch for 12GB VRAM
GRADIENT_ACCUMULATION = 4  # Effective batch size = 1 * 4 = 4
LEARNING_RATE = 2e-4
MAX_SEQ_LENGTH = 512     # Max tokens per example
WARMUP_STEPS = 10

# =============================================================================
# Helper Functions
# =============================================================================

def format_instruction(example):
    """Convert our training format to Mistral's instruction format."""
    instruction = example["instruction"]
    output = example["output"]

    # Mistral instruction format
    text = f"<s>[INST] {instruction} [/INST] {output}</s>"
    return {"text": text}


def load_training_data(path):
    """Load training data from JSON and convert to Dataset."""
    print(f"Loading training data from {path}...")

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    training_examples = data["training_data"]
    print(f"Loaded {len(training_examples)} training examples")

    # Convert to Hugging Face Dataset
    dataset = Dataset.from_list(training_examples)

    # Format for Mistral
    dataset = dataset.map(format_instruction)

    return dataset


def setup_model_and_tokenizer():
    """Load model in 4-bit and prepare for training."""
    print(f"Loading {MODEL_NAME} in 4-bit precision...")

    # 4-bit quantization config
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16,
        bnb_4bit_use_double_quant=True,
    )

    # Load tokenizer
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"

    # Load model
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        quantization_config=bnb_config,
        device_map="auto",
        trust_remote_code=True,
    )

    # Prepare for k-bit training
    model = prepare_model_for_kbit_training(model)

    # LoRA configuration
    lora_config = LoraConfig(
        r=LORA_R,
        lora_alpha=LORA_ALPHA,
        lora_dropout=LORA_DROPOUT,
        bias="none",
        task_type="CAUSAL_LM",
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj"],  # Attention layers
    )

    # Apply LoRA
    model = get_peft_model(model, lora_config)

    # Print trainable parameters
    trainable, total = model.get_nb_trainable_parameters()
    print(f"Trainable parameters: {trainable:,} / {total:,} ({100 * trainable / total:.2f}%)")

    return model, tokenizer


def train(model, tokenizer, dataset):
    """Run the fine-tuning."""
    print("Setting up training...")

    sft_config = SFTConfig(
        output_dir=OUTPUT_DIR,
        num_train_epochs=EPOCHS,
        per_device_train_batch_size=BATCH_SIZE,
        gradient_accumulation_steps=GRADIENT_ACCUMULATION,
        learning_rate=LEARNING_RATE,
        warmup_steps=WARMUP_STEPS,
        logging_steps=10,
        save_strategy="epoch",
        bf16=True,  # Use BF16 to match model's compute dtype
        optim="paged_adamw_8bit",  # Memory-efficient optimizer
        report_to="none",  # Disable wandb/tensorboard
        dataset_text_field="text",  # Column containing formatted text
    )

    trainer = SFTTrainer(
        model=model,
        train_dataset=dataset,
        processing_class=tokenizer,
        args=sft_config,
    )

    print("Starting training...")
    print(f"  Epochs: {EPOCHS}")
    print(f"  Batch size: {BATCH_SIZE} (effective: {BATCH_SIZE * GRADIENT_ACCUMULATION})")
    print(f"  Learning rate: {LEARNING_RATE}")
    print(f"  Training examples: {len(dataset)}")
    print("-" * 50)

    trainer.train()

    # Save the adapter
    print(f"Saving adapter to {OUTPUT_DIR}...")
    model.save_pretrained(OUTPUT_DIR)
    tokenizer.save_pretrained(OUTPUT_DIR)

    print("Training complete!")


# =============================================================================
# Main
# =============================================================================

def main():
    print("=" * 50)
    print("MTG Strategy Fine-Tuning with QLoRA")
    print("=" * 50)

    # Check CUDA
    if not torch.cuda.is_available():
        raise RuntimeError("CUDA not available. GPU required for training.")
    print(f"Using GPU: {torch.cuda.get_device_name(0)}")
    print(f"VRAM: {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f} GB")
    print()

    # Load data
    dataset = load_training_data(TRAINING_DATA_PATH)

    # Setup model
    model, tokenizer = setup_model_and_tokenizer()

    # Train
    train(model, tokenizer, dataset)

    print()
    print("=" * 50)
    print("Done! Adapter saved to:", OUTPUT_DIR)
    print("=" * 50)


if __name__ == "__main__":
    main()
