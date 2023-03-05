from django.test import TestCase
from django.contrib.auth.models import User
from store.models import Product, Comment, Subcategory, Category, Profile, Order, OrderItem

class TestModel(TestCase):

    def setUp(self):
        user = User.objects.create(username='sda')
        user.set_password('12345')
        user.save()

        self.profile = Profile.objects.create(
            user=user,
            street='1.avenue',
            number='5',
            post_code='00-000',
            city='N.Y',
            phone_number=2222,
            info='')

        self.order = Order.objects.create(
            profile=self.profile,
            complete=True)

        self.category = Category.objects.create(
            name='TV')

        self.subcategory = Subcategory.objects.create(
            name='TV Set',
            category=self.category)

        self.product = Product.objects.create(
            name='product1',
            description='product1',
            subcategory=self.subcategory,
            price=1000)

        self.orderitem = OrderItem.objects.create(
            product=self.product,
            order=self.order,
            quantity = 8)

        self.comment = Comment.objects.create(
            product=self.product,
            title='super',
            comment='super',
            score=5)

    def test_score_validation(self):
        self.assertEqual(self.product.get_total_score, 5)

    def test_orderitem_get_total(self):
        self.assertEqual(self.orderitem.get_total, 8000)





