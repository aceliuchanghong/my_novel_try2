import requests
from openai import OpenAI
import os

API_KEY = os.getenv("BRICK_API_KEY")  # 从本地环境变量获取API密钥
BASE_URL = "https://api.deepbricks.ai/v1/"

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

resp = client.images.generate(
  model="dall-e-3",
  prompt="""A scene in traditional Chinese Xianxia style, facing a mountain peak""",
  n=1,
  size="1024x1024",
  quality="hd"
)

# save image
image_resp = requests.get(resp.data[0].url)
with open("../z_using_files/example.png", "wb") as fw:
  fw.write(image_resp.content)
