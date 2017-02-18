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

firstResult = session.query(Restaurant).first()
print(firstResult.name)

