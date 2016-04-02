from django.http import HttpResponse, HttpResponseBadRequest

from cmdbox.snippets.models import Snippet


def snippet(request, username, slug):
    try:
        _snippet = Snippet.objects.get(user__username=username, slug=slug)
        is_help_request = 'h' in request.GET or 'help' in request.GET

        if is_help_request:
            output = _snippet.content
        else:
            format_params = _snippet.get_params()

            get_args = request.GET.get('a', request.GET.get('args', None))
            args = list()
            if get_args is not None:
                args = get_args.split(',')

            kwargs = dict()
            for field_name in format_params['kwargs']:
                if field_name in request.GET:
                    kwargs[field_name] = request.GET.get(field_name)

            output = _snippet.use(args, kwargs)
        return HttpResponse(output, content_type='text/plain')
    except Snippet.DoesNotExist:
        return HttpResponseBadRequest('Invalid URL. The snippet does not exist.', content_type='text/plain')
