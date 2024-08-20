# tasks.py

from celery import shared_task
import time


@shared_task(rate_limit='1/m')
def add(x, y):
    time.sleep(10)  # Simulate a delay for testing purposes
    return x + y


@shared_task
def high_priority_task(x, y):
    return x - y


@shared_task(name='video.encode')
def encode_video(video_id):
    # Video encoding logic here
    return f"Encoded video {video_id}"


@shared_task(name='feed.tasks.process_feed')
def process_feed(feed_id):
    # Feed processing logic here
    return f"Processed feed {feed_id}"


@shared_task(name='image.tasks.resize_image')
def resize_image(image_id):
    # Image resizing logic here
    return f"Resized image {image_id}"
