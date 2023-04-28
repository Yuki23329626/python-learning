import yt_dlp
import logging

ydl_opts = {
    'skip_download': False,
    'writesubtitles': True
}

while True:
    str_link = input('URL:')
    link = [str_link]
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(link)
    except Exception as e:
        logging.error(e)


