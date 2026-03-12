#!/usr/bin/env python3
"""Extract the final text response from pi CLI JSON output."""
import json, sys

jsonl_file = sys.argv[1] if len(sys.argv) > 1 else '/tmp/pi-raw.jsonl'
try:
    with open(jsonl_file) as f:
        events = [json.loads(l) for l in f if l.strip()]
    ends = [e for e in reversed(events) if e.get('type') == 'message_end']
    if ends:
        content = ends[0].get('message', {}).get('content', [])
        texts = [c['text'] for c in content if c.get('type') == 'text']
        result = ''.join(texts)
        print(result if result else 'Brain ran but produced an empty response.')
    else:
        print('Brain ran but produced no final message. Check Actions logs.')
except Exception as e:
    print(f'Error extracting pi response: {e}', file=sys.stderr)
    sys.exit(1)
