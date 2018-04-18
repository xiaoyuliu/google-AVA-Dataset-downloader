import os
import csv
import pdb
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

videoFolder = 'video_data'
videoNames = os.listdir(videoFolder)

trainFile = 'ava_train_v1.0.csv'
testFile = 'ava_test_v1.0.csv'
prename = ''

def cut_clips(data):
	for line in data:
		videoName = line[0]
		if videoName+'.mp4' not in videoNames:
			continue
		actionId = int(line[-1].strip())
		# I only want fall-down action
		if actionId != 5:
			continue

		if videoName != prename:
			count = 0
		else:
			count += 1

		middleTimeStamp = int(line[1])
		startTime = middleTimeStamp - 2.0
		endTime = middleTimeStamp + 1.5

		targetVideo = os.path.join(videoFolder, videoName+'-'+str(count)+'-cut.mp4')

		ffmpeg_extract_subclip(os.path.join(videoFolder, videoName+'.mp4'), startTime, endTime, targetname=targetVideo)

if __name__ == '__main__':
	with open(trainFile, 'r') as csvFile:
		data = csv.reader(csvFile, delimiter=',')
		cut_clips(data)
		
	with open(testFile, 'r') as csvFile:
		data = csv.reader(csvFile, delimiter='\t')
		cut_clips(data)


