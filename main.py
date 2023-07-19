"""Doc string"""

from stuff import StuffClass

print("Hello world")

stuff_object = StuffClass(5)
stuff_object.show_count()
stuff_object.update()
stuff_object.show_count()
stuff_object.count = 9
stuff_object.show_count()
stuff_object.update()
stuff_object.show_count()
