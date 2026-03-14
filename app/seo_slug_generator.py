from itertools import product
from app.seo_slug_data import BASE_KEYWORDS

PREFIX = [
"",
"convert",
"free",
"online",
"quick",
"instant",
]

SUFFIX = [
"",
"converter",
"calculator",
"conversion",
"tool",
]

def generate_slugs():

    slugs = set()

    for base, p, s in product(BASE_KEYWORDS, PREFIX, SUFFIX):

        parts = []

        if p:
            parts.append(p)

        parts.append(base)

        if s:
            parts.append(s)

        slug = "-".join(parts)

        slugs.add(slug)

    return sorted(slugs)

SEO_SLUGS = generate_slugs()
