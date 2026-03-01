from os.path import basename, exists

def download(url, dest=None):
    filename = dest if dest is not None else basename(url)
    if not exists(filename):
        from urllib.request import urlretrieve

        local, _ = urlretrieve(url, filename)
        print("Downloaded " + str(local))
    return filename