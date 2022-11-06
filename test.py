import googletrans
from googletrans import Translator

print(googletrans.LANGUAGES)

text1 = "조성원 개바보"

translator = Translator()

print(translator.detect(text1))
trans1 = translator.translate(text1, src="ko", dest="en")
print("English to Japanese: ", trans1.text)

from gtts import gTTS
tts = gTTS(trans1.text, lang="zh-cn")
tts.save('media/hello.mp3')
