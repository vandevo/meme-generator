from PIL import Image, ImageDraw, ImageFont
import os

def create_labeled_image(name, width, height, bg_color, label):
    """Create a placeholder image with a label indicating what photo should go here"""
    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    # Add border
    draw.rectangle([0, 0, width-1, height-1], outline=(150, 150, 150), width=3)
    
    # Add label text
    try:
        # Try to use a larger font
        font = ImageFont.truetype("arial.ttf", 60)
    except:
        try:
            font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 60)
        except:
            font = ImageFont.load_default()
    
    # Calculate text position (centered)
    bbox = draw.textbbox((0, 0), label, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    
    # Draw text with shadow for visibility
    draw.text((x+2, y+2), label, fill=(50, 50, 50), font=font)
    draw.text((x, y), label, fill=(255, 255, 255), font=font)
    
    # Add subtitle
    subtitle = f"Replace with {name} photo"
    try:
        sub_font = ImageFont.truetype("arial.ttf", 30)
    except:
        try:
            sub_font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 30)
        except:
            sub_font = ImageFont.load_default()
    
    sub_bbox = draw.textbbox((0, 0), subtitle, font=sub_font)
    sub_width = sub_bbox[2] - sub_bbox[0]
    sub_x = (width - sub_width) // 2
    sub_y = y + text_height + 20
    
    draw.text((sub_x+1, sub_y+1), subtitle, fill=(50, 50, 50), font=sub_font)
    draw.text((sub_x, sub_y), subtitle, fill=(200, 200, 200), font=sub_font)
    
    img.save(f'{name}.jpg', 'JPEG', quality=90)
    print(f'Created {name}.jpg - {label}')

# Create labeled placeholder images
create_labeled_image('cat', 800, 600, (40, 40, 50), 'CAT')
create_labeled_image('dog', 800, 600, (50, 40, 40), 'DOG')
create_labeled_image('surprised', 800, 600, (50, 50, 40), 'SURPRISED')
create_labeled_image('thinking', 800, 600, (40, 50, 50), 'THINKING')
create_labeled_image('happy', 800, 600, (50, 50, 40), 'HAPPY')

print('\nAll labeled placeholder images created!')
print('You can now replace these with actual photos matching the labels.')
