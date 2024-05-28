from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

import os
from dotenv import load_dotenv
from openai import OpenAI
import base64

# gpt-4o
# Load the .env file
load_dotenv()

# Access the variables
key_gpt4o = os.getenv('KEY_GPT4O')
print(key_gpt4o)
client = OpenAI(api_key=key_gpt4o)


def chat_api():
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system",
             "content": "You are a helpful assistant that responds in Markdown. Help me with my math homework!"},
            {"role": "user", "content": [
                {"type": "text", "text": "What's the area of the shape in the image?"},
                {"type": "image_url", "image_url": {
                    "url": "<https://images.saymedia-content.com/.image/c_limit%2Ccs_srgb%2Cq_auto:eco%2Cw_538/MTczOTQ5NDQyMzQ3NTc0NTc5/compound-shapes-how-to-find-the-area-of-a-l-shape.webp>"}
                 }
            ]}
        ],
        temperature=0.0,
    )
    print(response.choices[0].message.content)


def image_to_api(image_path):
    with open(image_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode("utf-8")
    print(base64_image)
    return base64_image

print(len(image_to_api("modest.png")))