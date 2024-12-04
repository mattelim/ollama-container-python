### Create and activate env

```bash
python -m venv ./.venv
```

### Install packages

```bash
pip install -r requirements.txt
```

### Setup ENV variables

Edit `.env.example` and save it as `.env`

Tip: You can generate a random number from `API_KEY` using `openssl rand -base64 24` in `bash`

### Run Flask in debug mode and test the API

```bash
python server.py
```

In a separate terminal:

```bash
curl http://localhost:5001/chat \
-H "Content-Type: application/json" \
-H "Authorization: Bearer YOUR_API_KEY" \
-d '{
    "model": "llama3.2",
    "messages": [
      {
        "role": "system",
        "content": "You are a helpful assistant."
      },
      {
        "role": "user",
        "content": "Hello!"
      }
    ]
  }'
```

It should return a chat completion object that looks like:

```json
{
  "created_at": "2024-12-03T15:18:39.220212972Z",
  "done": true,
  "done_reason": "stop",
  "eval_count": 10,
  "eval_duration": 51000000,
  "load_duration": 9762533,
  "message": {
    "content": "Hello! How can I assist you today?",
    "role": "assistant"
  },
  "model": "llama3.2",
  "prompt_eval_count": 33,
  "prompt_eval_duration": 1000000,
  "total_duration": 62777836
}
```
