#!/bin/sh

OPENAI_API_KEY="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"
TEMP=$1

curl https://api.openai.com/v1/chat/completions \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "model": "gpt-3.5-turbo",
  "messages": [
    {"role": "user", "content": "気温が${TEMP}度の時の服を60文字で"}
  ]
}'

