from transformers import AutoConfig
import json
import sys

def generate_spec(model_name):
    config = AutoConfig.from_pretrained(model_name)

    spec = {
        "model_name": model_name,
        "hidden_size": getattr(config, "hidden_size", None),
        "num_layers": getattr(config, "num_hidden_layers", None),
        "num_attention_heads": getattr(config, "num_attention_heads", None),
        "num_key_value_heads": getattr(config, "num_key_value_heads", None),
        "intermediate_size": getattr(config, "intermediate_size", None)
    }

    return spec

if __name__ == "__main__":
    model = sys.argv[1]
    spec = generate_spec(model)

    print(json.dumps(spec, indent=2))
