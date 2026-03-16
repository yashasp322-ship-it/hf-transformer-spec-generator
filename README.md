# HF Transformer Spec Generator

Prototype tool to automatically extract transformer architecture
specifications from HuggingFace model configurations.

## Example

python generator.py mistralai/Mistral-7B-v0.1

## Output

{
  "model_name": "mistralai/Mistral-7B-v0.1",
  "hidden_size": 4096,
  "num_layers": 32,
  "num_attention_heads": 32,
  "num_key_value_heads": 8,
  "intermediate_size": 14336
}

## Tested Models

- mistralai/Mistral-7B-v0.1
- tiiuae/falcon-7b
- EleutherAI/gpt-neox-20b
