import string
from random import SystemRandom
from django.utils.text import slugify

def random_strings(k=5):
    return ''.join(SystemRandom().choices(
        string.ascii_lowercase + string.digits,
        k=k
    ))


def slugify_new(text, k):
    return slugify(text) + '-' + random_strings(k)


