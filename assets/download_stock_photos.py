import urllib.request
import urllib.parse

# Use placeholder.com service to get actual stock photos
# These are free stock photos from various sources

def download_image(url, filename):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        req = urllib.request.Request(url, headers=headers)
        urllib.request.urlretrieve(url, filename)
        print(f'Downloaded {filename}')
        return True
    except Exception as e:
        print(f'Failed to download {filename}: {e}')
        return False

# Using placeholder.com which provides actual images
# These URLs point to free stock photos
base_urls = [
    ('https://picsum.photos/800/600?random=1', 'cat.jpg'),
    ('https://picsum.photos/800/600?random=2', 'dog.jpg'),
    ('https://picsum.photos/800/600?random=3', 'surprised.jpg'),
    ('https://picsum.photos/800/600?random=4', 'thinking.jpg'),
    ('https://picsum.photos/800/600?random=5', 'happy.jpg'),
]

print('Downloading stock photos...')
for url, filename in base_urls:
    download_image(url, filename)

print('\nDone!')
