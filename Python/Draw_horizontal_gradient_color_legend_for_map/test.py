from PIL import Image, ImageDraw, ImageFont

# Define the dimensions of the rectangle
width = 300
height = 200

# Define the list of colors
list_colors = ['43 131 186', '171 221 164', '255 255 191', '253 174 97', '215 25 28']

# Convert the list of colors from strings to tuples of integers
list_colors = [tuple(map(int, color.split())) for color in list_colors]

# Define the list of labels
label_list = [0, 10, 20, 30, 40, 50]

# Create a new image with the same dimensions as the rectangle
image = Image.new("RGB", (width, height), color="white")

# Create a drawing object
draw = ImageDraw.Draw(image)

# Load a font file and create a font object
font = ImageFont.truetype("arial.ttf", 16)

# Draw the gradient filled rectangle
for y in range(height):
    # Calculate the color at this row
    i = y * (len(list_colors) - 1) // height
    r = list_colors[i][0] + int((list_colors[i+1][0] - list_colors[i][0]) * (y % (height // (len(list_colors) - 1))) / (height // (len(list_colors) - 1)))
    g = list_colors[i][1] + int((list_colors[i+1][1] - list_colors[i][1]) * (y % (height // (len(list_colors) - 1))) / (height // (len(list_colors) - 1)))
    b = list_colors[i][2] + int((list_colors[i+1][2] - list_colors[i][2]) * (y % (height // (len(list_colors) - 1))) / (height // (len(list_colors) - 1)))
    color = (r, g, b)

    # Draw a horizontal line of this color at this row
    draw.line((0, y, width, y), fill=color)

    # Check if this row corresponds to a label
    if y * (len(label_list) - 1) % height == 0:
        # Get the label text
        label_text = str(label_list[y * (len(label_list) - 1) // height])

        # Get the size of the label text
        label_size = font.getsize(label_text)

        # Calculate the position to draw the label text
       # label_x = width - label_size[0] - 10
        label_y = y - label_size[1] // 2

        # Calculate the position to draw the label text
        if y == 0:
            label_x = 10  # Move the first label 10 pixels to the left
        elif y == height - 1:
            label_x = width - label_size[0] - 30  # Move the last label 30 pixels to the right
        else:
            label_x = width - label_size[0] - 20  # Leave other labels at the default position

        # Draw the label text
        draw.text((label_x, label_y), label_text, font=font, fill="black")

# Save the image to a file
image.save("gradient_rectangle_horizontal_labels.png")
