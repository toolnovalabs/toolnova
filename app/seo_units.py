from itertools import permutations
import re


def slugify(text: str) -> str:
    text = str(text).strip().lower()

    replacements = {
        "/": "-per-",
        "²": "2",
        "³": "3",
        "°": "",
        "(": "",
        ")": "",
        ".": "",
        ",": "",
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"[^a-z0-9\-]", "", text)
    text = re.sub(r"-{2,}", "-", text).strip("-")
    return text


def make_factor_pages(
    category: str,
    units: dict[str, float],
    allowed_pairs: set[tuple[str, str]] | None = None,
) -> list[dict]:
    pages = []

    for from_unit, to_unit in permutations(units.keys(), 2):
        if allowed_pairs is not None and (from_unit, to_unit) not in allowed_pairs:
            continue

        from_factor = units[from_unit]
        to_factor = units[to_unit]
        factor = from_factor / to_factor

        slug = f"{slugify(from_unit)}-to-{slugify(to_unit)}"
        title = f"{from_unit} to {to_unit} Converter"

        pages.append(
            {
                "slug": slug,
                "title": title,
                "from_unit": from_unit,
                "to_unit": to_unit,
                "factor": factor,
                "category": category,
            }
        )

    return pages


LENGTH_UNITS = {
    "Meters": 1.0,
    "Kilometers": 1000.0,
    "Centimeters": 0.01,
    "Millimeters": 0.001,
    "Feet": 0.3048,
    "Inches": 0.0254,
    "Yards": 0.9144,
    "Miles": 1609.344,
}

WEIGHT_UNITS = {
    "Kilograms": 1.0,
    "Grams": 0.001,
    "Milligrams": 0.000001,
    "Pounds": 0.45359237,
    "Ounces": 0.028349523125,
    "Tons": 1000.0,
}

VOLUME_UNITS = {
    "Liters": 1.0,
    "Milliliters": 0.001,
    "Cubic Meters": 1000.0,
    "Gallons": 3.785411784,
    "Cups": 0.2365882365,
    "Pints": 0.473176473,
}

SPEED_UNITS = {
    "km/h": 0.2777777778,
    "m/s": 1.0,
    "mph": 0.44704,
    "Knots": 0.5144444444,
    "ft/s": 0.3048,
}

AREA_UNITS = {
    "Square Meters": 1.0,
    "Square Feet": 0.09290304,
    "Acres": 4046.8564224,
    "Hectares": 10000.0,
    "Square Yards": 0.83612736,
    "Square Kilometers": 1000000.0,
}

LENGTH_ALLOWED = {
    ("Meters", "Feet"), ("Feet", "Meters"),
    ("Meters", "Inches"), ("Inches", "Meters"),
    ("Meters", "Yards"), ("Yards", "Meters"),
    ("Kilometers", "Miles"), ("Miles", "Kilometers"),
    ("Centimeters", "Inches"), ("Inches", "Centimeters"),
    ("Millimeters", "Inches"), ("Inches", "Millimeters"),
    ("Meters", "Kilometers"), ("Kilometers", "Meters"),
    ("Meters", "Centimeters"), ("Centimeters", "Meters"),
    ("Meters", "Millimeters"), ("Millimeters", "Meters"),
    ("Yards", "Feet"), ("Feet", "Yards"),
    ("Miles", "Feet"), ("Feet", "Miles"),
    ("Kilometers", "Feet"), ("Feet", "Kilometers"),
    ("Miles", "Yards"), ("Yards", "Miles"),
    ("Centimeters", "Feet"), ("Feet", "Centimeters"),
    ("Millimeters", "Feet"), ("Feet", "Millimeters"),
    ("Miles", "Inches"), ("Inches", "Miles"),
    ("Yards", "Inches"), ("Inches", "Yards"),
    ("Kilometers", "Yards"), ("Yards", "Kilometers"),
    ("Centimeters", "Yards"), ("Yards", "Centimeters"),
    ("Millimeters", "Yards"), ("Yards", "Millimeters"),
}

WEIGHT_ALLOWED = {
    ("Kilograms", "Pounds"), ("Pounds", "Kilograms"),
    ("Kilograms", "Grams"), ("Grams", "Kilograms"),
    ("Kilograms", "Ounces"), ("Ounces", "Kilograms"),
    ("Grams", "Ounces"), ("Ounces", "Grams"),
    ("Pounds", "Ounces"), ("Ounces", "Pounds"),
    ("Tons", "Kilograms"), ("Kilograms", "Tons"),
    ("Tons", "Pounds"), ("Pounds", "Tons"),
    ("Milligrams", "Grams"), ("Grams", "Milligrams"),
    ("Milligrams", "Kilograms"), ("Kilograms", "Milligrams"),
    ("Grams", "Pounds"), ("Pounds", "Grams"),
    ("Tons", "Ounces"), ("Ounces", "Tons"),
    ("Kilograms", "Milligrams"), ("Milligrams", "Kilograms"),
    ("Grams", "Tons"), ("Tons", "Grams"),
    ("Pounds", "Milligrams"), ("Milligrams", "Pounds"),
    ("Ounces", "Milligrams"), ("Milligrams", "Ounces"),
}

VOLUME_ALLOWED = {
    ("Liters", "Gallons"), ("Gallons", "Liters"),
    ("Liters", "Milliliters"), ("Milliliters", "Liters"),
    ("Liters", "Cubic Meters"), ("Cubic Meters", "Liters"),
    ("Gallons", "Milliliters"), ("Milliliters", "Gallons"),
    ("Cups", "Milliliters"), ("Milliliters", "Cups"),
    ("Cups", "Liters"), ("Liters", "Cups"),
    ("Pints", "Milliliters"), ("Milliliters", "Pints"),
    ("Pints", "Liters"), ("Liters", "Pints"),
    ("Gallons", "Cubic Meters"), ("Cubic Meters", "Gallons"),
    ("Gallons", "Cups"), ("Cups", "Gallons"),
    ("Gallons", "Pints"), ("Pints", "Gallons"),
    ("Cubic Meters", "Milliliters"), ("Milliliters", "Cubic Meters"),
    ("Cups", "Pints"), ("Pints", "Cups"),
    ("Liters", "Pints"), ("Pints", "Liters"),
}

SPEED_ALLOWED = {
    ("km/h", "mph"), ("mph", "km/h"),
    ("km/h", "m/s"), ("m/s", "km/h"),
    ("mph", "m/s"), ("m/s", "mph"),
    ("Knots", "km/h"), ("km/h", "Knots"),
    ("Knots", "mph"), ("mph", "Knots"),
    ("Knots", "m/s"), ("m/s", "Knots"),
    ("km/h", "ft/s"), ("ft/s", "km/h"),
    ("mph", "ft/s"), ("ft/s", "mph"),
    ("m/s", "ft/s"), ("ft/s", "m/s"),
    ("Knots", "ft/s"), ("ft/s", "Knots"),
}

AREA_ALLOWED = {
    ("Square Meters", "Square Feet"), ("Square Feet", "Square Meters"),
    ("Square Meters", "Acres"), ("Acres", "Square Meters"),
    ("Square Meters", "Hectares"), ("Hectares", "Square Meters"),
    ("Square Feet", "Acres"), ("Acres", "Square Feet"),
    ("Square Feet", "Hectares"), ("Hectares", "Square Feet"),
    ("Acres", "Hectares"), ("Hectares", "Acres"),
    ("Square Meters", "Square Yards"), ("Square Yards", "Square Meters"),
    ("Square Feet", "Square Yards"), ("Square Yards", "Square Feet"),
    ("Square Kilometers", "Hectares"), ("Hectares", "Square Kilometers"),
    ("Square Kilometers", "Acres"), ("Acres", "Square Kilometers"),
    ("Square Kilometers", "Square Meters"), ("Square Meters", "Square Kilometers"),
}

TEMPERATURE_PAGES = [
    {
        "slug": "celsius-to-fahrenheit",
        "title": "Celsius to Fahrenheit Converter",
        "from_unit": "Celsius",
        "to_unit": "Fahrenheit",
        "formula": "(x * 9 / 5) + 32",
        "category": "Temperature",
    },
    {
        "slug": "fahrenheit-to-celsius",
        "title": "Fahrenheit to Celsius Converter",
        "from_unit": "Fahrenheit",
        "to_unit": "Celsius",
        "formula": "(x - 32) * 5 / 9",
        "category": "Temperature",
    },
    {
        "slug": "celsius-to-kelvin",
        "title": "Celsius to Kelvin Converter",
        "from_unit": "Celsius",
        "to_unit": "Kelvin",
        "formula": "x + 273.15",
        "category": "Temperature",
    },
    {
        "slug": "kelvin-to-celsius",
        "title": "Kelvin to Celsius Converter",
        "from_unit": "Kelvin",
        "to_unit": "Celsius",
        "formula": "x - 273.15",
        "category": "Temperature",
    },
    {
        "slug": "fahrenheit-to-kelvin",
        "title": "Fahrenheit to Kelvin Converter",
        "from_unit": "Fahrenheit",
        "to_unit": "Kelvin",
        "formula": "((x - 32) * 5 / 9) + 273.15",
        "category": "Temperature",
    },
    {
        "slug": "kelvin-to-fahrenheit",
        "title": "Kelvin to Fahrenheit Converter",
        "from_unit": "Kelvin",
        "to_unit": "Fahrenheit",
        "formula": "((x - 273.15) * 9 / 5) + 32",
        "category": "Temperature",
    },
    {
        "slug": "celsius-to-rankine",
        "title": "Celsius to Rankine Converter",
        "from_unit": "Celsius",
        "to_unit": "Rankine",
        "formula": "(x + 273.15) * 9 / 5",
        "category": "Temperature",
    },
    {
        "slug": "rankine-to-celsius",
        "title": "Rankine to Celsius Converter",
        "from_unit": "Rankine",
        "to_unit": "Celsius",
        "formula": "(x - 491.67) * 5 / 9",
        "category": "Temperature",
    },
    {
        "slug": "fahrenheit-to-rankine",
        "title": "Fahrenheit to Rankine Converter",
        "from_unit": "Fahrenheit",
        "to_unit": "Rankine",
        "formula": "x + 459.67",
        "category": "Temperature",
    },
    {
        "slug": "rankine-to-fahrenheit",
        "title": "Rankine to Fahrenheit Converter",
        "from_unit": "Rankine",
        "to_unit": "Fahrenheit",
        "formula": "x - 459.67",
        "category": "Temperature",
    },
    {
        "slug": "kelvin-to-rankine",
        "title": "Kelvin to Rankine Converter",
        "from_unit": "Kelvin",
        "to_unit": "Rankine",
        "formula": "x * 9 / 5",
        "category": "Temperature",
    },
    {
        "slug": "rankine-to-kelvin",
        "title": "Rankine to Kelvin Converter",
        "from_unit": "Rankine",
        "to_unit": "Kelvin",
        "formula": "x * 5 / 9",
        "category": "Temperature",
    },
]

SEO_UNIT_PAGES = []
SEO_UNIT_PAGES += make_factor_pages("Length", LENGTH_UNITS, LENGTH_ALLOWED)
SEO_UNIT_PAGES += make_factor_pages("Weight", WEIGHT_UNITS, WEIGHT_ALLOWED)
SEO_UNIT_PAGES += make_factor_pages("Volume", VOLUME_UNITS, VOLUME_ALLOWED)
SEO_UNIT_PAGES += make_factor_pages("Speed", SPEED_UNITS, SPEED_ALLOWED)
SEO_UNIT_PAGES += make_factor_pages("Area", AREA_UNITS, AREA_ALLOWED)
SEO_UNIT_PAGES += TEMPERATURE_PAGES

SEO_PAGES_BY_SLUG = {page["slug"]: page for page in SEO_UNIT_PAGES}