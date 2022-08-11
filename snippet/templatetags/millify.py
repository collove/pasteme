from math import floor, log10
from django import template

register = template.Library()


@register.filter
def millify(n):
    mill_names = ["", "K+", "M+"]
    n = float(n)
    mill_idx = max(
        0,
        min(
            len(mill_names) - 1,
            int(floor(0 if n == 0 else log10(abs(n)) / 3)),
        ),
    )

    return "{:.0f}{}".format(n / 10 ** (3 * mill_idx), mill_names[mill_idx])
