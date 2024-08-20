from django.http import JsonResponse
from hello.tasks import add, high_priority_task, encode_video, process_feed, resize_image


def add_numbers(request, a, b):
    result = add.apply_async(args=[a, b], countdown=10, expires=3600)  # Expires after 1 hour
    return JsonResponse({"task_id": result.id})


def subtract_numbers(request, a, b):
    result = high_priority_task.delay(a, b)
    return JsonResponse({"task_id": result.id})


def encode_video_task(request, video_id):
    result = encode_video.delay(video_id)
    return JsonResponse({"task_id": result.id})


def process_feed_task(request, feed_id):
    result = process_feed.delay(feed_id)
    return JsonResponse({"task_id": result.id})


def resize_image_task(request, image_id):
    result = resize_image.delay(image_id)
    return JsonResponse({"task_id": result.id})


def get_result(request, task_id):
    from celery.result import AsyncResult
    result = AsyncResult(task_id)
    if result.state == 'SUCCESS':
        return JsonResponse({"result": result.result})
    else:
        return JsonResponse({"state": result.state})
