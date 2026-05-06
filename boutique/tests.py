from django.test import TestCase
from django.urls import NoReverseMatch, reverse
import re


PRODUCT_SLUGS = [
    "sunrise_bliss",
    "midnight_romance",
    "spring_meadow",
    "ocean_breeze",
    "enchanted_forest",
    "pastel_dream",
    "tropical_paradise",
    "lavender_serenity",
    "golden_harvest",
    "cherry_blossom",
    "sunset_glow",
    "winter_wonderland",
    "blushing_bride",
    "wildflower_whisper",
    "moody_mauve",
    "honeybee_garden",
    "rose_royale",
    "citrus_burst",
    "midnight_orchid",
    "peony_paradise",
    "desert_rose",
    "garden_party",
    "frosted_berry",
    "sunflower_fields",
    "lush_lotus",
    "fiesta_bloom",
    "ivory_elegance",
    "rainbow_riot",
    "secret_garden",
    "azure_dream",
]



class ProductRoutesTest(TestCase):
    def test_exactly_30_products(self):
        self.assertEqual(len(PRODUCT_SLUGS), 30)

    def test_product_route_names_are_unique(self):
        self.assertEqual(len(set(PRODUCT_SLUGS)), 30)


class ProductArrangedByTest(TestCase):
    def test_each_product_page_arranged_by_is_not_tbd(self):
        # Require a non-empty arranger name and explicitly reject TBD.
        arranged_by_pattern = re.compile(
            r"Arranged by:\s*<strong>\s*(?!TBD\s*</strong>)[^<]+</strong>",
            re.IGNORECASE,
        )

        for slug in PRODUCT_SLUGS:
            with self.subTest(product=slug):
                response = self.client.get(reverse(f"boutique:{slug}"))
                self.assertEqual(response.status_code, 200)

                html = response.content.decode("utf-8")
                self.assertRegex(html, arranged_by_pattern)
                self.assertNotIn("Arranged by: <strong>TBD</strong>", html)

