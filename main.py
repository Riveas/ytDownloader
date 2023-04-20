from pytube import YouTube

def resolution(choice):

    if choice in ['360', '360p', 'low']:
        res =  '360p'
    elif choice in ['480', '480p', 'mid', 'medium']:
        res =  '480p'
    elif choice in ['720', '720p', 'high', 'hd']:
        res =  '720p'
    elif choice in ['1080', '1080p', 'very high', 'very_high', 'full hd', 'full_hd']:
        res = '1080p'

    return res



if __name__ == '__main__':

    dir = input("Enter direction you'd like to save your video\n")

    link = input("Enter link to video you`d like to download\n")

    chosenResolution = resolution(input('Choose quality\n'))

    vid = YouTube(link)

    vid.streams.get_by_resolution(chosenResolution).download(dir)

