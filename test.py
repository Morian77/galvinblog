import os
import re
import shutil

# Paths (using raw strings to handle Windows backslashes correctly)
posts_dir = r"F:\Documents\galvinblog\content\posts"
attachments_dir = r"F:\Documents\My_Second_Brain\attachments"
static_images_dir = r"F:\Documents\galvinblog\static\images"

# Step 1: Process each markdown file in the posts directory
for filename in os.listdir(posts_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(posts_dir, filename)
        
        print(f"\nProcessing file: {filename}")
        
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
        
        # Use the working pattern we found
        images = re.findall(r'!!\[.*?\]\(/images/(.*?\.png)\)', content)
        
        print(f"Found images: {images}")
        
        # Process each image
        for image in images:
            # Convert %20 back to spaces for the filesystem
            source_image_name = image.replace('%20', ' ')
            image_source = os.path.join(attachments_dir, source_image_name)
            
            print(f"Looking for image at: {image_source}")
            
            if os.path.exists(image_source):
                try:
                    shutil.copy(image_source, static_images_dir)
                    print(f"Successfully copied: {source_image_name}")
                except Exception as e:
                    print(f"Error copying {source_image_name}: {e}")
            else:
                print(f"Image not found at: {image_source}")

print("Processing completed.")