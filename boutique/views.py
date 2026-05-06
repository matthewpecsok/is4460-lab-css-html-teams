from django.shortcuts import render, get_object_or_404

PRODUCTS = [
    {
        "id": 1,
        "name": "Sunrise Bliss",
        "price": "$45.00",
        "description": (
            "A radiant arrangement bursting with golden sunflowers, bright yellow roses, and sprigs of "
            "baby's breath. Perfect for brightening someone's morning and spreading joy throughout the day. "
            "Presented in a clear glass vase tied with an orange ribbon, Sunrise Bliss captures the warmth "
            "and energy of a perfect summer sunrise. Ideal for birthdays, get-well wishes, or simply "
            "letting a special person know you are thinking of them."
        ),
    },
    {
        "id": 2,
        "name": "Midnight Romance",
        "price": "$60.00",
        "description": (
            "Deep red and burgundy roses intertwined with dark calla lilies and velvety black-tipped tulips "
            "create an air of sophisticated mystery. Set against lush greenery and trailing ivy, this "
            "arrangement evokes moonlit gardens and whispered promises. Delivered in an elegant black matte "
            "vase, Midnight Romance is the ultimate statement for anniversaries, Valentine's Day, or any "
            "occasion that calls for passionate, unforgettable beauty."
        ),
    },
    {
        "id": 3,
        "name": "Spring Meadow",
        "price": "$40.00",
        "description": (
            "Celebrate the renewal of spring with a playful mix of lavender, pink peonies, white daisies, "
            "and cheerful yellow ranunculus. Each stem is carefully selected to mimic the natural scatter "
            "of wildflowers in a sunlit meadow. Arranged in a rustic ceramic pitcher, Spring Meadow brings "
            "the freshness of the outdoors inside. A beloved choice for Easter, Mother's Day, or a "
            "thoughtful housewarming gift."
        ),
    },
    {
        "id": 4,
        "name": "Ocean Breeze",
        "price": "$50.00",
        "description": (
            "Cool blue hydrangeas, soft white lilies, and sea-green succulents come together in a coastal "
            "palette that soothes the senses and calms the mind. Accented with silvery dusty miller and "
            "delicate blue thistle, Ocean Breeze evokes the feeling of standing at the shore with a gentle "
            "salt-scented wind in your hair. Presented in a driftwood-textured container, this arrangement "
            "suits beach lovers, nautical-themed spaces, or anyone craving a moment of serenity."
        ),
    },
    {
        "id": 5,
        "name": "Enchanted Forest",
        "price": "$55.00",
        "description": (
            "Step into a fairy tale with this lush woodland arrangement featuring deep green ferns, "
            "magenta orchids, white anemones, and clusters of berries nestled among moss and twigs. "
            "Enchanted Forest draws inspiration from ancient groves where magic feels close at hand. "
            "Housed in a weathered wooden box lined with burlap, it is a captivating choice for "
            "fantasy-themed events, autumn celebrations, or gifting to someone who loves nature's drama."
        ),
    },
    {
        "id": 6,
        "name": "Pastel Dream",
        "price": "$42.00",
        "description": (
            "Soft blush roses, mint green hydrangeas, pale peach carnations, and delicate white freesias "
            "blend into a dreamy watercolor palette. Pastel Dream is the embodiment of gentleness and "
            "grace, making it the perfect gift for baby showers, bridal brunches, or anyone who appreciates "
            "subtle elegance. Displayed in a frosted glass vase with a satin bow, this arrangement "
            "photographs beautifully and fills any room with a soft, sweet fragrance."
        ),
    },
    {
        "id": 7,
        "name": "Tropical Paradise",
        "price": "$65.00",
        "description": (
            "Transport yourself to an island getaway with bold birds-of-paradise, exotic anthuriums, "
            "bright orange ginger flowers, and broad tropical leaves. Every element of Tropical Paradise "
            "is chosen for its striking colour and dramatic silhouette. Arranged in a vibrant turquoise "
            "ceramic pot, this eye-catching display is perfect for luau parties, summer celebrations, "
            "corporate lobbies, or simply adding a burst of colour to any living space."
        ),
    },
    {
        "id": 8,
        "name": "Lavender Serenity",
        "price": "$38.00",
        "description": (
            "Fragrant bundles of true lavender are paired with soft purple statice, lilac stock, and "
            "wispy white gypsophila to create a calming, aromatic bouquet. Lavender Serenity is known "
            "for its stress-relieving scent and is often chosen as a wellness gift for someone going "
            "through a difficult time or needing a moment of peace. Presented in a woven basket with a "
            "purple velvet ribbon, it doubles as a charming home décor piece long after the blooms fade."
        ),
    },
    {
        "id": 9,
        "name": "Golden Harvest",
        "price": "$48.00",
        "description": (
            "Warm amber chrysanthemums, burnt-orange dahlias, russet marigolds, and sprigs of wheat "
            "capture the abundance and richness of autumn in a single breathtaking arrangement. Golden "
            "Harvest is ideal for Thanksgiving centerpieces, fall weddings, and harvest festivals. "
            "Nestled in a distressed copper tin bucket, this arrangement brings the colours of the season "
            "indoors with cosy, inviting warmth that guests will admire throughout the entire celebration."
        ),
    },
    {
        "id": 10,
        "name": "Cherry Blossom",
        "price": "$52.00",
        "description": (
            "Delicate pale pink cherry blossom branches arc gracefully above a bed of white ranunculus "
            "and blush sweet peas in this refined Japanese-inspired arrangement. Cherry Blossom celebrates "
            "the fleeting beauty of nature and the importance of cherishing each moment. Arranged in a "
            "tall, slender white ceramic vase, this piece brings zen-like tranquility to any space and "
            "makes an extraordinary gift for milestone birthdays or as a meaningful sympathy arrangement."
        ),
    },
    {
        "id": 11,
        "name": "Sunset Glow",
        "price": "$47.00",
        "description": (
            "Vibrant coral roses, tangerine gerberas, deep peach tulips, and fiery red dahlias are "
            "layered like the colours of a breathtaking evening sky in Sunset Glow. Accented with trails "
            "of golden foliage, this arrangement radiates warmth and vitality. Set in a terracotta pot, "
            "Sunset Glow is a perfect farewell gift, a cheerful congratulations present, or a brilliant "
            "way to decorate an outdoor evening reception or patio gathering."
        ),
    },
    {
        "id": 12,
        "name": "Winter Wonderland",
        "price": "$58.00",
        "description": (
            "Crisp white roses, silvery eucalyptus, frosted pine cones, and pearlescent ornament picks "
            "compose a magical holiday arrangement that captures the hush of a fresh snowfall. Winter "
            "Wonderland is nestled in a white birch-bark vase dusted with glitter, making it an "
            "exquisite centrepiece for Christmas dinners, holiday office parties, or a generous seasonal "
            "gift for a host or hostess. The refreshing scent of eucalyptus fills the room."
        ),
    },
    {
        "id": 13,
        "name": "Blushing Bride",
        "price": "$75.00",
        "description": (
            "Luxurious ivory garden roses, feathery white pampas grass plumes, champagne spray roses, "
            "and delicate pearl pins compose an arrangement fit for royalty. Blushing Bride is "
            "meticulously crafted for weddings, engagement parties, and bridal showers where only the "
            "finest will do. Arranged in a crystal-clear vase adorned with pearl-tipped pins, this "
            "arrangement exudes timeless romance and sophistication that photographs magnificently in "
            "every lighting condition."
        ),
    },
    {
        "id": 14,
        "name": "Wildflower Whisper",
        "price": "$36.00",
        "description": (
            "Loose and carefree, Wildflower Whisper features cosmos, Queen Anne's lace, purple liatris, "
            "ox-eye daisies, and trailing sweet peas bundled together as if freshly gathered from an "
            "open hillside. This honest, unpretentious arrangement celebrates the beauty of imperfection "
            "and is presented in a recycled mason jar tied with twine. It suits picnics, garden parties, "
            "informal gatherings, and gifts for the free-spirited soul who finds beauty in simplicity."
        ),
    },
    {
        "id": 15,
        "name": "Moody Mauve",
        "price": "$53.00",
        "description": (
            "Dusty mauve roses, plum lisianthus, smoky purple allium, and pale grey-green eucalyptus "
            "come together in a moody, editorial-inspired arrangement that feels both modern and timeless. "
            "Moody Mauve is a favourite among interior designers and style-forward gifters who want "
            "something beyond the ordinary. Presented in a matte charcoal concrete vessel, this "
            "arrangement suits loft apartments, creative offices, and sophisticated dinner party tables."
        ),
    },
    {
        "id": 16,
        "name": "Honeybee Garden",
        "price": "$39.00",
        "description": (
            "Cheerful yellow snapdragons, bright rudbeckia, creamy white cosmos, and honey-scented "
            "chamomile mimic the kind of garden that attracts bumblebees on warm afternoons. Honeybee "
            "Garden is lighthearted and full of charm, arranged in a sunny yellow ceramic pot painted "
            "with small bee motifs. It makes an excellent gift for gardening enthusiasts, nature lovers, "
            "teachers, or anyone who simply appreciates the simple pleasures of the natural world."
        ),
    },
    {
        "id": 17,
        "name": "Rose Royale",
        "price": "$70.00",
        "description": (
            "Fifty premium long-stemmed red roses arranged in a tight, opulent dome make an unmistakable "
            "declaration of love and devotion. Rose Royale uses only the finest garden roses sourced "
            "from premier growers, ensuring maximum bloom size, rich colour, and an intoxicating fragrance. "
            "Delivered in an oversized black hatbox lined with red satin, this arrangement is reserved "
            "for grand romantic gestures, milestone anniversaries, or when only the very best will convey "
            "your feelings."
        ),
    },
    {
        "id": 18,
        "name": "Citrus Burst",
        "price": "$44.00",
        "description": (
            "Zingy lemon-yellow tulips, bright lime-green button poms, vivid orange gerberas, and "
            "tangy kumquat branches create an arrangement as energising as freshly squeezed juice. "
            "Citrus Burst is designed to inject life and optimism into any environment — from kitchen "
            "tables to office reception desks. Housed in a striped ceramic pitcher in lemon and white, "
            "it is an uplifting gift for anyone who needs a dose of sunshine and positive energy."
        ),
    },
    {
        "id": 19,
        "name": "Midnight Orchid",
        "price": "$62.00",
        "description": (
            "Rare deep-purple Vanda orchids, near-black queen of night tulips, and velvety dark "
            "chocolate cosmos compose a striking, theatrical arrangement unlike anything found in "
            "a conventional florist. Midnight Orchid is bold, artful, and deliberately dramatic — a "
            "conversation piece that commands attention in any room. Presented in a tall smoke-grey "
            "cylindrical vase, it suits minimalist, contemporary, or avant-garde interior styles and "
            "makes an unforgettable gift for design-conscious recipients."
        ),
    },
    {
        "id": 20,
        "name": "Peony Paradise",
        "price": "$68.00",
        "description": (
            "An extravagant collection of fully bloomed blush, coral, and ivory peonies overflowing from "
            "a large cut-glass bowl creates pure romantic indulgence. Peony Paradise is the ultimate "
            "luxury arrangement for those who adore the lush, ruffled beauty of peonies at their most "
            "voluptuous peak. Accented with soft fern fronds and trails of jasmine, the fragrance alone "
            "is an experience. Available seasonally, making it a truly special and sought-after gift."
        ),
    },
    {
        "id": 21,
        "name": "Desert Rose",
        "price": "$46.00",
        "description": (
            "Terracotta-toned roses, sandy-pink proteas, pale cream leucadendron, and spiky green "
            "succulents evoke the stark, unexpected beauty of a desert in bloom after rain. Desert Rose "
            "celebrates resilience and quiet strength. Arranged in a raw, unglazed earthenware bowl, "
            "this arrangement suits bohemian, southwestern, and minimalist interior aesthetics. It is "
            "also wonderfully long-lasting, making it an excellent choice for home décor or gifting."
        ),
    },
    {
        "id": 22,
        "name": "Garden Party",
        "price": "$49.00",
        "description": (
            "A joyous celebration of colour featuring hot pink dahlias, violet lisianthus, yellow "
            "marigolds, and white snapdragons arranged with an abundant, overflowing abundance that "
            "feels like summer at its most festive. Garden Party is designed for outdoor celebrations, "
            "graduation parties, and bridal showers where the mood is bright and the laughter is loud. "
            "Presented in a vintage-inspired floral tin, the arrangement itself becomes a keepsake."
        ),
    },
    {
        "id": 23,
        "name": "Frosted Berry",
        "price": "$51.00",
        "description": (
            "White spray roses, iridescent dusty miller, clusters of silver-frosted berries, and "
            "pale blue delphiniums evoke the crystalline beauty of a winter morning when the world "
            "is still and frost covers every branch. Frosted Berry is elegant and serene, ideally "
            "suited to winter weddings, holiday tables, and as a sophisticated gift during the "
            "festive season. Arranged in a silver-lustre mercury glass vase, it catches and scatters "
            "candlelight in the most magical way."
        ),
    },
    {
        "id": 24,
        "name": "Sunflower Fields",
        "price": "$35.00",
        "description": (
            "A simple, honest bunch of oversized sunflowers with their broad, velvety faces turned "
            "toward the light epitomises summertime happiness. Sunflower Fields includes a dozen "
            "premium sunflowers of varying sizes, complemented by leafy green stems and tied with "
            "a cheerful striped ribbon. It is an uncomplicated, feel-good gift that brings instant "
            "cheer to any recipient — perfect for friends, family, or a spontaneous gesture of "
            "appreciation on any ordinary day."
        ),
    },
    {
        "id": 25,
        "name": "Lush Lotus",
        "price": "$57.00",
        "description": (
            "Graceful white lotus blossoms, floating on a shallow dish filled with smooth river "
            "stones and still water, create a meditative, spa-like centrepiece. Lush Lotus draws "
            "on the symbolism of purity and enlightenment found across Eastern traditions and is "
            "a deeply thoughtful gift for a yoga practitioner, wellness enthusiast, or anyone "
            "embarking on a new chapter in life. Complemented by bamboo stalks and trailing "
            "lily pads, this arrangement brings an unparalleled sense of calm to its surroundings."
        ),
    },
    {
        "id": 26,
        "name": "Fiesta Bloom",
        "price": "$43.00",
        "description": (
            "Red, orange, yellow, and magenta gerberas, marigolds, and zinnias explode with colour "
            "in an arrangement inspired by the vibrant festivals of Mexico. Fiesta Bloom is bold, "
            "lively, and impossible to ignore. Nestled in a hand-painted talavera-style ceramic pot, "
            "it brings festive energy to Cinco de Mayo parties, Day of the Dead altars, birthday "
            "tables, or any space that needs an injection of unapologetic colour and cultural spirit."
        ),
    },
    {
        "id": 27,
        "name": "Ivory Elegance",
        "price": "$66.00",
        "description": (
            "A restrained, impeccably curated palette of ivory roses, white calla lilies, cream "
            "freesias, and alabaster anemones achieves a standard of quiet luxury that speaks louder "
            "than colour ever could. Ivory Elegance is the choice of those who understand that "
            "understatement is the highest form of sophistication. Presented in a tall, fluted milk-glass "
            "vase, this arrangement is favoured for corporate gifting, sympathy tributes, upscale "
            "dinner parties, and formal weddings."
        ),
    },
    {
        "id": 28,
        "name": "Rainbow Riot",
        "price": "$41.00",
        "description": (
            "Why choose one colour when you can have all of them? Rainbow Riot is a joyful, inclusive "
            "explosion of every hue — red roses, orange tulips, yellow daffodils, green button poms, "
            "blue irises, indigo delphiniums, and violet lisianthus — celebrating the full spectrum "
            "of life's beauty. Perfect for Pride Month, a child's birthday, or anyone who believes "
            "that more colour is always better, Rainbow Riot arrives in a clear vase that lets every "
            "stem shine on its own."
        ),
    },
    {
        "id": 29,
        "name": "Secret Garden",
        "price": "$54.00",
        "description": (
            "Climbing roses in the softest blush, nodding foxglove spires, creeping sweet William, "
            "and trails of jasmine vine compose an arrangement that feels as though it was gathered "
            "from a hidden walled garden tucked behind an old estate. Secret Garden is romantic and "
            "literary, perfect for book lovers, Anglophiles, and dreamers. Presented in a vintage "
            "aged-terracotta pot wrapped in burlap, it evokes afternoons spent reading among roses "
            "with no obligations and all the time in the world."
        ),
    },
    {
        "id": 30,
        "name": "Azure Dream",
        "price": "$56.00",
        "description": (
            "Brilliant azure delphiniums, cornflower-blue bachelor's buttons, sky-blue hydrangeas, "
            "and pure white sweet alyssum create a bouquet as clear and boundless as an open sky on "
            "a perfect summer day. Azure Dream is a refreshing, optimistic arrangement that pairs "
            "beautifully with white linen tablecloths and natural wood surfaces. Presented in a "
            "classic blue-and-white toile ceramic pitcher, it suits coastal cottages, breezy summer "
            "homes, and anyone who finds their greatest happiness outdoors under an open sky."
        ),
    },
]


def home(request):
    return render(request, "boutique/home.html", {"products": PRODUCTS})


def product_detail(request, product_id):
    product = next((p for p in PRODUCTS if p["id"] == product_id), None)
    if product is None:
        from django.http import Http404
        raise Http404("Product not found")
    return render(request, "boutique/product_detail.html", {"product": product})

