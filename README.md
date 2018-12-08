# Full Stack Development Milestone Project - Shoepersonic.com

[![Build Status](https://travis-ci.org/harryphelps2/shoepersonic2.svg?branch=master)](https://travis-ci.org/harryphelps2/shoepersonic2)

Link to live site: https://recipes-hp.herokuapp.com/



## Business Objectives

Sell shoes to people like Derek (see below).

## Customer Profile, Derek from London:

Grew up London, enjoys running as a project on the side to stay healthy, relieve stress and compete. Dave was never a talented athlete but he is persistent and enjoys training to compete in races. He did a degree in mechanical engineering and ran in a club at school and tried out numerous individual sports at university. David struggles with confidence around other men and women and enjoys running. He likes feeling part of a club but struggles to break through into the social side of things. He really wants to be invited to the party but feels like he is never engaging enough or gregarious enough break into the cool crowd. 

He doesn’t mind spending money in his hobby but is time poor. He makes decisions quickly. 

He has a reasonable amount of speed and believes if he stuck to running and had more time to train he could really excel. 

He hates ignorance. His science background has given him a healthy sense of I know better. He always feels slightly outside the mainstream, slightly ahead of he curve.  He talks to other runners about new training techniques but they don’t know what he is talking about. 

He loves learning about running  but can’t find anyone to talk about it with. He runs to give him confidence. He doesn’t need running shoes that are supportive or gimmicky he looks for running shoes that are light and look good so when he turns up on the start like he feels like the real deal. He likes encouragement. Often described as stoic he has learned to work hard. He wants to be recognised for what talent he has. He is not the most genetically gifted athlete and that plays on his mind. He believes hard work will pay off and wants to see how far he can take running. 

He gets nervous about racing and likes to research them before he goes. He wants to learn more about race tactics elevation and ground quality. He likes to see things up-close. Tne more detail Derek can get about a prospective pruchase the more it draws him in. He finds buying shoes online stressful as you can't try them on and wants to know what they are like to run in. 

## UX

The user should be able to:

1. Choose a shoe to view in more detail

2. Choose a size and quantity and add it to the basket

3. View the basket and total price before choosing to buy

4. Agree to purchase and be able to input contact details

5. Add delivery details

6. Add card details and make purchase

7. Be able to add details to save for next time.

The shoe owner should be able to:

1. Enforce the terms and conditions in order for the customer to make a purchase

2. Be able to control and edit stock levels so that a customer cannot purchase something that is not in stock.


## Features

### Views

The site has ben designed for mobile first

1. Base page, navbar and footer - The base page allows the site designer to change the title page and meta description with a block tags to match choosen keywords and improve SEO. The navbar collapses at smaller screen sizes.

2. Landing page - A big hero image, with the brand and strapline to welcome the customer in. Scrolling down the customer can sees a summary of the what the site does. The hero image has a call-to-action 'SHOP NOW' red button to invite the customer to view the product page. The font sizes adjust for larger screens.

3. Product Page - Clicking through to the product page the customer can see all 5 shoes sold with a summary of their features. The number of cards per row adjusts with screen size. 

4. Shoe detail page - This page has a responsive touch screen compatible carousel of product images and the product name. The customer can select a size from the drop down which tells them how many of each shoe is left. The customer can also increase and decrease the quantity which uses jquery to update the quantity number when the button is clicked. The user then clicks add to basket and the size, quantity and product are added to the session storage.

5. Basket - The Basket page shows all the products added so far and their total. The customer can update the quantity of the shoe by selecting the pluses and minuses. (BUG: If there is more than one pair of shoes in the basket the quantity updater will always update the top one. There wasn't time to fix this bug. It is assumed most customers will only purchase the one pair of shoes but the bug will get fixed early next year.) The customer selects checkout and goes to the contact details page.

4. Contact details

5. Delivery Details

6. Card details

7. Order confirmation

8. Review page with comparative shoe review

9. The Hangar (blog page with links to articles)


### Data



### Functionality

1. Add to basket

2. Adjust basket

3. 


### Features to Implement

In the near future I would like to bring several features:

1. Add Strava interacting intergrating my dashboard from the interactive front end project so users can add their Strava credientials and the site will summarise their progress with some interesting statistics around distance and elevation (eg: you have run 50% around the world and climbed everest 5 times)
2. Add extra products like spare spikes and a bag that can be upsold in the basket page.
3. Search Engine Optimization of all pages to include keywords capabable of ranking in google top 10 for every page on the site.
4. Explored using a the Wagtail CMS to manage the blog but ran out of time to implement properly. Would like to migrate the blog section to Wagtail to make managing it easier.
5. Add Paypal as a payment option.

## Technologies Used

1. [Django](https://www.djangoproject.com/) python framework for the backend
2. [postgres](https://www.postgresql.org/) for the database.
3. [AWS](https://aws.amazon.com/) for serving static files.
4. [jquery](https://jquery.com/) javascript library to manipulate the DOM in realtime as the customer updates basket quantities.
5. [Slick](http://kenwheeler.github.io/slick/) carousel for touch screen compatible image browsing.
6. [Bootstrap](https://getbootstrap.com/) for front end layout and button styling.
7. [sass](https://sass-lang.com/) for custom styling.


## Testing

The site uses Travis integration to run a set of automated tests of the checkout happy path and the site is not deployed unless they all pass. The automated test suite can be found here: https://github.com/harryphelps2/shoepersonic2/blob/master/shop/tests.py




## Deployment

To deploy the project on Heroku:



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
