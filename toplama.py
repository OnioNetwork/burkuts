import urllib.request
import gzip
...
# Read the first 64 bytes of the file inside the .gz archive located at `url`
url = 'https://github.com/Burkuts-Translate/webkiller'
with urllib.request.urlopen(url) as response:
    with gzip.GzipFile(fileobj=response) as uncompressed:
        file_header = uncompressed.read(64) # a `bytes` object
        # Or do anything shown above using `uncompressed` instead of `response`.