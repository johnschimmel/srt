import subprocess
import urllib
import autosubNYT
import amaraHelper

def downloadVideo(url, target):
	try:
		test=urllib.FancyURLopener()
		test.retrieve(url,target)
		return target
	except ValueError:
		print "unable to download video", ValueError
		return False


def getDuration(videoFile):
	"""Returns duration in seconds (integer) for a given video file."""
	# found solution here -> http://stackoverflow.com/a/24488789
	cmd = 'ffprobe -v quiet -print_format compact=print_section=0:nokey=1:escape=csv -show_entries format=duration ' + videoFile
	result = subprocess.check_output(cmd.split(' '),stderr=subprocess.STDOUT)
	try:
		converted = int(float(result))
		return converted
	except ValueError:
		print "result is not a float"
		return False
	

# download video url
videoUrl = "https://vp.nyt.com/video/2016/12/08/70077_1_lastword-johnglenn_wg_480p.mp4"

# localVideo = downloadVideo(videoUrl, "/Users/205377/Documents/projects/srt/sample_dl.mp4")
localVideo = "/Users/205377/Documents/projects/srt/sample_dl.mp4"
if localVideo:
	# get duration
	duration = getDuration(localVideo)
	print "duration", duration

	# run autosub
	subber = autosubNYT.Client()
	srtResults = subber.run(localVideo, 'test.srt')
	print srtResults

	if duration and srtResults:
		print 'create video on amara'
		createResult = amaraHelper.createVideo({
			'video_url':videoUrl,
			'title':'john glenn test video',
			'duration': str(duration),
			'primary_audio_language_code':'en'
		})

		print createResult