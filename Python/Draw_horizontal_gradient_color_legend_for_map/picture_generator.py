from PIL import Image, ImageDraw, ImageFont

# Define the dimensions of the rectangle
width = 1500
height = 40

# Define the list of colors
list_colors = ['43 131 186', '171 221 164', '255 255 191', '253 174 97', '215 25 28']

# Define the list of labels
label_list = [0, 10, 20, 30, 40, 50]

# Convert the list of colors from strings to tuples of integers
list_colors = [tuple(map(int, color.split())) for color in list_colors]



# Create a new image with the same dimensions as the rectangle
image = Image.new("RGB", (width, height), color="white")

# Create a drawing object
draw = ImageDraw.Draw(image)

# Load a font file and create a font object
font = ImageFont.truetype("arial.ttf", 16)

# Draw the gradient filled rectangle
for x in range(width):
    # Calculate the color at this column
    i = x * (len(list_colors) - 1) // width
    r = list_colors[i][0] + int((list_colors[i+1][0] - list_colors[i][0]) * (x % (width // (len(list_colors) - 1))) / (width // (len(list_colors) - 1)))
    g = list_colors[i][1] + int((list_colors[i+1][1] - list_colors[i][1]) * (x % (width // (len(list_colors) - 1))) / (width // (len(list_colors) - 1)))
    b = list_colors[i][2] + int((list_colors[i+1][2] - list_colors[i][2]) * (x % (width // (len(list_colors) - 1))) / (width // (len(list_colors) - 1)))
    color = (r, g, b)

    # Draw a vertical line of this color at this column
    draw.line((x, 0, x, 15), fill=color)

    # Check if this column corresponds to a label
    if x * (len(label_list) - 1) % width == 0:
        # Get the label text
        label_text = str(label_list[x * (len(label_list) - 1) // width])

        # Get the size of the label text
        label_size = font.getsize(label_text)

        # Calculate the position to draw the label text
        # label_x = x - label_size[0] // 2
        label_y = height - label_size[1] - 5

        print("x: ", x)

        # Calculate the position to draw the label text
        if x == 0:
            label_x = 1
        elif x == width + 300: # todo calculate and set position for last label
            label_x = width - 10
        else:
            label_x = x - label_size[0] // 2

        # Draw the label text
        draw.text((label_x, label_y), label_text, font=font, fill="black")

# Save the image to a file
image.save("gradient_rectangle_horizontal_labels.png")
