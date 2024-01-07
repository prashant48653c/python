from pytube import YouTube
import pandas as pd

def progress_func(vid_id):
    print(f"Progressing with {vid_id} ...")
    
     

def complete_func(vid_id):
    print(f"The video of id {vid_id} was retrieved from Pytube")
  
# to download the video at maixmum resolution
isLoading=False
def download_video(vid_id,download_path):
    print("Download video function is running")
    try:
        selectedVideo=YouTube(f"https://www.youtube.com/watch?v={vid_id}",
                               on_complete_callback=complete_func(vid_id),
                               )
        
        maxResVid = selectedVideo.streams.get_highest_resolution()
        if  maxResVid:
             maxResVid.download(download_path)
           
        else:   # if the higher resolution video is not available then we will download video with lower resolution
             lowResVid=selectedVideo.streams.get_lowest_resolution()
             lowResVid.download(download_path)
           

    except Exception as downloadError:
        print("Error at download_video function while downloading the video ", downloadError)





def getVidLinkAndDownload(csv_path):
    download_path="download_folder"

    print("Get vidlink from csv function is running")
    df=pd.read_csv(csv_path)
    vidIds=df['URL'].to_list()
    print("Video list", vidIds)
    i=1
   
    for id in vidIds:
        isLoading=True
        download_video(id,download_path)
        isLoading=False
        if isLoading == False:
        
           print(f"The '{i}' no. video was downloaded")
           i+=1

 
 
csv_path="csv_folder/vid_data.csv"
getVidLinkAndDownload(csv_path)
 


