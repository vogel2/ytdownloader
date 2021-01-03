from pytube import YouTube

link = input("Type video URL: ")

video = YouTube(link)

print(f"Title:\n{video.title} \n")
print(f"Description:\n{video.description} \n")
print(f"Views:\n{video.views} \n")
print(f"Rating:\n{video.rating} / 5.0 \n")
print(f"Length:\n{video.length/60} minutes \n")

for stream in video.streams.filter(progressive=True, file_extension='mp4'):
        print(stream)