from lesson3.smartphone import Smartphone

catalog = []
catalog.append(Smartphone("Apple", "Iphone 14 pro", "+79555782575"))
catalog.append(Smartphone("Apple", "Iphone 15 pro", "+7955577545"))
catalog.append(Smartphone("Apple", "Iphone 16 pro max", "+79534182425"))
catalog.append(Smartphone("Samsung", "Galaxy A20", "+79353452442"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 20S", "+79815435514"))
[print(i) for i in catalog]
