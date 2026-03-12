#!/usr/bin/env python3
"""Simple Alibaba Cloud LLM call for summarization tasks."""
import os, sys, argparse, json
import urllib.request, urllib.error

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', default='qwen3.5-plus')
    parser.add_argument('--prompt', required=True)
    parser.add_argument('--system', default='You are a helpful assistant.')
    args = parser.parse_args()

    api_key = os.environ.get('ALIKEY', '')
    base_url = os.environ.get('ALIURL', 'https://coding-intl.dashscope.aliyuncs.com/v1')

    if not api_key:
        print("Error: ALIKEY not set", file=sys.stderr)
        sys.exit(1)

    url = f"{base_url.rstrip('/')}/chat/completions"
    payload = {
        "model": args.model,
        "messages": [
            {"role": "system", "content": args.system},
            {"role": "user", "content": args.prompt}
        ],
        "max_tokens": 1024
    }
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    req = urllib.request.Request(url, data=json.dumps(payload).encode(), headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.loads(resp.read())
            print(data['choices'][0]['message']['content'])
    except urllib.error.HTTPError as e:
        print(f"HTTP error: {e.code} {e.read().decode()}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
