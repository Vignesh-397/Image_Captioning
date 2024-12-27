import os
import pandas as pd

# Step 1: Define the folder path and Google Sheet path
folder_path = "Images"  # Replace with your Drive folder path
sheet_path = "Image Captioning Data.xlsx"  # Replace with your captions sheet path

# Step 2: Load captions from the Google Sheet
captions_df = pd.read_excel(sheet_path)  # Ensure the sheet has columns: 'Name', 'Caption-1', 'Caption-2', 'Caption-3'

# Step 3: Map captions to image IDs
captions_map = {}
for _, row in captions_df.iterrows():
    img_id = str(row['Name']).zfill(3)  # Format the Image ID as three digits
    captions = [row['Caption-1'], row['Caption-2'], row['Caption-3']]  # Captions columns
    captions_map[img_id] = captions

# Step 4: Generate the output file
output_file = "output.txt"
with open(output_file, "w") as file:
    for image_name in os.listdir(folder_path):
        if image_name.endswith(('.png', '.jpg', '.jpeg')):
            img_id = os.path.splitext(image_name)[0]  # Get the image ID (filename without extension)
            img_id = img_id.zfill(3)  # Ensure the ID matches the three-digit format
            if img_id in captions_map:
                for caption in captions_map[img_id]:
                    file.write(f"{img_id},{caption}\n")

print(f"Output file '{output_file}' has been created successfully!")
