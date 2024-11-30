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
        
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
        
        # Step 2: Find all image links in the format ![Image Description](/images/Pasted%20image%20...%20.png)
        images = re.findall(r'!!\[.*?\]\(/images/(.*?\.png)\)', content)
        
        # Step 3: Replace image links and ensure URLs are correctly formatted
        for image in images:
            # Prepare the Markdown-compatible link with %20 replacing spaces
            source_image_name = image.replace('%20', ' ')
            image_source = os.path.join(attachments_dir, source_image_name)
            
            # Step 4: Copy the image to the Hugo static/images directory if it exists
            if os.path.exists(image_source):
                shutil.copy(image_source, static_images_dir)

print("Markdown files processed and images copied successfully.")
