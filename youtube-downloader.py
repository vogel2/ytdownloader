from pytube import YouTube

link = input("Type video URL: ")

video = YouTube(link)

print(f"Title:\n{video.title} \n")
print(f"Description:\n{video.description} \n")
print(f"Views:\n{video.views} \n")
print(f"Rating:\n{video.rating} / 5.0 \n")
print(f"Length:\n{video.length} / 60 minute(s) \n")

for stream in video.streams.filter(progressive=True, file_extension='mp4'):
        print(stream)

quality = str("")
print(f"Select Quality: HD / SD")
input(quality)

downloadLocation = str("")
print(f"Input your download location")

video.streams.get_highest_resolution().download(output_path="/d/Projects/ytdownloader", filename="video")
input(downloadLocation)

def show_progress_bar(stream, chunk, file_handle, bytes_remaining):
         return  # do work

if quality == "HD":
    
elif quality == "SD":
    video.streams.get_lowest_resolution().download(output_path=downloadLocation)

def finish():
    print("Download Complete!")

video.register_on_progress_callback(show_progress_bar)

video.register_on_complete_callback(finish())
