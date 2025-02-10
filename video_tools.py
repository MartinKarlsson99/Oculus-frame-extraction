import os
from ffmpeg import FFmpeg


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
