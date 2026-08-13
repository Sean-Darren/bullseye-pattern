import os

BASE_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

MODEL_DIRECTORY = os.path.join(BASE_DIRECTORY, "models")
MODEL_PATH = os.path.join(MODEL_DIRECTORY, "best.pt")
FALLBACK_MODEL = "yolov8n.pt"

DEFAUL_CONFIDENCE_TRESHOLD = 0.25
DEFAULT_IOU_THRESHOLD = 0.45
IMAGE_SIZE = (640, 640)

TEMP_RAW_CHART = os.path.join(BASE_DIRECTORY, "temp_raw.png")
TEMP_DETECTED_CHART = os.path.join(BASE_DIRECTORY, "temp_detected.png")

#data default 
DEFAULT_TICKER = "0700.HK"
DEFAULT_PERIOD = "6mo"
DEFAULT_INTERVAL = "1d"


PERIODS = ["1mo", "3mo", "6mo", "1y", "2y", "5y"]
INTERVALS = ["1d", "1h", "1wk"]

COLORS = {
    "bg": "#1e1e1e",
    "panel": "#2d2d2d",
    "accent": "#00c853",
    "text": "#e0e0e0",
    "danger": "#ff5252",
}