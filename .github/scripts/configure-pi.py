#!/usr/bin/env python3
"""Configure pi CLI with Alibaba Cloud DashScope provider."""
import json, os

config = {
    "providers": {
        "alibaba": {
            "baseUrl": "https://coding-intl.dashscope.aliyuncs.com/v1",
            "api": "openai-completions",
            "apiKey": "ALIKEY",
            "models": [
                {
                    "id": "qwen3.5-plus",
                    "name": "Qwen3.5-Plus (Alibaba Cloud)",
                    "reasoning": False,
                    "input": ["text", "image"],
                    "contextWindow": 131072,
                    "maxTokens": 16384
                }
            ]
        }
    }
}

path = os.path.expanduser("~/.pi/agent/models.json")
os.makedirs(os.path.dirname(path), exist_ok=True)
with open(path, "w") as f:
    json.dump(config, f, indent=2)
print(f"pi configured: {path}")
print(f"Provider: alibaba / qwen3.5-plus")
