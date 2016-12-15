import os, json, subprocess
from dotenv import load_dotenv

load_dotenv('.env') # get envs

# command 
# autosub -K  -C 2 -o ~/Desktop/sample.srt -F srt -S en ~/Desktop/sample.mp4
# os.environ.get('amaraToken')

class Client:
	def __init__(self):
		print "inside autosubnyt "

	def run(self, srcVideo, destSrtFile):
		cmd = 'autosub -K {googleToken} -C 2 -o {srtFile} -F srt -S en {source}'.format(googleToken=os.environ.get('googleToken'),
																						srtFile=destSrtFile,
																						source=srcVideo)
		result = subprocess.check_output(cmd.split(' '),stderr=subprocess.STDOUT)
		print result
		return result