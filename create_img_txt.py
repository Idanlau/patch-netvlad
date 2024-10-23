import os

def save_image_paths_to_file(image_folder, output_file):
    # Define valid image extensions
    valid_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']

    # Open the output file in write mode
    with open(output_file, 'w') as file:
        # Loop through all files in the specified folder
        for root, _, files in os.walk(image_folder):
            for filename in files:
                # Check if the file has a valid image extension
                if os.path.splitext(filename)[1].lower() in valid_extensions:
                    # Get the absolute path of the image
                    abs_path = os.path.join(root, filename)
                    # Write the absolute path to the output file
                    file.write(abs_path + '\n')


# Specify the folder containing images and the output file path
split_type = "train"
image_datetime = "2014-12-16-09-14-09"

image_folder = f'/Users/idanlau/Desktop/robot_car_dataset_setup/oxford_{split_type}_images/{image_datetime}/stereo/left'
output_file = f'/Users/idanlau/Desktop/robot_car_dataset_setup/imagename_text_files/{image_datetime}.txt'

# Call the function to save image paths
save_image_paths_to_file(image_folder, output_file)

print(f"Image paths saved to {output_file}")
