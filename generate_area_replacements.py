import json
from collections import OrderedDict

# Run this script to generate a json with the replacement patches for each
# crop sprite. The sprite index of each overwritten sprite must be specified in the
# entries list for the given mod (see bottom of file for entries)
#
# Assumes that all sprites are the same size and that the replacement sprite sheet
# is the same size and has sprites in the same locations as the original sprite sheet.

def generate_entry(
    target: str,
    from_file: str,
    sprite_size_px: int,
    sprites_per_row: int,
    sprite_index: int,
    entry_name: str) -> OrderedDict:
    location = OrderedDict([
        ('X', (sprite_index % sprites_per_row) * sprite_size_px),
        ('Y', (sprite_index // sprites_per_row) * sprite_size_px),
        ('Width', sprite_size_px),
        ('Height', sprite_size_px)
    ])
    return OrderedDict([
        ('$comment', entry_name),
        ('Action', 'EditImage'),
        ('PatchMode', 'Replace'),
        ('Target', target),
        ('FromFile', from_file),
        ('FromArea', location),
        ('ToArea', location)
    ])

def generate_all_entries(data: dict):
    return [
        generate_entry(
            target=data['target'], 
            from_file=data['from_file'],
            sprite_size_px=data['sprite_size_px'],
            sprites_per_row=data['sprites_per_row'],
            sprite_index=sprite_index,
            entry_name=entry_name
        )
        for entry_name, sprite_index in data['entries']
    ]

def create_json(data: dict, out_file: str):
    entries_json = {"Changes": generate_all_entries(data)}
    with open(out_file, mode="wt") as f:
        json.dump(entries_json, f, indent=4)


more_crops_data = {
    "target": "Cornucopia.MoreCrops/Objects",
    "from_file": "CornucopiaMoreCrops/assets/objects.png",
    "sprite_size_px": 16,
    "sprites_per_row": 20,
    "entries": [
        # NB grape starter won't work because it isn't loaded the same way
        ("Grape Starter", 3),
        # 110 total
        ("Basil", 195),
        ("Bell Pepper", 9),
        ("Turnip", 141),
        ("Cotton Boll", 15),
        ("Cucumber", 13),
        ("Kiwi", 183),
        ("Lettuce", 123),
        ("Olive", 267),
        ("Onion", 17),
        ("Peanut", 23),
        ("Raspberry", 25),
        ("Spinach", 83),
        ("Sugarcane", 31),
        ("Watermelon", 11),
        ("Zucchini", 121),
        ("Vanilla", 271),
        ("Peppercorn", 191),
        ("Adzuki Bean", 89),
        ("Agave", 77),
        ("Asparagus", 155),
        ("Bamboo", 97),
        ("Barley", 99),
        ("Black Bean", 151),
        ("Black Currants", 71),
        ("Blue Agave", 79),
        ("Buckwheat", 125),
        ("Butternut Squash", 127),
        ("Cabbage", 7),
        ("Canary Melon", 5),
        ("Canola Flower", 157),
        ("Cantaloupe", 129),
        ("Cassava", 19),
        ("Celery", 29),
        ("Chicken of the Woods", 39),
        ("Chickpea", 63),
        ("Daikon", 143),
        ("Durum", 185),
        ("Elderberries", 81),
        ("Ginseng", 135),
        ("Gooseberry", 69),
        ("Green Peas", 91),
        ("Groundcherries", 265),
        ("Habanero", 189),
        ("Honeydew", 131),
        ("Jalapeno", 93),
        ("Juniper Berries", 27),
        ("Kidney Beans", 153),
        ("Navy Beans", 149),
        ("Oats", 61),
        ("Okra", 133),
        ("Passionfruit", 87),
        ("Pinto Beans", 147),
        ("Quinoa", 159),
        ("Red Onion", 181),
        ("Shallot", 73),
        ("Shiitake", 37),
        ("Sugar Beet", 85),
        ("Sweet Potato", 33),
        ("Wasabi Root", 137),
        ("White Grape (Planter)", 75),
        ("White Grape (Bush)", 95),
        ("Aloe", 215),
        ("Bay Leaves", 213),
        ("Catnip", 207),
        ("Chives", 193),
        ("Cilantro", 217),
        ("Dill", 241),
        ("Fennel", 209),
        ("Fenugreek", 243),
        ("Lemongrass", 255),
        ("Licorice Root", 253),
        ("Marjoram", 257),
        ("Mint", 199),
        ("Oregano", 251),
        ("Parsley", 201),
        ("Perilla Leaves", 205),
        ("Rosemary", 203),
        ("Sage", 197),
        ("Tarragon", 245),
        ("Thyme", 211),
        ("Tumeric", 247),
        ("Wormwood", 249),
        ("Avocado Sapling", 375),
        ("Cocoa Pod Sapling", 383),
        ("Pear Sapling", 371),
        ("Pistachio Sapling", 397),
        ("Almond Sapling", 385),
        ("Breadfruit Sapling", 429),
        ("Cashew Sapling", 387),
        ("Dragonfruit Sapling", 373),
        ("Durian Sapling", 427),
        ("Fig Sapling", 369),
        ("Grapefruit Sapling", 425),
        ("Lemon Sapling", 367),
        ("Lime Sapling", 379), 
        ("Lychee Sapling", 431),
        ("Nectarine Sapling", 381),
        ("Papaya Sapling", 363),
        ("Pecan Sapling", 421),
        ("Persimmon Sapling", 377),
        ("Plaintain Sapling", 395),
        ("Pomelo Sapling", 423),
        ("Ume Sapling", 393),
        ("Walnut Sapling", 389),
        ("Yuzu Sapling", 391),
        ("Camphor Leaves Sapling", 435),
        ("Cinnamon Sticks Sapling", 399),
        ("Eucalyptus Leaves Sapling", 439),
        ("Melaleuca Leaves Sapling", 441),
        ("Nutmeg Sapling", 437)
    ]
}

more_flowers_data = {
    "target": "Cornucopia.MoreFlowers/Objects",
    "from_file": "CornucopiaMoreFlowers/assets/objects.png",
    "sprite_size_px": 16,
    "sprites_per_row": 20,
    "entries": [
        # 48 total
        ("Blue Mist", 3),
        ("Chrysanthemum", 148),
        ("Iris", 37),
        ("Lily", 125),
        ("Lotus", 35),
        ("Morning Glory", 33),
        ("Orchid", 131),
        ("Pansy", 154),
        ("Pink Cat", 13),
        ("Rose", 122),
        ("Bee Balm", 9),
        ("Blue Bonnet", 39),
        ("Buttercup", 27),
        ("Calico Rose", 87),
        ("Camellia", 31),
        ("Carnation", 134),
        ("Chamomile", 5),
        ("Clary Sage", 7),
        ("Clematis", 25),
        ("Dahlia", 145),
        ("Daisy", 29),
        ("Fairy Duster", 19),
        ("Fall Rose", 75),
        ("Freesia", 151), 
        ("Geranium", 69),
        ("Honeysuckle", 21),
        ("Hyacinth", 128),
        ("Hydrangea", 157),
        ("Larkspur", 137),
        ("Lavender", 15),
        ("Lilac", 81),
        ("Lupine", 142),
        ("Peony", 67),
        ("Petunia", 65),
        ("Pitcher Plant", 63),
        ("Prismatic Rose", 79),
        ("Purple Coneflower", 23),
        ("Rafflessia", 61),
        ("Spring Rose", 71),
        ("Summer Rose", 73),
        ("Violet", 11),
        ("Winter Rose", 77),
        ("Wolfsbane", 85),
        ("Hibiscus Sapling", 263),
        ("Jasmine Sapling", 265),
        ("Magnolia Sapling", 261),
        ("Wisteria Sapling", 269),
        ("Ylang Ylang Sapling", 267)
    ]
}

create_json(more_crops_data, "./CornucopiaMoreCrops/objects.json")
create_json(more_flowers_data, "./CornucopiaMoreFlowers/objects.json")