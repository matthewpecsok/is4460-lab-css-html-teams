from django.test import TestCase
from django.urls import NoReverseMatch, reverse


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


class HomePageTest(TestCase):
    def test_homepage_returns_200(self):
        response = self.client.get(reverse("boutique:home"))
        self.assertEqual(response.status_code, 200)

    def test_homepage_contains_30_products(self):
        response = self.client.get(reverse("boutique:home"))
        self.assertContains(response, "View Details", count=30)

    def test_homepage_links_all_products(self):
        response = self.client.get(reverse("boutique:home"))
        for slug in PRODUCT_SLUGS:
            url = reverse(f"boutique:{slug}")
            self.assertContains(response, url)


class ProductPageTest(TestCase):
    def test_all_product_pages_return_200(self):
        for slug in PRODUCT_SLUGS:
            url = reverse(f"boutique:{slug}")
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200, msg=f"Product page {slug} returned non-200")

    def test_product_page_shows_arranged_by_tbd(self):
        for slug in PRODUCT_SLUGS:
            url = reverse(f"boutique:{slug}")
            response = self.client.get(url)
            self.assertContains(response, "TBD")

    def test_legacy_dynamic_product_url_returns_404(self):
        response = self.client.get("/product/1/")
        self.assertEqual(response.status_code, 404)


class ProductRoutesTest(TestCase):
    def test_exactly_30_products(self):
        self.assertEqual(len(PRODUCT_SLUGS), 30)

    def test_legacy_named_route_removed(self):
        with self.assertRaises(NoReverseMatch):
            reverse("boutique:product_detail")

    def test_product_route_names_are_unique(self):
        self.assertEqual(len(set(PRODUCT_SLUGS)), 30)

