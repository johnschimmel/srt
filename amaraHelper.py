import os, json
import tortilla
import srt
from dotenv import load_dotenv


def jsonPrint(data):
	print json.dumps(data, sort_keys=True,indent=4, separators=(',', ': '))


load_dotenv('.env') # get envs

# amaraApiUrl = 'https://www.amara.org/api/'
amaraApiUrl = 'http://localhost:8000/api/'

api = tortilla.wrap(amaraApiUrl, suffix="/", debug=True)
api.config.headers['X-api-username'] = 'johntest'
api.config.headers['X-apikey'] = '9287f28dac7222531773940fc996e89ce35b8854' #os.environ.get('amaraToken')
api.config.headers['Accept'] = 'application/json'

videoId = 'gPZUcxWUf7rc'
languageCode = 'en'

# videoInfo = api.videos(videoId).get()
# subtitles = api.videos(videoId).languages(languageCode).subtitles.get()
# jsonPrint(subtitles)

def createVideo(videoInfo):
	# create video - is not working now
	# newVideoDict = {
	# 	'video_url':'https://vp.nyt.com/video/2016/12/08/70077_1_lastword-johnglenn_wg_480p.mp4',
	# 	'title':'john glenn test video',
	# 	'duration':'404',
	# 	'primary_audio_language_code':languageCode
	# }

	try:
		newVideoResp = api.videos.post(data=videoInfo)
		jsonPrint(newVideoResp)
		return newVideoResp, True

	except Exception as e:
		print e
		return e, False


