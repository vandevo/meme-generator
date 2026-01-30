from PIL import Image, ImageDraw, ImageFont
import os

# Create simple placeholder images for memes
def create_placeholder(name, width, height, bg_color, text=""):
    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    # Add a simple border
    draw.rectangle([0, 0, width-1, height-1], outline=(200, 200, 200), width=2)
    
    # Add text if provided
    if text:
        try:
            font = ImageFont.truetype("arial.ttf", 40)
        except:
            font = ImageFont.load_default()
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        position = ((width - text_width) // 2, (height - text_height) // 2)
        draw.text(position, text, fill=(100, 100, 100), font=font)
    
    img.save(f'{name}.jpg', 'JPEG', quality=85)
    print(f'Created {name}.jpg')

# Create meme-worthy placeholder images
create_placeholder('cat', 800, 600, (240, 240, 240), 'Cat Meme')
create_placeholder('dog', 800, 600, (230, 240, 250), 'Dog Meme')
create_placeholder('surprised', 800, 600, (250, 240, 230), 'Surprised')
create_placeholder('thinking', 800, 600, (240, 250, 240), 'Thinking')
create_placeholder('happy', 800, 600, (255, 250, 230), 'Happy')

print('\nAll placeholder images created!')
