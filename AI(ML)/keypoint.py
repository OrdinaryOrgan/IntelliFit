# 该代码用于检测关键点并计算关键点，生成csv文件

import cv2
import cv2
import mediapipe as mp
import os
import csv

save_folder = './LandmarkImage/act1/pos/' 
csv_path = './keypoints.csv'
header = ['Name'] + ['Point' + str(i) + '_' + axis for i in range(1, 15) for axis in ['x', 'y', 'z']]

# 如果文件夹不存在则创建
if not os.path.exists(save_folder):
  os.makedirs(save_folder)

if not os.path.exists(csv_path):
  with open(csv_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

def draw_landmarks(img, results):
    mp_draw = mp.solutions.drawing_utils
    mp_draw.draw_landmarks(img, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
    return img

folder = './RawImage/act1/pos/'

for img_name in os.listdir(folder):
    # 读取图像
    img_path = os.path.join(folder, img_name)
    img = cv2.imread(img_path)
    
    # 检测关键点  
    results = pose.process(img)

    if not results.pose_landmarks:
        continue

    # 绘制关键点
    img = draw_landmarks(img, results)
    
    # 构造保存文件的路径和名称
    save_path = os.path.join(save_folder, 'landmark_' + img_name)
    
    # 保存图片到新的文件夹
    cv2.imwrite(save_path, img)
    
    # 获取头部相关关键点索引
    head_points = [0, 14, 15, 16, 17] 

    # 求头部关键点的平均坐标
    x = sum(results.pose_landmarks.landmark[i].x for i in head_points) / len(head_points)
    y = sum(results.pose_landmarks.landmark[i].y for i in head_points) / len(head_points)
    z = sum(results.pose_landmarks.landmark[i].z for i in head_points) / len(head_points)

    # 将平均坐标作为Point1写入
    row = [img_name, x, y, z]

    for i in range(1, 14):
        x = results.pose_landmarks.landmark[i].x
        y = results.pose_landmarks.landmark[i].y
        z = results.pose_landmarks.landmark[i].z
        row.append(x)
        row.append(y)
        row.append(z)

    with open('keypoints_act1_pos.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(row)