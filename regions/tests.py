from django.test import TestCase
from regions.models import Region


class RegionTestCase(TestCase):
    def setUp(self):
        parent = Region.objects.create(name='ParentRegion', tag='PR')
        Region.objects.create(name="ChildRegion1", tag='CR1', parent_region=parent)
        Region.objects.create(name="ChildRegion2", tag='CR2', parent_region=parent)

    def test_has_tree_regions(self):
        regions = Region.objects.all()
        self.assertEqual(regions.count(), 3)

    def test_parent_region_has_two_child(self):
        self.assertEqual(Region.objects.filter(name='ParentRegion').first().child_regions.all().count(), 2)

    def test_parent_region_has_child_region_one(self):
        self.assertIsNotNone(Region.objects.filter(name='ParentRegion').first()
                             .child_regions.filter(name='ChildRegion1').first())

    def test_parent_region_has_child_region_two(self):
        self.assertIsNotNone(Region.objects.filter(name='ParentRegion').first()
                             .child_regions.filter(name='ChildRegion2').first())

    def test_child_region_one_has_parent_region(self):
        child_region1 = Region.objects.filter(name='ChildRegion1').first()
        self.assertIsNotNone(child_region1)
        self.assertEqual(child_region1.parent_region.name, 'ParentRegion')

    def test_child_region_two_has_parent_region(self):
        child_region2 = Region.objects.filter(name='ChildRegion2').first()
        self.assertIsNotNone(child_region2)
        self.assertEqual(child_region2.parent_region.name, 'ParentRegion')

    def test_parent_region_tag(self):
        self.assertTrue(Region.objects.filter(tag='PR').exists())

    def test_child_region_one_tag(self):
        self.assertTrue(Region.objects.filter(tag='CR1').exists())

    def test_child_region_two_tag(self):
        self.assertTrue(Region.objects.filter(tag='CR2').exists())

    def test_no_region_name_master_exist(self):
        self.assertFalse(Region.objects.filter(name='master').exists())

    def test_no_region_tag_mr_exist(self):
        self.assertFalse(Region.objects.filter(tag='mr').exists())
