''' videoCVffp.py 
    cv2 + ffpyPlayer 播放 Video + sound
    請先安裝 ffmpeg     
'''
import cv2
from ffpyplayer.player import MediaPlayer

filename = 'YourAnswer.mp4'

# cv 設定
video = cv2.VideoCapture(filename)
FPS = int(video.get(cv2.CAP_PROP_FPS))  # Frames per Sec
cv2.namedWindow('video',cv2.WINDOW_KEEPRATIO) 
cv2.resizeWindow('video', 500,300) 
cv2.moveWindow('video',300,200)

# 聲音 設定
player = MediaPlayer(filename)

# 開始播放
val = ''
while val != 'eof':
    
    # 聲音在此
    audio_frame, val = player.get_frame()
    
    if val != 'eof' and audio_frame is not None:
        img, t = audio_frame
        print(val, t, img.get_pixel_format(), img.get_buffer_size())
         
    # 影像在此
    ret, frame = video.read()
    
    # if 影片末尾
    if not ret:
        print("End of video")
        break
    
    # if 按Esc 中斷
    if cv2.waitKey(FPS) == 27:
        break
    
    cv2.imshow('video', frame)
  
#--- ending
video.release()
cv2.destroyAllWindows()
player.close_player()

