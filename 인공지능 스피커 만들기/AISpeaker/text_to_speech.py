# TTS (Text To Speech)
# STT (Speech To Text)

# gTTS를 이용해서 텍스트를 음성으로 변환 후 저장하는 코드 만듦
from gtts import gTTS
# 실행된 파일을 바로 목소리로 들려줌
from playsound import playsound 

# 영어문장
#text = 'Imagine that you have just arrived at a hotel after a tiring 7-hour overnight flight.'
#file_name = 'sample.mp3'
#tts_en = gTTS(text=text, lang='en')
#tts_en.save(file_name)
#playsound(file_name) # .mp3 파일 재생

# 한글 문장
# text = "저는 기계입니다. 하지만 괜찮아 보이죠?"
# tts_ko = gTTS(text=text, lang='ko')
# file_name = 'sample.mp3'
# tts_ko.save(file_name)
# playsound(file_name)

# 긴 문장
with open('C:/Users/hanyoung/python_05/AISpeaker/sample.txt', 'r', encoding='utf-8') as f:
    text = f.read()

tts_ko = gTTS(text=text, lang='ko')
file_name = 'sample.mp3'
tts_ko.save(file_name)
playsound(file_name)