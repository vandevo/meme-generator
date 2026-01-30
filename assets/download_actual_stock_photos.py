import urllib.request
import json

# Using Unsplash Source API (no key required for basic usage)
# These are direct links to actual stock photos matching the descriptions

def download_image(url, filename):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            with open(filename, 'wb') as f:
                f.write(response.read())
        print(f'Downloaded {filename}')
        return True
    except Exception as e:
        print(f'Failed to download {filename}: {e}')
        return False

# Using Unsplash Source - free stock photos that match descriptions
# Format: https://source.unsplash.com/800x600/?keyword
photos = [
    ('https://source.unsplash.com/800x600/?cat', 'cat.jpg'),
    ('https://source.unsplash.com/800x600/?dog', 'dog.jpg'),
    ('https://source.unsplash.com/800x600/?surprised,expression', 'surprised.jpg'),
    ('https://source.unsplash.com/800x600/?thinking,person', 'thinking.jpg'),
    ('https://source.unsplash.com/800x600/?happy,smile', 'happy.jpg'),
]

print('Downloading actual stock photos matching descriptions...')
for url, filename in photos:
    download_image(url, filename)

print('\nDone! Note: Unsplash Source may sometimes return random images.')
