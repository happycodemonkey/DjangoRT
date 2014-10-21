from django.conf import settings

RT_HOST = getattr(settings, 'CHAMELEON_RT_HOST', '')
RT_UN = getattr(settings, 'CHAMELEON_RT_UN', '')
RT_PW = getattr(settings, 'CHAMELEON_RT_PW', '')
RT_QUEUE = getattr(settings, 'CHAMELEON_RT_QUEUE', 'Chameleon')
