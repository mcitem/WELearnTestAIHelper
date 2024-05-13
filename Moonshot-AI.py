from openai import OpenAI
from utils.config import config
f =open('./output.txt','rt',encoding='utf-8')
client = OpenAI(
    api_key = config['kimi'],
    base_url = "https://api.moonshot.cn/v1",
)
 
response = client.chat.completions.create(
    model="moonshot-v1-8k",
    messages=[
        {
            "role": "system",
            "content": "请给我下面英文题目最有可能的答案，不需要解释过程",
        },
        {"role": "user", "content": f.read()},
    ],
    temperature=0.3,
    stream=True,
)
 
collected_messages = []
for idx, chunk in enumerate(response):
    # print("Chunk received, value: ", chunk)
    chunk_message = chunk.choices[0].delta
    if not chunk_message.content:
        continue
    collected_messages.append(chunk_message)  # save the message
    print(f"#{idx}: {''.join([m.content for m in collected_messages])}")
    
print(f"Full conversation received: {''.join([m.content for m in collected_messages])}")