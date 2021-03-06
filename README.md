# Full Stack Development Milestone Project - Shoepersonic.com

[![Build Status](https://travis-ci.org/harryphelps2/shoepersonic2.svg?branch=master)](https://travis-ci.org/harryphelps2/shoepersonic2)

Link to live site: https://shoepersonic2.herokuapp.com/

## Business Objectives

Sell shoes to people like Derek (see below).

## Customer Profile, Derek from London:

Grew up in London, enjoys running as a project on the side to stay healthy, relieve stress and compete. Derek was never a talented athlete but he enjoys training to compete in races now he is independent and working. He did a degree in mechanical engineering and ran in a club at school and tried out numerous individual sports at university. David struggles with confidence around other men and women and enjoys running. He likes feeling part of a club but struggles to break through into the social side of things. He really wants to be invited to the party but feels like he is never engaging enough or gregarious enough to break into the cool crowd. 

He doesn’t mind spending money on his hobby but is time poor. He makes decisions quickly and likes to assimilate all the information he can in one place to make the right choice. He doesn't have time to search lots of sites to decide what the best thing to do is. 

He has a reasonable amount of speed and believes if he stuck to running and had more time to train he could really excel. 

He hates ignorance. His science background has given him a healthy sense of 'I know better'. He always feels slightly outside the mainstream, slightly ahead of he curve.  He talks to other runners about new training techniques but they don’t know what he is talking about. 

He loves learning about running  but can’t find anyone to talk about it with. He doesn’t need running shoes that are supportive or gimmicky he looks for running shoes that are light and look good so when he turns up on the start like he feels like the real deal. He likes encouragement. Often described as stoic, he has learned to work hard. He wants to be recognised for what talent he has. He is not the most genetically gifted athlete and that plays on his mind. He believes hard work will pay off and wants to see how far he can take running.

He gets nervous about racing and likes to research the races before he goes. He wants to learn more about race tactics elevation and ground quality. He likes to see things up-close. Tne more detail Derek can get about a prospective pruchase the more it draws him in. He finds buying shoes online stressful as you can't try them on and wants to know what they are like to run in.

## UX

The user should be able to:

1. Choose a shoe to view in more detail.

2. Choose a size and quantity and add to the basket.

3. View the basket and total price before choosing to buy.

4. Choose to purchase and be able to input contact details.

5. Add delivery details.

6. Add card details and make purchase.

7. Be able to save details for next time.

8. Access detailed reviews of the shoes before making a decision.

9. See the shoes in action.

10. Find out how to return them if they are not right.

11. Comment on reviews.

12. Edit your comment.

13. Delete comment.

The shoe shop owner should be able to:

1. Enforce the terms and conditions in order for the customer to make a purchase

2. Be able to control and edit stock levels so that a customer cannot purchase something that is not in stock.

## Features

### Views

The site has ben designed for mobile first.

1. Base page, navbar and footer - The base page allows the site designer to change the title page and meta description with block tags to match chosen keywords and improve search engine performance. The navbar collapses at smaller screen sizes. The footer contains social media links that highlight in the colour of the brand when hovered over.

2. Landing page - The user is presented with a big hero image, with the brand and strapline to welcome the customer in. Scrolling down the customer can see a summary of the what the site does with icons. The hero image has a call-to-action 'SHOP NOW' red button to invite the customer to view the product page. The font sizes and icons adjust for larger screens.

3. Product Page - Clicking through to the product page the customer can see all 5 shoes with a summary of their features. The number of cards per row adjusts with screen size.

4. Shoe detail page - This page has a height-responsive touch screen compatible carousel of product images. The customer can select a size from the drop down which tells them how many of each shoe is left. The customer can also increase and decrease the quantity which uses jquery to update the quantity number in the DOM when the button is clicked. The user then clicks add to basket and the size, quantity and product are added to the session storage.

5. Basket - The Basket page shows all the products added so far and their total. The customer can update the quantity of the shoe by clicking the plus and minus buttons either side of the quantity number. (BUG: If there is more than one pair of shoes in the basket the quantity updater will always update the top one. This bug was discovered too late to fix, but it is assumed most customers will only purchase the one pair of shoes. The bug will get fixed early next year.) The customer selects checkout and goes to the contact details page.

6. Contact details - The user has to add an email so we can contact them about the order and can also add a running club. If they do 5% of the profits from their purchase will be donated to that running club. The delivery and payment tabs are disabled.

7. Delivery Details - User adds address to send shoes to. The payment tab is disabled but the contact details tab is linked so the customer can navigate backwards.

8. Card details - User uses stripe input to send card details. The site utilises Stripes capt and auth functionality to reserve the funds on the account but not take them. This gives the shop-owner a chance to check they are in stock before accepting the order and taking the money, instead of having to refund if the shoes aren't in stock. The delivery and contact details tabs are linked.

9. Order confirmation - The customer is shown their order number and is asked if they want to create a password to save details for next time. The stock number of the shoe size decrease by 1.

10. Review page with comparative shoe review - The user can see all 5 shoes compared with an embedded youtube video with montage.

11. The Hangar (blog page with links to articles) - The user can browse articles about running. Each article links back to a shoe.

12. Delivery and Returns information

13. Profile page - list of previous orders and current profile information. A link for each order takes the customer through to the returns page.

### Data

1. Shoe - A shoe is a brand and model of shoe including various attributes such as weight and colour. Each shoe includes a primary image.

2. Stock - Each shoe has a stock entry for each size.

3. Order - And order is an address and email of a customer who has made an order

4. Ordel Line Item - The order is related to the shoes by an order line item which records the Order number, the product, the size and the quantity.

5. Product Images - Shoes can have multiple images to display in the shoe detail carousel.

6. Profile - Each user has an attached profile with more details such as address and running club and marketing opt-in preference.

### Functionality

1. Add to basket - Add quantity, product and size to basket. Was quite challenging to add the size to the basket. In the end the size was concatenated with the product id into one field and split when the basket had to be shown.

2. Adjust basket - change quantity of product in basket.

3. Checkout - Add order details and submit payment information to Stripe.

4. Leave comment - Customer who is registered can add comments to shoe reviews and the bottom of the page.

5. Edit comment - Customer who is logged in can edit their own comments.

6. Delete comment - Customer who is logged in can delete their own comments.

7. Edit profile - Customer can go to their profie page and edit their details.

### Features to Implement

In the near future I would like to bring several features online:

1. Add Strava interacting intergrating my dashboard from the interactive front end project so users can add their Strava credientials and the site will summarise their progress with some interesting statistics around distance and elevation (eg: you have run 50% around the world and climbed everest 5 times)

2. Add extra products like spare spikes and a bag that can be upsold in the basket page.

3. Explored using a the Wagtail CMS to manage the blog but ran out of time to implement properly. Would like to migrate the blog section to Wagtail to make managing it easier.

4. Add Paypal as a payment option.

## Technologies Used

1. [Django](https://www.djangoproject.com/) python framework for the backend.
2. [postgres](https://www.postgresql.org/) for the database.
3. [AWS](https://aws.amazon.com/) for serving static files.
4. [jquery](https://jquery.com/) javascript library to manipulate the DOM in realtime as the customer updates basket quantities.
5. [Slick](http://kenwheeler.github.io/slick/) carousel for touch screen compatible image browsing.
6. [Bootstrap](https://getbootstrap.com/) for front end layout and button styling.
7. [sass](https://sass-lang.com/) for custom styling.


## Testing

The site uses Travis integration to run a set of automated tests of the checkout happy path and the site is not deployed unless they all pass. The automated test suite can be found here: https://github.com/harryphelps2/shoepersonic2/blob/master/shop/tests.py

Manually, an order can be tested to be successful by checking the payment has come through on Stripe.

## Deployment

To deploy the project on Heroku:

1. Add Procfile to tell Heroku about the app:

    ```web: gunicorn shoepersonic2.wsgi:application```

2. Add the env.py config vars to the Heroku config vars

3. Connect to github repository

4. Deploy

To run locally:

```python3 manage.py runserver```


## Contributing

1. Set up virtual environment

```pip install virtualenv```

Go to directory for project and type:

```python3 -m venv env```

then

```source env/bin/activate```

2. Install django

```pip install django```

## Credits

### Acknowledgements

Luke Holbrook for Photography

Robbie Harman for Camera work (https://www.robbieharman.com/)

Celebration animation for purchase can be found here: https://gist.github.com/defaultnamehere/304035030078e590138b

Profile code to update user when profile is saved from https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
