import pytest


@pytest.fixture(scope='class')
def set_params():
    params = {
        'q': '',
        'cp': 0,
        'client': 'desktop-gws-wiz-on-focus-serp',
        'xssi': 't',
        'ofp': 'EAEy1gEKGwoZUHl0aG9uIGRpY3Rpb25hcnkgZ2V0IGtleQoRCg9QeXRob24gZGljdCBnZXQKIgogUHl0aG9uIGdldCB2YWx1ZSBmcm9tIGRpY3Rpb25hcnkKFwoVRGljdCBtYXggdmFsdWUgcHl0aG9uCigKJlB5dGhvbiBkaWN0aW9uYXJ5IHJlbW92ZSBrZXkgYW5kIHZhbHVlCgsKCURpY3Qga2V5cwoPCg1QeXRob24gZ2V0IHZzCh0KG0RlbGV0ZSBrZXkgZnJvbSBkaWN0IFB5dGhvbhBHMsoBCjEKL0hvdyBkbyB5b3UgcmV0dXJuIGEgdmFsdWUgZnJvbSBhIGtleSBpbiBQeXRob24_CjEKL0hvdyBkbyB5b3UgYWNjZXNzIGEgZGljdGlvbmFyeSB2YWx1ZSBpbiBQeXRob24_CjsKOUhvdyBkbyBJIGdldCB0aGUgdmFsdWUgb2YgYSBzcGVjaWZpYyBrZXkgaW4gYSBkaWN0aW9uYXJ5PwoiCiBDYW4gSSBnZXQga2V5IGZyb20gdmFsdWUgUHl0aG9uPxDkAg'
    }
    return params
