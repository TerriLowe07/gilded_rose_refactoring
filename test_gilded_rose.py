import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_quality_day1(self):
        items = [Item("Mulgore Spice Bread", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(19, items[0].quality)

    def test_sell_in_day1(self):
        items = [Item("Mulgore Spice Bread", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(9, items[0].sell_in)

    def test_quality_reduces_by2_when_expired(self):
        items = [Item("Mulgore Spice Bread", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(18, items[0].quality)

    def test_quality_never_neg(self):
        items = [Item("Mulgore Spice Bread", 10, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)

    def test_sell_in_is_neg(self):
        items = [Item("Mulgore Spice Bread", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(-1, items[0].sell_in)

    def test_aged_brie_increase_quality(self):
        items = [Item("Aged Brie", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(21, items[0].quality)

    def test_quality_never_over_50(self):
        items = [Item("Aged Brie", 10, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)

    def test_sulfuras_never_sold(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(10, items[0].sell_in)

    def test_sulfuras_quality_never_decreases(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(20, items[0].quality)

    def test_passes_quality_increase2_10days_remaining(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(22, items[0].quality)

    def test_passes_quality_increase1_11days_remaining(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(21, items[0].quality)

    def test_passes_quality_increase3_5days_remaining(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(23, items[0].quality)

    def test_passes_quality_increase3_2days_remaining(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 2, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(23, items[0].quality)

    def test_passes_quality_drop_to_zero(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", -1, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)

    def test_passes_quality_never_exceed_50(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)

    def test_conjured_quality(self):
        items = [Item("Conjured Mana Cake", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(18, items[0].quality)

    def test_conjured_sell_in(self):
        items = [Item("Conjured Mana Cake", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(9, items[0].sell_in)

    
    

        
if __name__ == '__main__':
    unittest.main()