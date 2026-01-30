import urllib.request
import urllib.error
import json
import time

def download_with_headers(url, filename):
    """Download image with proper headers"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Referer': 'https://www.google.com/'
        }
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            with open(filename, 'wb') as f:
                f.write(response.read())
        print(f'[OK] Downloaded {filename}')
        return True
    except Exception as e:
        print(f'[FAIL] Failed {filename}: {e}')
        return False

# Try multiple sources for each keyword
photos_to_download = {
    'cat': [
        'https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=800&h=600&fit=crop',
        'https://images.unsplash.com/photo-1574158622682-e40e69881006?w=800&h=600&fit=crop',
        'https://picsum.photos/id/237/800/600',
    ],
    'dog': [
        'https://images.unsplash.com/photo-1552053831-71594a27632d?w=800&h=600&fit=crop',
        'https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=800&h=600&fit=crop',
        'https://picsum.photos/id/1025/800/600',
    ],
    'surprised': [
        'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=800&h=600&fit=crop',
        'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=800&h=600&fit=crop',
        'https://picsum.photos/id/64/800/600',
    ],
    'thinking': [
        'https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=800&h=600&fit=crop',
        'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=800&h=600&fit=crop',
        'https://picsum.photos/id/1011/800/600',
    ],
    'happy': [
        'https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?w=800&h=600&fit=crop',
        'https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=800&h=600&fit=crop',
        'https://picsum.photos/id/1005/800/600',
    ],
}

print('Downloading photos matching keywords...\n')

for keyword, urls in photos_to_download.items():
    filename = f'{keyword}.jpg'
    success = False
    
    for url in urls:
        if download_with_headers(url, filename):
            success = True
            time.sleep(1)  # Be polite with delays
            break
        time.sleep(0.5)
    
    if not success:
        print(f'[WARN] Could not download {filename} from any source')

print('\nDone! Note: Some images may still be random if services are unavailable.')
