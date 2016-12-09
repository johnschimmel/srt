import srt

# open sample srt
file = open('sample.srt', 'r')

# parse subtitles
subtitle_generator = srt.parse(file.read())
subtitles = list(subtitle_generator)

print subtitles


print(srt.compose(subtitles))


