from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)

session = DBSession()

# first entry
myFirstRestaurant = Restaurant(name = " Pizza World")
#session.add(myFirstRestaurant)
#session.commit()

#session.query(Restaurant).all

# menu entry
cheesePizza = MenuItem(name = "cheese pizza", description = "made with natura stuff",
                       course = "Entree", price = "8.99" , restaurant = myFirstRestaurant)
#session.add(cheesePizza)
#session.commit()

allRestaurant = session.query(Restaurant).filter_by(id = 3).one()
name = allRestaurant.name
print(name)

# get all menu items. READ
Items = session.query(MenuItem).all()
for el in Items:
    print(el.restaurant.name)
    print("\n")

#get menu item by name
veggieBurger = session.query(MenuItem).filter_by(restaurant_id = 3)
for vb in veggieBurger:
    print(vb.restaurant_id)
    print(vb.restaurant.name)
    print(vb.price)
    print("\n")


# get burger with id 43 Auntie Ann's diner
AuntieB = session.query(MenuItem).filter_by(id = 43).one()
print(AuntieB.price)
print("\n")

# changing burger price UPDATE
#AuntieB.price = "$9.69"
#session.add(AuntieB)
#session.commit()

# filtering by ID
items = session.query(MenuItem).filter_by(restaurant_id = 3)
for item in items:
    print(item.restaurant.name)
    print("\n")


# Delete
spinach = session.query(MenuItem).filter_by(name = 'Spinach Ice Cream').one()
print(spinach.name)
session.delete(spinach)
session.commit()