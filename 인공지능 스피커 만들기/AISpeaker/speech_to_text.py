import speech_recognition as sr

# 마이크로부터 음성 듣기
r = sr.Recognizer()
with sr.Microphone() as source:
    print('듣고 있어요')
    audio = r.listen(source) # 마이크로부터 음성 듣기
    
# 파일로부터 음성 불러오기 (wav, aiff, flac 가능, mp3는 불가)
r = sr.Recognizer()
with sr.AudioFile('sample.wav') as source:
    audio = r.record(source)
    
try:
    # google API 사용 (하루 50회 제한)
    # 영어 문장
    # text = r.recognize_google(audio, language='en-US')
    # print(text)
    
    # 한글 문장
    text = r.recognize_google(audio, language='ko')
    print(text)
    
except sr.UnknownValueError:
    print("인식 실패했어요")
except sr.RequestError as e:
    print("요청 실패했어요: {0}".format(e)) # API Key 오류, 네트워크 단절 등
    
    
    
    