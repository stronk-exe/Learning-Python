import pytube

print('***  download youtube videos using python    ***')
url = input('url: ')
path = 'Downloads'

pytube.YouTube(url).streams.get_highest_resolution().download(path)
print('done!')
