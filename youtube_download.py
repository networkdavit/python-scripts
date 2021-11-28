from pytube import YouTube

link = input("Please specify the link: ")
video_name = input("Please name the video: ")

YouTube(link).streams.get_highest_resolution().download(filename=f"{video_name}.mp4")

