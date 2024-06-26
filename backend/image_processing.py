import cv2
import numpy as np
import json

def analyze_urine_strip(image_file):
    colors = {}
    belt = ['URO', 'BIL', 'KET', 'BLD', 'PRO', 'NIT', 'LEU', 'GLU', 'SG', 'PH']
    image = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_COLOR)
    width = image.shape[1] // 10
    for i in range(10):
        x = i * width
        roi = image[:, x:x+width]
        
        pixels = np.float32(roi.reshape(-1, 3))
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        flags = cv2.KMEANS_RANDOM_CENTERS
        _, _, centers = cv2.kmeans(pixels, 1, None, criteria, 10, flags)
        dominant_color = centers[0].astype(np.int32).tolist()
        
        colors[belt[i]] = dominant_color
    
    return json.dumps(colors)