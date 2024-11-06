import pytest
from src.gilded_rose.main import Item, GildedRose

def test_normal_item_before_sell_date():
    items = [Item("normal", 5, 10)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 9
    assert items[0].sell_in == 4

def test_normal_item_on_sell_date():
    items = [Item("normal", 0, 10)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 9

def test_normal_item_after_sell_date():
    items = [Item("normal", -5, 10)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 8
    assert items[0].sell_in == -6

def test_normal_item_zero_quality():
    items = [Item("normal", 5, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 0

def test_aged_brie_before_sell_date():
    items = [Item("Aged Brie", 5, 10)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 11
    assert items[0].sell_in == 4

def test_aged_brie_with_max_quality():
    items = [Item("Aged Brie", 5, 50)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 50

def test_aged_brie_passes_max_quality():
    items = [Item("Aged Brie", 5, 49)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 50

def test_sulfuras_never_changes():
    items = [Item("Sulfuras, Hand of Ragnaros", 5, 80)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 80
    assert items[0].sell_in == 5

def test_backstage_passes_long_before_concert():
    items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 10)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 11

def test_backstage_passes_medium_close_to_concert():
    items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 10)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 12

def test_backstage_passes_very_close_to_concert():
    items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 10)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 13

def test_backstage_passes_after_concert():
    items = [Item("Backstage passes to a TAFKAL80ETC concert", -1, 10)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 0

def test_backstage_passes_max_quality():
    items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 49)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 50

def test_conjured_before_sell_date():
    items = [Item("Conjured", 5, 10)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 8

def test_conjured_after_sell_date():
    items = [Item("Conjured", -1, 10)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 6

def test_multiple_items():
    items = [
        Item("normal", 5, 10),
        Item("Aged Brie", 5, 10),
        Item("Sulfuras, Hand of Ragnaros", 5, 80),
        Item("Backstage passes to a TAFKAL80ETC concert", 5, 10),
        Item("Conjured", 5, 10)
    ]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 9  # normal
    assert items[1].quality == 11  # aged brie
    assert items[2].quality == 80  # sulfuras
    assert items[3].quality == 13  # backstage passes
    assert items[4].quality == 8   # conjured
