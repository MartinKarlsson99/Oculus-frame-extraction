import os

import cv2
from ffmpeg import FFmpeg, Progress
import ffmpeg


def apply_mask(image, mask):
    return image * (mask//255)


def chop_video(video_path, output_dir):
    ffmpeg = (
        FFmpeg()
        .option("y")
        .input(video_path)
        .output(
            os.path.join(output_dir, '%d.png'),
            crf=30
        )
    )

    ffmpeg.execute()
