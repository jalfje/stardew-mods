import json
from enum import Enum
from collections import OrderedDict

# Run this script to generate a json with the replacement patches for each
# crop sprite. The sprite index of each overwritten sprite must be specified in the
# entries list for the given mod (see bottom of file for entries)
#
# Assumes that all sprites are the same size and that the replacement sprite sheet
# is the same size and has sprites in the same locations as the original sprite sheet.

class Special(Enum):
    NONE = 0
    UNPACKETED = 1
    SAPLING = 2

def generate_entry(
    target: str,
    from_file: str,
    sprite_size_px: int,
    sprites_per_row: int,
    sprite_index: int,
    entry_name: str,
    special: Special) -> OrderedDict:
    location = OrderedDict([
        ('X', (sprite_index % sprites_per_row) * sprite_size_px),
        ('Y', (sprite_index // sprites_per_row) * sprite_size_px),
        ('Width', sprite_size_px),
        ('Height', sprite_size_px)
    ])

    when = None
    if special == Special.UNPACKETED:
        when = ('When', OrderedDict([
            ('All Seeds Have Packets', True)
        ]))
    if special == Special.SAPLING:
        when = ('When', OrderedDict([
            ('Seasonal Saplings', True)
        ]))

    results = [
        ('$comment', entry_name),
        ('Action', 'EditImage'),
        ('PatchMode', 'Replace'),
        ('Target', target),
        ('FromFile', from_file),
        ('FromArea', location),
        ('ToArea', location)
    ]
    if when:
        results.insert(1, when)

    return OrderedDict(results)


def generate_all_entries(data: dict):
    return [
        generate_entry(
            target=data['target'], 
            from_file=data['from_file'],
            sprite_size_px=data['sprite_size_px'],
            sprites_per_row=data['sprites_per_row'],
            sprite_index=sprite_index,
            entry_name=entry_name,
            special=rest[0] if len(rest) > 0 else Special.NONE
        )
        for entry_name, sprite_index, *rest in data['entries']
    ]

def create_json(data: dict):
    entries_json = {'Changes': generate_all_entries(data)}
    with open(data['out_file'], mode='wt', newline='\n') as f:
        json.dump(entries_json, f, indent=4)
        f.write('\n')

vanilla_data = {
    'out_file': 'src/Vanilla/data/springobjects.json',
    'target': 'Maps/springobjects',
    'from_file': 'Vanilla/assets/springobjects.png',
    'sprite_size_px': 16,
    'sprites_per_row': 24,
    'entries': [
        ('Banana Sapling', 69, Special.SAPLING),
        ('Cherry Sapling', 628, Special.SAPLING),
        ('Apricot Sapling', 629, Special.SAPLING),
        ('Orange Sapling', 630, Special.SAPLING),
        ('Peach Sapling', 631, Special.SAPLING),
        ('Pomegranate Sapling', 632, Special.SAPLING),
        ('Apple Sapling', 633, Special.SAPLING),
        ('Mango Sapling', 835, Special.SAPLING)
    ]
}

# TODO: Replace grape starter via an objectsreplacement.json and cmct
more_crops_data = {
    'out_file': 'src/CornucopiaMoreCrops/data/objects.json',
    'target': 'Cornucopia.MoreCrops/Objects',
    'from_file': 'CornucopiaMoreCrops/assets/objects.png',
    'sprite_size_px': 16,
    'sprites_per_row': 20,
    'entries': [
        # NB grape starter won't work because it isn't loaded the same way
        ('Grape Starter', 3),
        # 110 total
        ('Basil', 195),
        ('Bell Pepper', 9),
        ('Turnip', 141),
        ('Cotton Boll', 15),
        ('Cucumber', 13),
        ('Kiwi', 183),
        ('Lettuce', 123),
        ('Olive', 267),
        ('Onion', 17),
        ('Peanut', 23),
        ('Raspberry', 25),
        ('Spinach', 83),
        ('Sugarcane', 31, Special.UNPACKETED),
        ('Watermelon', 11),
        ('Zucchini', 121),
        ('Vanilla', 271),
        ('Peppercorn', 191),
        ('Adzuki Bean', 89),
        ('Agave', 77),
        ('Asparagus', 155),
        ('Bamboo', 97, Special.UNPACKETED),
        ('Barley', 99),
        ('Black Bean', 151),
        ('Black Currants', 71),
        ('Blue Agave', 79),
        ('Buckwheat', 125),
        ('Butternut Squash', 127),
        ('Cabbage', 7),
        ('Canary Melon', 5),
        ('Canola Flower', 157, Special.UNPACKETED),
        ('Cantaloupe', 129),
        ('Cassava', 19),
        ('Celery', 29),
        ('Chicken of the Woods', 39),
        ('Chickpea', 63),
        ('Daikon', 143),
        ('Durum', 185),
        ('Elderberries', 81),
        ('Ginseng', 135),
        ('Gooseberry', 69),
        ('Green Peas', 91),
        ('Groundcherries', 265),
        ('Habanero', 189),
        ('Honeydew', 131),
        ('Jalapeno', 93),
        ('Juniper Berries', 27),
        ('Kidney Beans', 153),
        ('Navy Beans', 149),
        ('Oats', 61),
        ('Okra', 133),
        ('Passionfruit', 87),
        ('Pinto Beans', 147),
        ('Quinoa', 159),
        ('Red Onion', 181),
        ('Shallot', 73),
        ('Shiitake', 37),
        ('Sugar Beet', 85),
        ('Sweet Potato', 33),
        ('Wasabi Root', 137, Special.UNPACKETED),
        ('White Grape (Planter)', 75),
        ('White Grape (Bush)', 95),
        ('Aloe', 215),
        ('Bay Leaves', 213),
        ('Catnip', 207),
        ('Chives', 193),
        ('Cilantro', 217),
        ('Dill', 241),
        ('Fennel', 209),
        ('Fenugreek', 243),
        ('Lemongrass', 255),
        ('Licorice Root', 253),
        ('Marjoram', 257),
        ('Mint', 199),
        ('Oregano', 251),
        ('Parsley', 201),
        ('Perilla Leaves', 205),
        ('Rosemary', 203),
        ('Sage', 197),
        ('Tarragon', 245),
        ('Thyme', 211),
        ('Tumeric', 247),
        ('Wormwood', 249),
        ('Avocado Sapling', 375, Special.SAPLING),
        ('Cocoa Pod Sapling', 383, Special.SAPLING),
        ('Pear Sapling', 371, Special.SAPLING),
        ('Pistachio Sapling', 397, Special.SAPLING),
        ('Almond Sapling', 385, Special.SAPLING),
        ('Breadfruit Sapling', 429, Special.SAPLING),
        ('Cashew Sapling', 387, Special.SAPLING),
        ('Dragonfruit Sapling', 373, Special.SAPLING),
        ('Durian Sapling', 427, Special.SAPLING),
        ('Fig Sapling', 369, Special.SAPLING),
        ('Grapefruit Sapling', 425, Special.SAPLING),
        ('Lemon Sapling', 367, Special.SAPLING),
        ('Lime Sapling', 379, Special.SAPLING), 
        ('Lychee Sapling', 431, Special.SAPLING),
        ('Nectarine Sapling', 381, Special.SAPLING),
        ('Papaya Sapling', 363, Special.SAPLING),
        ('Pecan Sapling', 421, Special.SAPLING),
        ('Persimmon Sapling', 377, Special.SAPLING),
        ('Plaintain Sapling', 395, Special.SAPLING),
        ('Pomelo Sapling', 423, Special.SAPLING),
        ('Ume Sapling', 393, Special.SAPLING),
        ('Walnut Sapling', 389, Special.SAPLING),
        ('Yuzu Sapling', 391, Special.SAPLING),
        ('Camphor Leaves Sapling', 435, Special.SAPLING),
        ('Cinnamon Sticks Sapling', 399, Special.SAPLING),
        ('Eucalyptus Leaves Sapling', 439, Special.SAPLING),
        ('Melaleuca Leaves Sapling', 441, Special.SAPLING),
        ('Nutmeg Sapling', 437, Special.SAPLING)
    ]
}

more_flowers_data = {
    'out_file': 'src/CornucopiaMoreFlowers/data/objects.json',
    'target': 'Cornucopia.MoreFlowers/Objects',
    'from_file': 'CornucopiaMoreFlowers/assets/objects.png',
    'sprite_size_px': 16,
    'sprites_per_row': 20,
    'entries': [
        # 48 total
        ('Blue Mist', 3),
        ('Chrysanthemum', 148),
        ('Iris', 37),
        ('Lily', 125),
        ('Lotus', 35, Special.UNPACKETED),
        ('Morning Glory', 33),
        ('Orchid', 131),
        ('Pansy', 154),
        ('Pink Cat', 13),
        ('Rose', 122),
        ('Bee Balm', 9),
        ('Blue Bonnet', 39),
        ('Buttercup', 27),
        ('Calico Rose', 87, Special.UNPACKETED),
        ('Camellia', 31),
        ('Carnation', 134),
        ('Chamomile', 5),
        ('Clary Sage', 7),
        ('Clematis', 25),
        ('Dahlia', 145),
        ('Daisy', 29),
        ('Fairy Duster', 19),
        ('Fall Rose', 75),
        ('Freesia', 151), 
        ('Geranium', 69),
        ('Honeysuckle', 21),
        ('Hyacinth', 128),
        ('Hydrangea', 157),
        ('Larkspur', 137),
        ('Lavender', 15),
        ('Lilac', 81),
        ('Lupine', 142),
        ('Peony', 67),
        ('Petunia', 65),
        ('Pitcher Plant', 63, Special.UNPACKETED),
        # ('Prismatic Rose', 79), # This has a special packet that we don't overwrite
        ('Purple Coneflower', 23),
        ('Rafflessia', 61),
        ('Spring Rose', 71),
        ('Summer Rose', 73),
        ('Violet', 11),
        ('Winter Rose', 77),
        ('Wolfsbane', 85),
        ('Hibiscus Sapling', 263, Special.SAPLING),
        ('Jasmine Sapling', 265, Special.SAPLING),
        ('Magnolia Sapling', 261, Special.SAPLING),
        ('Wisteria Sapling', 269, Special.SAPLING),
        ('Ylang Ylang Sapling', 267, Special.SAPLING)
    ]
}

# TODO: Replace modified bushes via an objectsreplacement.json and cmct
growable_forage_and_crop_bushes_data = {
    'out_file': 'src/GrowableForageAndCropBushes/data/objects.json',
    'target': 'Cornucopia.GrowableForage/objects',
    'from_file': 'GrowableForageAndCropBushes/assets/objects.png',
    'sprite_size_px': 16,
    'sprites_per_row': 10,
    'entries': [
        ('Spring Onion', 2),
        ('Ginger', 3),
        ('Sweet Pea', 4),
        ('Crocus', 5),
        ('Common Mushroom', 10),
        ('Chanterelle', 11),
        ('Morel', 12),
        ('Salmonberry', 13),
        ('Blackberry', 14),
        ('Holly', 15),
        ('Coconut Sapling', 8, Special.SAPLING),
        ('Hazelnut Sapling', 9, Special.SAPLING)
    ]
}

vanilla_forage_crops_and_bushes_data = {
    'out_file': 'src/VanillaForageCropsAndBushes/data/objects.json',
    'target': 'ZoeyHoshi.ForageCrops/Objects',
    'from_file': 'VanillaForageCropsAndBushes/assets/objects.png',
    'sprite_size_px': 16,
    'sprites_per_row': 6,
    'entries': [
        ('Cave Carrot', 0),
        ('Daffodil', 1),
        ('Dandelion', 2),
        ('Leek', 3),
        ('Wild Horseradish', 4),
        ('Fiddlehead Fern', 5),
        ('Snow Yam', 6),
        ('Winter Root', 7),
        ('Seaweed', 8),
        ('Red Mushroom', 9),
        ('Spice Berry', 10),
        ('Purple Mushroom', 11),
        ('Crystal Fruit', 12),
        ('Magma Cap', 13),
        ('Wild Plum Sapling', 14, Special.SAPLING)
    ]
}

create_json(vanilla_data)
create_json(more_crops_data)
create_json(more_flowers_data)
create_json(growable_forage_and_crop_bushes_data)
create_json(vanilla_forage_crops_and_bushes_data)
