import cv2
import time

cap = cv2.VideoCapture(0)
cnt = 0  

while True:
    ret, frame = cap.read()
    if ret:
        filename = './RawImage/frame_{}.jpg'.format(cnt)
        cv2.imwrite(filename, frame)
        cnt += 1
        
    if cv2.waitKey(15) & 0xFF == ord('q'):
        break
        
cap.release()


# # 抽帧逻辑
# video_path = 'video.mp4'
# cap = cv2.VideoCapture(video_path) 

# cnt = 0
# while cap.isOpened():
#     ret, frame = cap.read()
    
#     if ret:
#        # 保存抽取的帧
#         cv2.imwrite('./RawImage/frame_' + str(cnt) + '.jpg', frame)
#         cnt += 1
        
#     else:
#         break
        
# cap.release()