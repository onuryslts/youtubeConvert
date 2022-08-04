from pytube import YouTube
link = input("Link: ")
directory = input("Directory: ")

try:
    yt = YouTube(link)
except:
    print("Invalid link!")
    exit()
    
mp4s = yt.streams.filter(file_extension="mp4")



for i, mp4 in enumerate(mp4s):
    print(i+1, mp4)

n = int(input("Choose: "))
print("Dowloading..")
mp4s[n-1].download(directory)
print("Download complete! ")