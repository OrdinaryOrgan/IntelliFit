import cv2
import mediapipe as mp
import csv
import datetime
import joblib
import numpy as np

class point:

    def __init__(self, x, y, z, name):
       self.x = x
       self.y = y
       self.z = z
       self.name = name

    def Print(self):
        print('name: ', self.name, ' x:', self.x, ' y:', self.y, ' z:', self.z)


class ImageProcesser:

    def __init__(self, height=170):
        self.csv_path = 'data.csv'
        self.factor = height/220

        self.name_list = ['Point1', 'Point2', 'Point3', 'Point4', 'Point5', 'Point6', 'Point7', 'Point8', 'Point9','Point10','Point11','Point12','Point13','Point14']
        with open(self.csv_path, 'w', encoding='UTF8', newline='') as f:
            header = ['Time']
            for i in self.name_list:
                for j in ['x', 'y', 'z']:
                    header.append(i+'.'+j)
            writer = csv.writer(f)
            writer.writerow(header)

        self.model = joblib.load('model/test23n_svm.joblib')
        self.scaler = joblib.load('model/test23n_scaler.joblib')

    def save(self, coord):
        with open(self.csv_path, 'a+', encoding='UTF8', newline='') as f:
            coords = [datetime.datetime.now()]
            for i in coord:
                coords.extend([i.x, i.y, i.z])
            writer = csv.writer(f)
            writer.writerow(coords)

    def predict(self, coord):
        x = []
        for i in coord:
            x.append(i.x)
            x.append(i.y)
            x.append(i.z)
        x = np.array(x).reshape(1, -1)
        x = self.factor*x
        x = self.scaler.transform(x)
        y = self.model.predict(x)
        return y[0]


    def judge(self, result):
        idx = -1

        # head
        idx += 1
        head_coord = point(0, 0, 0, self.name_list[idx])
        head_points = [0, 14, 15, 16, 17] 

        # 求头部关键点的平均坐标
        head_coord.x = sum(result.pose_landmarks.landmark[i].x for i in head_points) / len(head_points)
        head_coord.y = sum(result.pose_landmarks.landmark[i].y for i in head_points) / len(head_points)
        head_coord.z = sum(result.pose_landmarks.landmark[i].z for i in head_points) / len(head_points)

        # body
        body_coord = []
        for i in range(1, 14):
            temp_coord = point(0, 0, 0, self.name_list[idx])
            idx += 1
            if result.pose_world_landmarks.landmark[i] is None:
                body_coord.append(temp_coord)
            temp_coord.x = result.pose_world_landmarks.landmark[i].x
            temp_coord.y = result.pose_world_landmarks.landmark[i].y
            temp_coord.z = result.pose_world_landmarks.landmark[i].z
            body_coord.append(temp_coord)
            
        # total
        coord = []
        coord.append(head_coord)
        coord.extend(body_coord)
        self.save(coord)
        return self.predict(coord)

    # 调用入口
    def ImageProcess(self, img):
        mp_pose = mp.solutions.pose # 模型定义
        with mp_pose.Pose(
            static_image_mode=True,
            model_complexity=1,
            enable_segmentation=True,
            min_detection_confidence=0.5) as pose:
            results = pose.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            if results.pose_world_landmarks is None:
                return 0
        pose = self.judge(results)
        return pose
