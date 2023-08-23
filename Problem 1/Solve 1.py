import os
import shutil
import csv
import time

def extract_images(source_folder, destination_folder):
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.endswith(('.jpg', '.jpeg', '.png')):
                source_path = os.path.join(root, file)
                destination_path = os.path.join(destination_folder, file)
                shutil.copyfile(source_path, destination_path)

def discard_prefix(image_name):
    return image_name.split('-', 1)[-1]

def convert_to_megabytes(size_in_bytes):
    size_in_mb =  size_in_bytes / (1024 * 1024)
    return f"{size_in_mb:.2f} MB"

def generate_report(images_folder, report_file):

    report_dir = os.path.dirname(report_file)
    os.makedirs(report_dir, exist_ok=True)


    with open(report_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Image Name', 'Image Size', 'Last Modification Date'])
        
        for root, dirs, files in os.walk(images_folder):
            for file in files:
                file_path = os.path.join(root, file)
                image_name = discard_prefix(file)
                image_stat = os.stat(file_path)
                image_size = convert_to_megabytes(image_stat.st_size)
                last_modified = time.ctime(image_stat.st_mtime)
                writer.writerow([image_name, image_size, last_modified])

# Set the source folder containing the dataset of images
source_folder = 'problem1\\problem1\\dairies\\dairies'

# Set the destination folder where the images will be copied
destination_folder = 'problem1\\problem1\\images dataset for ex'

# Set the path for the CSV report file
report_file = 'Solve 1/Report file.csv'

# Extract images from the source folder and copy them to the destination folder
extract_images(source_folder, destination_folder)

# Generate the CSV report
generate_report(destination_folder, report_file)