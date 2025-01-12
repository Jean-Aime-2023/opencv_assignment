import cv2
import matplotlib.pyplot as plt

# Load the image
image_path = 'assignment-001-given.jpg'
image = cv2.imread(image_path)

# Verify if the image is loaded successfully
if image is None:
    raise FileNotFoundError(f"Error: Unable to find the image at '{image_path}'.")

# Create a copy of the original image for drawing
output_image = image.copy()

# Draw a green rectangle
start_point = (265, 190)
end_point = (985, 925)
rectangle_color = (0, 255, 0)  # Green
rectangle_thickness = 8
cv2.rectangle(output_image, start_point, end_point, rectangle_color, rectangle_thickness)

# Add a semi-transparent black rectangle
overlay = output_image.copy()
cv2.rectangle(overlay, (795, 80), (1235, 175), (0, 0, 0), -1)  # Filled black rectangle
alpha = 0.5  # Transparency factor
cv2.addWeighted(overlay, alpha, output_image, 1 - alpha, 0, output_image)

# Add text to the image
text = 'RAH972U'
text_position = (800, 160)
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 3
text_color = (0, 255, 0)  # Green
text_thickness = 7
cv2.putText(output_image, text, text_position, font, font_scale, text_color, text_thickness)

# Save the resulting image
result_path = 'results.jpg'
cv2.imwrite(result_path, output_image)

# Convert the image to RGB for displaying with matplotlib
image_rgb = cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB)

# Display the image
plt.imshow(image_rgb)
plt.axis('off')  # Hide the axes for better visualization
plt.show()
