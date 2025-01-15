import cv2
import numpy as np
import tqdm

input_video = cv2.VideoCapture('input.mp4')

width = int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = input_video.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_video = cv2.VideoWriter('output.avi', fourcc, 120, (width, height))

bar = tqdm.tqdm(total=int(input_video.get(cv2.CAP_PROP_FRAME_COUNT)), unit='frames')
while input_video.isOpened():
    ret, frame = input_video.read()
    if not ret:
        break
    
    output_video.write(np.zeros((height, width, 3), dtype=np.uint8))
    output_video.write(frame)
    bar.update(1)


input_video.release()
output_video.release()