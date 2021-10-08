import pytube

def formats():
    print("""
	Video/Audio
	itag 	Code     Container  	Resolution
	 17	3gp	audio/video 	  144p
	 18	mp4	audio/video 	  360p
	 22	mp4	audio/video	  720p
	 133*	mp4	video 	 	  240p
	 134*	mp4	video 		  360p
	 135*	mp4	video 		  480p
	 136*	mp4	video 		  720p
	 137*	mp4	video 		  1080p
	 138*	mp4	video 		  2160p60

	Only audio
	itag 	Code     Container  	Resolution
	 139	m4a	audio only	  48Kbps
	 140	m4a	audio only	  128Kbps
	 249	webm	audio only	  50Kbps
	 250	webm	audio only	  70Kbps
	 251	webm	audio only	  160Kbps

	 *Note: Some of it may not work!!
	 *Note: Also some of it contains only video but not audio!!
    """)

def mainpart():
	video_url = input("\nEnter YouTube Video link: ")
	youtube = pytube.YouTube(video_url)
	formats()
	choose = input("Enter itag of video to download(see above list): ")
	video = youtube.streams.get_by_itag(choose)
	video.download()

try:
	mainpart()

except Exception as e:
	print("\033c")
	print(f"Try again!! : {e}")
	mainpart()
