import re

def safe_filename(text, max_length=200):
    """
    Sanitizes filenames for many operating systems.

    Keyword arguments:
    text -- The unsanitized pending filename.
    """
    #Quickly truncates long filenames.
    truncate = lambda text: text[:max_length].rsplit(' ', 0)[0]

    #Tidy up ugly formatted filenames.
    text = text.replace('_', ' ')
    text = text.replace(':', ' -')

    #NTFS forbids filenames containing characters in range 0-31 (0x00-0x1F)
    ntfs = [chr(i) for i in range(0, 31)]

    #Removing these SHOULD make most filename safe for a wide range
    #of operating systems.
    paranoid = ['\"', '\#', '\$', '\%', '\'', '\*', '\,', '\.', '\/', '\:',
                '\;', '\<', '\>', '\?', '\\', '\^', '\|', '\~', '\\\\']

    blacklist = re.compile('|'.join(ntfs + paranoid), re.UNICODE)
    filename = blacklist.sub('', text)
    return truncate(filename)

def print_download_progress(progress, file_size):
    """
    > video.download(TMP_FOLDER, on_progress=Utilities.print_download_progress)
    """
    percent = progress * 100. / file_size
    status = r"%10d  [%3.2f%%]" % (progress, percent)
    status = status + chr(8) * (len(status) + 1)
    print status
