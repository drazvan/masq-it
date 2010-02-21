from models import Space

print 'Content-Type: text/plain'
print ''
print 'Hello, world!'

space = Space(name="SomeSpace")
space.put()

for space in Space.all():
    print space.name, ","