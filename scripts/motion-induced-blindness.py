import numpy as np
import cv2

img = np.zeros((240,320,3))

def get_square(size: int, thickness: int=3):
	square = np.zeros((size,size,3), 'uint8')
	cv2.line(square,(0,size//2),(size,size//2),(255,0,0),thickness)
	cv2.line(square,(size//2,0),(size//2,size),(255,0,0),thickness)
	return square

def pad(img: np.ndarray, n: int, value:int = 0):
	return np.pad(img, ((n,),(n,),(0,)), constant_values=value)

def rotate(img: np.ndarray, degrees: float):
	rot_mat = cv2.getRotationMatrix2D(tuple(n//2 for n in img.shape[:2]), degrees, 1.0)
	return cv2.warpAffine(img, rot_mat, img.shape[:2])

def put_dots(img: np.ndarray, size: int, colour: tuple = (0,255,255)):
	cv2.circle(img, (int(img.shape[1]*0.50),int(img.shape[0]*0.70)), size, colour, -1)
	cv2.circle(img, (int(img.shape[1]*0.36),int(img.shape[0]*0.40)), size, colour, -1)
	cv2.circle(img, (int(img.shape[1]*0.64),int(img.shape[0]*0.40)), size, colour, -1)
	return img

def overlay_images(img1: np.ndarray, img2: np.ndarray):
	mask = 	((img2[:,:,0] != 0) + (img2[:,:,1] != 0) + (img2[:,:,2] != 0)) != 0
	img1[:,:,0][mask] = img2[:,:,0][mask]
	img1[:,:,1][mask] = img2[:,:,1][mask]
	img1[:,:,2][mask] = img2[:,:,2][mask]
	return img1

def hsv_to_bgr(h: float, s: float, v: float):
	"""
	h (degrees), s (0->1), v (0->1) to bgr (0->255)
	from https://www.codespeedy.com/hsv-to-rgb-in-cpp/
	"""
	h = h % 360
	c = s*v
	x = c*(1-abs(((h/60) % 2)-1))
	m = v - c

	if h >= 0 and h < 60:
		r, g, b = c, x, 0
	elif h < 120:
		r, g, b = x, c, 0
	elif h < 180:
		r, g, b = 0, c, x
	elif h < 240:
		r, g, b, = 0, x, c
	elif h < 300:
		r, g, b = x, 0, c
	else:
		r, g, b = c, 0, x

	return int((b+m)*255), int((g+m)*255), int((r+m)*255)


background = pad(np.tile(pad(get_square(40,2), 7), (7,7,1)), 100)

rotation_range = range(0,5*360,2) # rotate 5 times
hue_range = (x/max(rotation_range)*360 for x in rotation_range) # cycle through hues once

video_writer = cv2.VideoWriter('assets/videos/motion-induced-blindness.mp4',cv2.VideoWriter_fourcc(*'avc1'), 30, (background.shape[1],background.shape[0]))

show_video = False

for rotation, dot_hue in zip(rotation_range, hue_range):
	bg = rotate(background, rotation)
	frame = put_dots(bg, 5, hsv_to_bgr(dot_hue,1,1))
	video_writer.write(frame)
	if show_video:
		cv2.imshow('img', frame)
		cv2.waitKey(20)

video_writer.release()