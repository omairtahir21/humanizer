from django.http import JsonResponse
import json
from .functions import humanize_text

def humanize_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            input_text = data.get('text', '')

            if not input_text:
                return JsonResponse({'error': 'Text is required.'}, status=400)

            result = humanize_text(input_text)
            return JsonResponse({'humanized_text': result}, status=200)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Only POST method allowed'}, status=405)
