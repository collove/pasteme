from math import floor, log10

from django import template

register = template.Library()


@register.filter
def millify(n):
    mill_names = ["", "K", "M"]
    n = float(n)
    mill_idx = max(
        0,
        min(
            len(mill_names) - 1,
            int(floor(0 if n == 0 else log10(abs(n)) / 3)),
        ),
    )

    is_more = "+" if mill_names[mill_idx] else ""

    return "{}{:.0f}{}".format(is_more, n / 10 ** (3 * mill_idx), mill_names[mill_idx])
