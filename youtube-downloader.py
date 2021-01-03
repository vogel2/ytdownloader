from pytube import YouTube

link = input("Type video URL: ")

video = YouTube(link)

print(f"Title:\n{video.title}")
print(f"Description:\n{video.description}")
print(f"Views:\n{video.views}")
print(f"Rating:\n{video.rating}")
print(f"Length:\n{video.length}")

