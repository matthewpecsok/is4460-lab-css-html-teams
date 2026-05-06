from django.test import TestCase, Client
from django.urls import reverse
from .views import PRODUCTS


class HomePageTest(TestCase):
    def test_homepage_returns_200(self):
        response = self.client.get(reverse("boutique:home"))
        self.assertEqual(response.status_code, 200)

    def test_homepage_contains_30_products(self):
        response = self.client.get(reverse("boutique:home"))
        self.assertContains(response, "View Details", count=30)

    def test_homepage_links_all_products(self):
        response = self.client.get(reverse("boutique:home"))
        for product in PRODUCTS:
            url = reverse("boutique:product_detail", args=[product["id"]])
            self.assertContains(response, url)


class ProductDetailPageTest(TestCase):
    def test_all_product_pages_return_200(self):
        for product in PRODUCTS:
            url = reverse("boutique:product_detail", args=[product["id"]])
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200, msg=f"Product {product['id']} returned non-200")

    def test_product_page_shows_name_and_description(self):
        product = PRODUCTS[0]
        url = reverse("boutique:product_detail", args=[product["id"]])
        response = self.client.get(url)
        self.assertContains(response, product["name"])
        self.assertContains(response, product["price"])

    def test_product_page_shows_arranged_by_tbd(self):
        for product in PRODUCTS:
            url = reverse("boutique:product_detail", args=[product["id"]])
            response = self.client.get(url)
            self.assertContains(response, "TBD")

    def test_invalid_product_returns_404(self):
        response = self.client.get(
            reverse("boutique:product_detail", args=[9999])
        )
        self.assertEqual(response.status_code, 404)


class ProductDataTest(TestCase):
    def test_exactly_30_products(self):
        self.assertEqual(len(PRODUCTS), 30)

    def test_all_products_have_required_fields(self):
        for product in PRODUCTS:
            self.assertIn("id", product)
            self.assertIn("name", product)
            self.assertIn("price", product)
            self.assertIn("description", product)

    def test_product_ids_are_unique_and_sequential(self):
        ids = [p["id"] for p in PRODUCTS]
        self.assertEqual(sorted(ids), list(range(1, 31)))

