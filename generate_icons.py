from PIL import Image, ImageDraw


def draw_line_graph_icon(size, out_path):
    # Create base image with opaque circle background
    base = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    base_draw = ImageDraw.Draw(base)
    pad = int(size * 0.06)
    bbox = (pad, pad, size - pad, size - pad)
    base_draw.ellipse(bbox, fill=(30, 136, 229, 255))

    # Create overlay for semi-transparent elements and compositing-safe drawing
    overlay = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    # Grid lines (semi-transparent)
    grid_color = (255, 255, 255, 60)
    for i in range(1, 4):
        y = pad + (size - 2 * pad) * i / 4
        draw.line([(pad, y), (size - pad, y)], fill=grid_color, width=1)

    # Graph polyline (normalized points)
    points = [(0.05, 0.75), (0.2, 0.55), (0.4, 0.6), (0.6, 0.35), (0.8, 0.45), (0.95, 0.25)]
    scaled = [
        (pad + x * (size - 2 * pad), pad + y * (size - 2 * pad)) for x, y in points
    ]

    # Draw filled area under the graph with transparency on overlay
    area = [(scaled[0][0], size - pad)] + scaled + [(scaled[-1][0], size - pad)]
    draw.polygon(area, fill=(255, 255, 255, 40))

    # Draw polyline (mostly opaque) and points on overlay
    draw.line(scaled, fill=(255, 255, 255, 220), width=max(2, size // 64))
    r = max(2, size // 64)
    for x, y in scaled:
        draw.ellipse((x - r, y - r, x + r, y + r), fill=(255, 255, 255, 255))

    # Composite overlay onto base to preserve base alpha and properly blend transparency
    result = Image.alpha_composite(base, overlay)
    result.save(out_path)


if __name__ == '__main__':
    draw_line_graph_icon(192, 'icon-192.png')
    draw_line_graph_icon(512, 'icon-512.png')
