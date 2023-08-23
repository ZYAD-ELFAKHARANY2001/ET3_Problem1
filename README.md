# ET3_Problem1

**Professional Documentation:**

**Project Overview:**
This Python script is designed to perform the following tasks:
1. Extract image files with specific extensions (.jpg, .jpeg, .png) from a source folder and its subfolders.
2. Copy the extracted images to a destination folder.
3. Generate a CSV report file containing information about each image's name, size in megabytes, and last modification date.

**Solution Components:**
The solution consists of several functions:

1. `extract_images(source_folder, destination_folder)`: This function recursively walks through the source folder and its subfolders, identifies image files with specified extensions, and copies them to the destination folder.

2. `discard_prefix(image_name)`: This function is used to clean up image names by removing a specified prefix (if present).

3. `convert_to_megabytes(size_in_bytes)`: This function converts image sizes from bytes to megabytes for better readability in the report.

4. `generate_report(images_folder, report_file)`: This function generates a CSV report file that includes the image name, size in megabytes, and last modification date for each image in the specified images folder.

**Instructions to Run the Solution:**
Follow these steps to run the solution:

1. Ensure that you have Python installed on your system.

2. Create a source folder (`source_folder`) containing the dataset of images you want to process. Make sure the images have the extensions .jpg, .jpeg, or .png.

3. Create a destination folder (`destination_folder`) where the extracted images will be copied.

4. Set the `report_file` variable to specify the path and name of the CSV report file where the image information will be saved.

5. Run the Python script containing the provided code.

Here's an example of how you can run the solution with your provided paths:

```python
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
```

After running the script, you will find the extracted images in the specified destination folder, and a CSV report file will be generated with information about each image in the specified report file path.

This solution provides an efficient way to organize and analyze image data from a source folder and create a report for further analysis or documentation.
