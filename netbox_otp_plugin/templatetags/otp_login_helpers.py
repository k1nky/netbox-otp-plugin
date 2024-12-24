from django import template

register = template.Library()


@register.filter()
def is_version_greater(value, target):
    """ Returns true if `value` is greater than or equal to `target`.
    """
    version = lambda s: list(map(int, s.split('.')))    # noqa: E731
    return version(value) >= version(target)
