import pyaudio
import wave
from playsound import playsound
import sys
from termcolor import colored


CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100

def record():

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print(colored("Start recording, press CTRL + C to stop", "green"))

    frames = []

    try:
        while True:
            data = stream.read(CHUNK)
            frames.append(data)
    except KeyboardInterrupt:
        print(colored("Done recording", "green"))
    except Exception as e:
        print(str(e))

    sample_width = p.get_sample_size(FORMAT)
    
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    return sample_width, frames 

def record_to_file(file_path):
    wf = wave.open(file_path, 'wb')
    wf.setnchannels(CHANNELS)
    sample_width, frames = record()
    wf.setsampwidth(sample_width)
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

if __name__ == '__main__':
    video_name = input(colored("Please enter a name for the file: ", "green"))
    record_to_file(f"{video_name}.wav")
    answer = input(colored("Do you want to play the audio now? Press y to play or other key to exit: ", "green"))
    if answer == "y":
        playsound(f"{video_name}.wav")
        print(colored(f"Result written to {video_name}.wav", "green"))
    else:
        print(colored(f"Result written to {video_name}.wav", "green"))
        sys.exit()
