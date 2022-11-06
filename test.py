import openai
import os
from os.path import join, dirname
from dotenv import load_dotenv


openai.api_key =  'sk-7F2ogycs6VjlJ6...'

response = openai.Image.create(
  prompt="white cat on dog",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
print(image_url);
