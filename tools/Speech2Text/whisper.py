from pydub import AudioSegment
import whisper
import ffmpeg

def convert_opus_to_mp3(opus_file, mp3_file):
    opus_file_path = opus_file
    mp3_file_path = mp3_file
    
    audio = AudioSegment.from_file(opus_file_path)
    audio.export(mp3_file_path, format="mp3")
    
    return mp3_file_path
       
def find_in_audio(key, audio_path):
    
    listener = whisper.load_model("small")

    result = listener.transcribe(convert_opus_to_mp3(audio_path))
    
    if(key.lower() in result['text'].lower()):
        return True
    return False

def get_text(audio_path):
    listener = whisper.load_model("small")

    result = listener.transcribe(convert_opus_to_mp3(audio_path))
    
    return result['text']
