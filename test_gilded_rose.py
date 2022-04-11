import unittest

from gilded_rose import ItemUpdate, GildedRose, Item

class GildedRoseTest(unittest.TestCase):
    def test_quality_day1(self):
        items = [ItemUpdate().update("Mulgore Spice Bread", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(19, items[0].quality)

    def test_sell_in_day1(self):
        items = [ItemUpdate().update("Mulgore Spice Bread", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].sell_in)

    def test_quality_reduces_at_50(self):
        items = [ItemUpdate().update("Mulgore Spice Bread", 10, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].sell_in)

    def test_quality_reduces_by2_when_expired(self):
        items = [ItemUpdate().update("Mulgore Spice Bread", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(18, items[0].quality)

    def test_quality_never_neg(self):
        items = [ItemUpdate().update("Mulgore Spice Bread", 10, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_sell_in_is_neg(self):
        items = [ItemUpdate().update("Mulgore Spice Bread", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)

    def test_aged_brie_increase_quality(self):
        items = [ItemUpdate().update("Aged Brie", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(21, items[0].quality)

    def test_quality_never_over_50(self):
        items = [ItemUpdate().update("Aged Brie", 10, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_sulfuras_never_sold(self):
        items = [ItemUpdate().update("Sulfuras, Hand of Ragnaros", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(10, items[0].sell_in)

    def test_sulfuras_quality_never_decreases(self):
        items = [ItemUpdate().update("Sulfuras, Hand of Ragnaros", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(20, items[0].quality)

    def test_backstage_quality_increase1_11days_remaining(self):
        items = [ItemUpdate().update("Backstage passes to a TAFKAL80ETC concert", 11, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(21, items[0].quality)

    def test_backstage_quality_increase2_10days_remaining(self):
        items = [ItemUpdate().update("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(22, items[0].quality)

    def test_backstage_quality_increase3_5days_remaining(self):
        items = [ItemUpdate().update("Backstage passes to a TAFKAL80ETC concert", 5, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(23, items[0].quality)

    def test_backstage_quality_increase3_2days_remaining(self):
        items = [ItemUpdate().update("Backstage passes to a TAFKAL80ETC concert", 2, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(23, items[0].quality)

    def test_backstage_quality_drop_to_zero(self):
        items = [ItemUpdate().update("Backstage passes to a TAFKAL80ETC concert", -1, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_backstage_quality_never_exceed_50(self):
        items = [ItemUpdate().update("Backstage passes to a TAFKAL80ETC concert", 10, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_conjured_quality(self):
        items = [ItemUpdate().update("Conjured Mana Cake", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(18, items[0].quality) #passes!

    def test_conjured_sell_in(self):
        items = [ItemUpdate().update("Conjured Mana Cake", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].sell_in) #passes
    
       
if __name__ == '__main__':
    unittest.main()