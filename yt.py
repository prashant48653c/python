from pytube import YouTube
import pandas as pd

# to download the video at maixmum resolution
def download_video(vid_id,download_path):
    print("Download video function is running")
    try:
        selectedVideo=YouTube(f"https://www.youtube.com/watch?v={vid_id}")
        print(selectedVideo.title)
        maxResVid = selectedVideo.streams.get_highest_resolution()
        maxResVid.download(download_path)

    except Exception as downloadError:
        print("Error at download_video function while downloading the video ", downloadError)





def getVidLinkAndDownload(csv_path):
    download_path="download_folder"

    print("Get vidlink from csv function is running")
    df=pd.read_csv(csv_path)
    videoLinks=df['URL'].to_list()
    print("Video list", videoLinks)
    i=1
    isLoading=False
    for id in videoLinks:
        isLoading=True
        download_video(id,download_path)
        isLoading=False
        if isLoading == False:
        
           print(f"The '{i}' no. video was downloaded")
           i+=1

 
 
csv_path="csv_folder/vid_data.csv"
getVidLinkAndDownload(csv_path)
 


