"""
Generate banner images for the MDP Learning Project communication email.
Uses gen_image_bedrock.py from the project root.
"""

import asyncio
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from gen_image_bedrock import generate_image_bedrock

OUT_DIR = os.path.dirname(os.path.abspath(__file__))


async def main():
    # Email banner — wide format, Manulife green theme
    print("Generating email banner...")
    await generate_image_bedrock(
        prompt=(
            "A vibrant corporate email banner for an insurance company internal learning campaign. "
            "Green and white color scheme (Manulife brand green #00A758). "
            "Show a playful illustration of people interacting with a large tablet/screen displaying charts and graphs. "
            "Include subtle icons: lightbulb, game controller, trophy. "
            "Modern flat illustration style, clean and professional. "
            "Text area on the right side for overlay. "
            "No text in the image itself."
        ),
        aspect_ratio="16:9",
        output_path=os.path.join(OUT_DIR, "email_banner.png"),
    )
    print("Done: email_banner.png")

    # Game show banner
    print("Generating game show banner...")
    await generate_image_bedrock(
        prompt=(
            "A fun colorful game show banner for a corporate knowledge quiz event. "
            "Board game theme with dice, chess pieces, confetti. "
            "Green and gold color scheme. "
            "Playful and engaging, like a TV game show poster. "
            "Modern flat illustration style. "
            "No text in the image."
        ),
        aspect_ratio="16:9",
        output_path=os.path.join(OUT_DIR, "gameshow_banner.png"),
    )
    print("Done: gameshow_banner.png")


if __name__ == "__main__":
    asyncio.run(main())
