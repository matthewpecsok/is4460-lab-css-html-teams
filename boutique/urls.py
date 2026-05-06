from django.urls import path
from . import views

app_name = "boutique"

urlpatterns = [
    path("", views.home, name="home"),
    path("products/sunrise_bliss/", views.sunrise_bliss, name="sunrise_bliss"),
    path("products/midnight_romance/", views.midnight_romance, name="midnight_romance"),
    path("products/spring_meadow/", views.spring_meadow, name="spring_meadow"),
    path("products/ocean_breeze/", views.ocean_breeze, name="ocean_breeze"),
    path("products/enchanted_forest/", views.enchanted_forest, name="enchanted_forest"),
    path("products/pastel_dream/", views.pastel_dream, name="pastel_dream"),
    path("products/tropical_paradise/", views.tropical_paradise, name="tropical_paradise"),
    path("products/lavender_serenity/", views.lavender_serenity, name="lavender_serenity"),
    path("products/golden_harvest/", views.golden_harvest, name="golden_harvest"),
    path("products/cherry_blossom/", views.cherry_blossom, name="cherry_blossom"),
    path("products/sunset_glow/", views.sunset_glow, name="sunset_glow"),
    path("products/winter_wonderland/", views.winter_wonderland, name="winter_wonderland"),
    path("products/blushing_bride/", views.blushing_bride, name="blushing_bride"),
    path("products/wildflower_whisper/", views.wildflower_whisper, name="wildflower_whisper"),
    path("products/moody_mauve/", views.moody_mauve, name="moody_mauve"),
    path("products/honeybee_garden/", views.honeybee_garden, name="honeybee_garden"),
    path("products/rose_royale/", views.rose_royale, name="rose_royale"),
    path("products/citrus_burst/", views.citrus_burst, name="citrus_burst"),
    path("products/midnight_orchid/", views.midnight_orchid, name="midnight_orchid"),
    path("products/peony_paradise/", views.peony_paradise, name="peony_paradise"),
    path("products/desert_rose/", views.desert_rose, name="desert_rose"),
    path("products/garden_party/", views.garden_party, name="garden_party"),
    path("products/frosted_berry/", views.frosted_berry, name="frosted_berry"),
    path("products/sunflower_fields/", views.sunflower_fields, name="sunflower_fields"),
    path("products/lush_lotus/", views.lush_lotus, name="lush_lotus"),
    path("products/fiesta_bloom/", views.fiesta_bloom, name="fiesta_bloom"),
    path("products/ivory_elegance/", views.ivory_elegance, name="ivory_elegance"),
    path("products/rainbow_riot/", views.rainbow_riot, name="rainbow_riot"),
    path("products/secret_garden/", views.secret_garden, name="secret_garden"),
    path("products/azure_dream/", views.azure_dream, name="azure_dream"),
]
