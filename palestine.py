from PIL import Image, ImageDraw

# Define flag dimensions
width = 2000
height = 1000

# Create a new image with white background
flag = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(flag)

# Stripe height calculation (each stripe is 1/3 of total height)
stripe_height = height // 3

# Draw black stripe (top)
draw.rectangle([(0, 0), (width, stripe_height)], fill="black")

# Draw white stripe (middle)
draw.rectangle([(0, stripe_height), (width, 2 * stripe_height)], fill="white")

# Draw green stripe (bottom)
draw.rectangle([(0, 2 * stripe_height), (width, height)], fill="green")

# Draw red triangle on the left
triangle_points = [(0, 0), (0, height), (width // 3, height // 2)]
draw.polygon(triangle_points, fill="red")

# Save the image
flag.save("palestine_flag.png")

print("✅ Palestine flag generated and saved as 'palestine_flag.png'")
