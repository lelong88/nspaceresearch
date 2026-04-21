#!/usr/bin/env python3
"""
create_preint_a2_1.py - Preintermediate zh-vi: Vietnamese Long-Distance Travel
Series: A2 城市出行与交通 (ii4ilg7x), Display Order: 3, Price: 49
Tone: desc=metaphor_led, farewell=quiet_awe
"""
import sys, json, logging
sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums/zh-vi")
from api_helpers import create_curriculum, add_to_series, set_display_order, set_price
from validate_content import validate
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
SERIES_ID = "ii4ilg7x"
DISPLAY_ORDER = 3
PRICE = 49
