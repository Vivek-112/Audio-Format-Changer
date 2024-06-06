import speech_recognition as sr
from pydub import AudioSegment

audio = AudioSegment.from_file(r"English.mp3")
audio.export("convert_audio.wav", format="wav")
print("Congratulations, your audio file is converted to wav format")
recognizer = sr.Recognizer()
audio_file = sr.AudioFile("convert_audio.wav")
with audio_file as source:
    audio = recognizer.record(source)
    try:
      text = recognizer.recognize_google(audio)
      print("Text: ", text)
    except sr.RequestError as e:
      print(f"Could not understand audio; {e}")
    except sr.UnknownValueError:
      print("Google speech recognition could not understand audio")
