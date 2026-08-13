import os
import cv2
from typing import Tuple, List, Dict
from ultralytics import YOLO
import config
import numpy as np

class VisionEngine:
    def __init__(self, model_path: str = config.MODEL_PATH):
        self.model_path = model_path
        self.model = self._initialize_model()

    def _initialize_model(self) -> YOLO:
        """loads custom trained model weight"""
        if os.path.exists(self.model_path):
            print(f"Successfully loaded custom model from: {self.model_path}")

            return YOLO(self.model_path)
        else:
            print(f"Could not find '{self.model_path}'.")
            print("[VisionEngine] Falling back to standard pre-trained yolov8n.pt")
            return YOLO("yolov8n.pt")

    def run_detection(self, source: str | np.ndarray, confidence_threshold: float = config.DEFAULT_CONFIDENCE_THRESHOLD,)-> Tuple[str, List[Dict]]:
        """Run YOLOv8 object detection on the chart image"""
        results = self.model.predict(
            source = source,
            conf = confidence_threshold,
            iou = config.DEFAULT_IOU_THRESHOLD,
            save = False,
            verbose = False,
        )

        result = results[0]

        anomated_frame = result.plot()
        cv2.imwrite(output_path, anomated_frame)

        detections = []
        for box in result.boxes:
            class_id = int(box.cls[0])
            class_name = self.model.names[class_id]
            confidence = float(box.conf[0])
            bbox = box.xyxy[0].tolist()

            detections.append({
                "class_name": class_name,
                "confidence": confidence,
                "bbox": [round(c, 2) for c in bbox]
            })

        return output_path, detections
