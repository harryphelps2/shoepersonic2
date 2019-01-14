from django.test import TestCase
from .views import decide_weekly_running_volume
# Create your tests here.


class TrainTests(TestCase):
    """
    Tests for generating a training plan.
    """
    def test_decide_weekly_running_volume(self):

        self.assertEqual(decide_weekly_running_volume("beginner", "5k"), 30)
        self.assertEqual(decide_weekly_running_volume("low-key competitive", "5k"), 35)
    
    # def test_add_to_basket_happy_path(self):
    #     shoe = Shoe.objects.create(id=1, brand='Best Brand', name='Top Shoe', colour='Red', price=500)

    #     client = Client()

    #     # View the product page
    #     response = client.get('/shop/shoe_detail/{0}/'.format(shoe.id))
    #     self.assertEqual(response.status_code, 200)

    #     # Add product to the basket
    #     response = client.post('/basket/add/{0}/'.format(shoe.id), {
    #         'quantity': 1,
    #         'size': 10,
    #     })
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, '/basket/')
    #     self.assertEqual(client.session['basket'], {'1-10': {'quantity': 1, 'size': '10'}})

    #     # View basket page
    #     response = client.get('/basket/')
    #     self.assertContains(response, shoe.name, status_code=200)

    # def test_checkout_happy_path(self):
    #     # Create shoe
    #     shoe = Shoe.objects.create(brand='Best Brand', name='Top Shoe', colour='Red', price=500)
    #     # Create browser
    #     client = Client()

    #     # Create cart
    #     session = client.session
    #     session['basket'] = {'1-10': {'quantity': 1, 'size': '10'}}
    #     session.save()
        
    #     # Go to checkout contact details page
    #     response = client.get('/checkout/contact_details')
    #     self.assertEqual(response.status_code, 200)

    #     # Collect contact details to session
    #     response = client.post('/checkout/contact_details',{
    #         'email': 'happy@path.com',
    #         'running_club': 'HAPZ'
    #     })
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, '/checkout/delivery_details')
    #     self.assertEqual(client.session['email'], 'happy@path.com')
    #     self.assertEqual(client.session['running_club'], 'HAPZ')

    #     # Collect delivery details
    #     response = client.get('/checkout/delivery_details')
    #     self.assertEqual(response.status_code, 200)

    #     # Collect delivery details
    #     response = client.post('/checkout/delivery_details',{
    #         'first_name': 'happy',
    #         'last_name': 'path',
    #         'address_line_1':'1 happy street',
    #         'postcode':'ha4 4py'
    #     })
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, '/checkout/card_details')
    #     self.assertEqual(client.session['first_name'], 'happy')
    #     self.assertEqual(client.session['last_name'], 'path')
    #     self.assertEqual(client.session['address_line_1'], '1 happy street')
    #     self.assertEqual(client.session['postcode'], 'ha4 4py')
