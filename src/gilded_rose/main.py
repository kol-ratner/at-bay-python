class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue
            
            self._update_item_quality(item)
            self._update_sell_in(item)

    def _update_sell_in(self, item):
        item.sell_in -= 1

    def _update_item_quality(self, item):
        if item.name == "Aged Brie":
            self._update_aged_brie(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            self._update_backstage_passes(item)
        elif item.name == "Conjured":
            self._update_conjured(item)
        else:
            self._update_normal_item(item)

    def _update_aged_brie(self, item):
        if item.quality < 50:
            # as a default we add 1 quality each iteration
            item.quality += 1
            # in that same iteration if the sell_in is < 0, then we tack on another quality point 
            # resulting in 2 total quality points
            if item.sell_in < 0:
                item.quality += 1

    def _update_backstage_passes(self, item):
        if item.sell_in < 0:
            item.quality = 0
            return

        if item.quality < 50:
            # as a default we add 1 quality each iteration
            item.quality += 1
            # in that same iteration if the sell_in is < 11, then we tack on another quality point 
            # resulting in 2 additional quality points total
            if item.sell_in < 11 and item.quality < 50:
                item.quality += 1
            # in that same iteration if the sell_in is < 6, then we tack on yet another quality point 
            # resulting in 3 additional quality points total
            if item.sell_in < 6 and item.quality < 50:
                item.quality += 1

    def _update_conjured(self, item):
        if item.quality > 0:
            # setting standard degredation of quality
            quality_decrease = 2
            # doubling standard degredation of quality of sell_in < 0
            if item.sell_in < 0:
                quality_decrease *= 2
            # as long as the quality value is positive, 
            # then we subtract the quality_decrease value from the quality
            item.quality = item.quality - quality_decrease

    def _update_normal_item(self, item):
        if item.quality > 0:
            # setting standard degredation of quality
            quality_decrease = 1
            # doubling standard degredation of quality of sell_in < 0
            if item.sell_in < 0:
                quality_decrease *= 2
            
            # as long as the quality value is positive, 
            # then we subtract the quality_decrease value from the quality
            item.quality = item.quality - quality_decrease


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
