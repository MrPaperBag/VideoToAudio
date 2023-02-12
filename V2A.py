import sys
from moviepy.video.io.VideoFileClip import VideoFileClip

def convert_video_to_audio(video_file, audio_file):
	clip = VideoFileClip(video_file)
	clip.audio.write_audiofile(audio_file, )


arguments = sys.argv[1:]
audio = ""
default_format = "mp3"
if arguments[:]:
	video = arguments[0]
	if len(arguments)>1:
		audio = arguments[1]
else:
	video = input("Enter video: ")

if not audio:
	audio = "".join(video.split(".")[:-1:]) + "." + default_format
convert_video_to_audio(video, audio)
print(f"Converted {audio}")
