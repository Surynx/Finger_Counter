
import cv2 as cv

# Load the image in color using OpenCV
image_path = "wall.jpg"
c = cv.imread(image_path)

# Check if the image is loaded successfully
if c is None:
    print("Error: Unable to load the image. Check the file path.")
else:
    # Draw a line on the image
    # (500, 99) is the starting point, (769, 638) is the ending point
    # (255, 0, 0) is the color in BGR (Blue)
    # 5 is the thickness of the line
    cv.line(c, (500, 99), (769, 638), (255, 0, 0), 5)

    # Display the modified image
    cv.imshow("Image with Line", c)

    # Wait for a key press and close all OpenCV windows
    cv.waitKey(0)
    cv.destroyAllWindows()