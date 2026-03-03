from __future__ import annotations

import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
FIGURES_DIR = ROOT / "figures"
OUTPUT_PATH = FIGURES_DIR / "topic_growth_by_year.png"
TOPICS_PATH = ROOT / "TOPICS.md"

YEARS = ["2022", "2023", "2024", "2025"]
COLORS = [
    "#0B3C5D",
    "#328CC1",
    "#D9B310",
    "#1D2731",
    "#B56576",
    "#6D597A",
    "#355070",
    "#588157",
    "#BC4749",
    "#6C757D",
    "#FF7B00",
    "#3A86FF",
    "#8338EC",
    "#2A9D8F",
]

CANVAS_W = 2200
CANVAS_H = 1400
MARGIN_LEFT = 190
MARGIN_RIGHT = 620
MARGIN_TOP = 120
MARGIN_BOTTOM = 150
PLOT_W = CANVAS_W - MARGIN_LEFT - MARGIN_RIGHT
PLOT_H = CANVAS_H - MARGIN_TOP - MARGIN_BOTTOM


def load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
        if bold
        else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf"
        if bold
        else "/usr/share/fonts/dejavu/DejaVuSans.ttf",
    ]
    for candidate in candidates:
        path = Path(candidate)
        if path.exists():
            return ImageFont.truetype(str(path), size=size)
    return ImageFont.load_default()


def load_topics() -> list[str]:
    return [line[3:].strip() for line in TOPICS_PATH.read_text().splitlines() if line.startswith("## ")]


def count_topics(topics: list[str]) -> dict[str, list[int]]:
    counts = {topic: [0, 0, 0, 0] for topic in topics}
    for paper_file in sorted(ROOT.glob("20*/**/PAPERS.md")):
        year = paper_file.parts[-3]
        if year not in YEARS:
            continue
        year_idx = YEARS.index(year)
        text = paper_file.read_text()
        for tag_line in re.findall(r"^- \*\*Tags:\*\* (.+)$", text, flags=re.M):
            for tag in [tag.strip() for tag in tag_line.split(",") if tag.strip()]:
                if tag in counts:
                    counts[tag][year_idx] += 1
    return counts


def x_position(index: int) -> float:
    return MARGIN_LEFT + (PLOT_W * index / (len(YEARS) - 1))


def y_position(value: int, max_y: int) -> float:
    return MARGIN_TOP + PLOT_H - (PLOT_H * value / max_y)


def draw_rotated_text(
    image: Image.Image,
    text: str,
    font: ImageFont.ImageFont,
    fill: str,
    center: tuple[int, int],
) -> None:
    dummy = Image.new("RGBA", (1, 1), (255, 255, 255, 0))
    dummy_draw = ImageDraw.Draw(dummy)
    bbox = dummy_draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    text_img = Image.new("RGBA", (text_w + 20, text_h + 20), (255, 255, 255, 0))
    text_draw = ImageDraw.Draw(text_img)
    text_draw.text((10, 10), text, font=font, fill=fill)
    rotated = text_img.rotate(90, expand=True)
    x = int(center[0] - rotated.width / 2)
    y = int(center[1] - rotated.height / 2)
    image.alpha_composite(rotated, (x, y))


def render() -> None:
    FIGURES_DIR.mkdir(exist_ok=True)
    topics = load_topics()
    counts = count_topics(topics)
    max_y = max(max(series) for series in counts.values())
    max_y = max(max_y, 1)

    title_font = load_font(48, bold=True)
    axis_font = load_font(34, bold=True)
    tick_font = load_font(26)
    legend_font = load_font(24)

    image = Image.new("RGBA", (CANVAS_W, CANVAS_H), "white")
    draw = ImageDraw.Draw(image)

    # Title
    title = "ResearchAtlas Topic Growth by Year"
    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    title_w = title_bbox[2] - title_bbox[0]
    draw.text(((CANVAS_W - title_w) / 2, 28), title, fill="#111111", font=title_font)

    # Grid + axes
    for tick in range(max_y + 1):
        yy = y_position(tick, max_y)
        draw.line((MARGIN_LEFT, yy, MARGIN_LEFT + PLOT_W, yy), fill="#DDDDDD", width=2)
        label = str(tick)
        bbox = draw.textbbox((0, 0), label, font=tick_font)
        draw.text((MARGIN_LEFT - 24 - (bbox[2] - bbox[0]), yy - 14), label, fill="#222222", font=tick_font)

    draw.line((MARGIN_LEFT, MARGIN_TOP, MARGIN_LEFT, MARGIN_TOP + PLOT_H), fill="#222222", width=4)
    draw.line((MARGIN_LEFT, MARGIN_TOP + PLOT_H, MARGIN_LEFT + PLOT_W, MARGIN_TOP + PLOT_H), fill="#222222", width=4)

    for idx, year in enumerate(YEARS):
        xx = x_position(idx)
        draw.line((xx, MARGIN_TOP + PLOT_H, xx, MARGIN_TOP + PLOT_H + 12), fill="#222222", width=3)
        bbox = draw.textbbox((0, 0), year, font=tick_font)
        draw.text((xx - (bbox[2] - bbox[0]) / 2, MARGIN_TOP + PLOT_H + 24), year, fill="#222222", font=tick_font)

    x_label = "Year"
    bbox = draw.textbbox((0, 0), x_label, font=axis_font)
    draw.text((MARGIN_LEFT + PLOT_W / 2 - (bbox[2] - bbox[0]) / 2, CANVAS_H - 72), x_label, fill="#222222", font=axis_font)

    draw_rotated_text(
        image=image,
        text="Paper Count",
        font=axis_font,
        fill="#222222",
        center=(72, MARGIN_TOP + PLOT_H // 2),
    )

    # Series
    for idx, topic in enumerate(topics):
        color = COLORS[idx % len(COLORS)]
        points = [(x_position(i), y_position(value, max_y)) for i, value in enumerate(counts[topic])]
        draw.line(points, fill=color, width=5)
        for px, py in points:
            draw.ellipse((px - 8, py - 8, px + 8, py + 8), fill=color, outline=color)

    # Legend
    legend_x = MARGIN_LEFT + PLOT_W + 36
    legend_y = 122
    for idx, topic in enumerate(topics):
        color = COLORS[idx % len(COLORS)]
        yy = legend_y + idx * 54
        draw.line((legend_x, yy, legend_x + 34, yy), fill=color, width=5)
        draw.ellipse((legend_x + 11, yy - 7, legend_x + 25, yy + 7), fill=color, outline=color)
        draw.text((legend_x + 52, yy - 16), topic, fill="#111111", font=legend_font)

    image.convert("RGB").save(OUTPUT_PATH)


if __name__ == "__main__":
    render()
