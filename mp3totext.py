import whisper

model = whisper.load_model("medium")
result = model.transcribe("C:/Users/rssmo/Desktop/youtube.mp3",fp16=False, language='tr')
print(result["text"])


