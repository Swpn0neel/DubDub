import speech_recognition as sr
from pydub import AudioSegment

def mp3_to_wav(input_file, output_file):
    try:
        audio = AudioSegment.from_mp3(input_file)
        audio.export(output_file, format="wav")
        print(f"Conversion successful: {input_file} -> {output_file}")
    except Exception as e:
        print(f"Conversion failed: {e}")

def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()

    audio = AudioSegment.from_mp3(audio_file)

    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
        try:
            transcript = recognizer.recognize_sphinx(audio)
            return transcript
        except sr.UnknownValueError:
            return "Speech recognition could not understand audio"
        except sr.RequestError as e:
            return f"Could not request results; {e}"

if __name__ == "__main__":
    audio_file = "./downloads/output_audio.mp3"
    input_audio_file = "./downloads/output_audio.wav"

    mp3_to_wav(audio_file , input_audio_file)

    transcript = transcribe_audio(input_audio_file)

    output_file_path = "transcript.txt"
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        output_file.write(transcript)
        
    print("Transcript:")
    print(transcript)