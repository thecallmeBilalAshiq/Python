# Python OOP — Aasan Roman Urdu Guide (C++ se Python tak)

*Ye guide un logon ke liye hai jo C++ ka OOP jaante hain aur ab Python ka OOP seekh rahe hain. Har cheez ko sabse aasan tareeqe se, roz-marra ki misalon se samjhaya gaya hai.*

---

## Kaise parhna hai

Aap C++ mein classes, objects, inheritance already jaante hain — is liye hum "OOP kya hota hai" nahi seekhenge. Balke sirf ye dekhenge ke **Python mein wahi cheezein kaise likhi jaati hain**, aur C++ se kya farq hai.

Har code khud type karo, copy-paste mat karo. Hath se likhne se yaad rehta hai.

---

## 1. Class aur Object — Shuruaat

```python
class Car:
    pass

my_car = Car()
print(type(my_car))
```

Socho **Class** ek **naqsha (blueprint)** hai — jaise ghar ka naqsha. Aur **Object** us naqshe se bana hua asli ghar hai.

- `class Car:` — naqsha bana rahe hain
- `Car()` — naqshe se ek asli ghar (object) bana rahe hain

**C++ se farq:** C++ mein aap `Car myCar;` likh kar stack pe object bana sakte the, ya `new Car()` se heap pe. Python mein **har object hamesha heap pe** banta hai, aur aapke paas uska sirf reference hota hai. `delete` bhi khud nahi karna padta — Python khud memory saaf kar deta hai (garbage collection).

---

## 2. `self` kya hai (C++ ke `this` jaisa)

```python
class Dog:
    def bark(self):
        print(f"{self.name} bhonk raha hai")
```

`self` ka matlab hai **"main khud"** — yani wo object jispe method call ho raha hai.

C++ mein `this` chupa hota hai, aap likhte nahi. Python mein `self` **har method mein khule aam likhna padta hai**, pehla parameter ban ke.

Yaad rakho: `dog.bark()` likhna aur `Dog.bark(dog)` likhna — dono ek hi cheez hain. Python khud `dog` ko `self` mein daal deta hai.

---

## 3. `__init__` — Constructor

```python
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"

my_car = Car("Toyota", "Corolla", 2022)
print(my_car)   # 2022 Toyota Corolla
```

`__init__` wo function hai jo **jab bhi object banta hai, khud-ba-khud chalta hai**. Isme aap object ki starting values set karte hain — bilkul C++ ke constructor jaisa.

**Zaroori baat:** Python mein aap ek class mein **do `__init__` nahi likh sakte** (jaise C++ mein overloading hoti hai — same naam ke multiple constructors). Iski jagah ya to default values do, ya `classmethod` use karo:

```python
class Car:
    def __init__(self, brand, model, year=2024):
        self.brand = brand
        self.model = model
        self.year = year

    @classmethod
    def from_string(cls, car_str):
        brand, model, year = car_str.split("-")
        return cls(brand, model, int(year))

car2 = Car.from_string("Honda-Civic-2021")
```

Ye `@classmethod` wala tareeqa Python ka "dusra constructor banane" ka rasta hai.

**Destructor ka kissa:** C++ mein aap destructor pe bharosa karte the ke file band ho jaye, connection close ho jaye. Python mein `__del__` hota to hai, lekin **istemal nahi karte** — iski jagah `with` statement use karte hain:

```python
class ManagedFile:
    def __enter__(self):
        self.file = open("log.txt", "w")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with ManagedFile() as f:
    f.write("hello")
# yahan file khud band ho jayegi, chahe error hi kyun na aaye
```

---

## 4. Instance Attribute vs Class Attribute

```python
class Dog:
    species = "Canis familiaris"   # SAARI dogs ke liye SAME

    def __init__(self, name):
        self.name = name            # HAR dog ka apna alag naam
```

- **Class attribute** (`species`) — ek hi value, **sab objects share** karte hain. Bilkul C++ ke `static` member jaisa.
- **Instance attribute** (`self.name`) — har object ka **apna alag** hota hai.

### Sabse bada trap (dhyan se parho!)

```python
class Dog:
    tricks = []   # KHATRA: sab dogs isko SHARE karenge

    def add_trick(self, trick):
        self.tricks.append(trick)

d1 = Dog()
d2 = Dog()
d1.add_trick("baithna")
print(d2.tricks)  # ['baithna']  <- BUG! d2 ne to seekha hi nahi tha!
```

List, dictionary jaisi cheezein **kabhi class ke andar seedha mat likho**. Hamesha `__init__` ke andar banao:

```python
class Dog:
    def __init__(self):
        self.tricks = []   # ab har dog ki apni alag list hai
```

---

## 5. Teen Tarah ke Methods

```python
class Circle:
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius

    def area(self):                    # INSTANCE method — object chahiye
        return Circle.pi * self.radius ** 2

    @classmethod
    def unit_circle(cls):              # CLASS method — poori class ko pata hota hai
        return cls(radius=1)

    @staticmethod
    def is_valid_radius(r):            # STATIC method — na self, na cls
        return r > 0
```

| Type | Pehla Parameter | Kab Use Karo |
|---|---|---|
| Instance method | `self` | Jab object ki apni values chahiye |
| Class method | `cls` | Jab naya object khud bana ke dena ho (alternate constructor) |
| Static method | kuch nahi | Jab sirf ek helper function chahiye, class se related hai bas naam ke liye |

---

## 6. "Private" Kuch Nahi Hota Python Mein!

Ye sabse bada farq hai C++ se, dhyan se samjho.

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance          # PUBLIC — koi bhi access kar sakta hai
        self._pin = "1234"              # "Protected" — sirf ISHARA hai, rok nahi
        self.__account_number = "9999"  # "Private" jaisa — lekin ye bhi rok nahi
```

- `self.balance` — bilkul khula hua, koi bhi bahar se change kar sakta hai.
- `self._pin` (ek underscore) — sirf ek **request** hai dusre developers se: "isko bahar se mat chhedo." Python isko rokta bilkul nahi.
- `self.__account_number` (do underscore) — Python iska naam khud badal deta hai (`_BankAccount__account_number`), lekin ye bhi **security nahi hai**, sirf accidental clash rokne ke liye hai.

```python
b = BankAccount(1000)
print(b._pin)                          # phir bhi chal jayega
print(b._BankAccount__account_number)  # ye bhi chal jayega
```

**Kyun aisa hai?** Python ki soch ye hai: "hum sab samajhdar log hain, compiler ko rokwala banane ki zaroorat nahi." C++ mein `private`/`protected`/`public` compiler khud check karta hai. Python mein sirf **convention (rules of thumb)** hai, koi lock nahi.

---

## 7. `@property` — Sahi Tareeqa Getter/Setter Ka

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance negative nahi ho sakta")
        self._balance = value

acc = BankAccount(500)
print(acc.balance)     # dikhta seedha attribute jaisa hai, lekin getter chal raha hai
acc.balance = 1000      # setter chalega, check karega
acc.balance = -50       # error dega
```

C++ mein aap shuru se hi `getBalance()`/`setBalance()` banate the. Python mein aap **seedha `self.balance` se shuru karo**, aur baad mein zaroorat pade to `@property` laga do — bahar wala code (`acc.balance`) bilkul waisa hi rahega, badalna nahi padega. Ye Python ka bada fayda hai.

---

## 8. Inheritance (Wirasat)

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Bacchi class ko ye likhna hoga")

class Dog(Animal):
    def speak(self):
        return f"{self.name} bolta hai: Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} bolta hai: Meow!"

d = Dog("Rex")
print(d.speak())
```

Farq C++ se:
- Python mein `virtual` likhna hi nahi padta — **har method khud-ba-khud virtual hoti hai**.
- `public`/`private` inheritance jaisa kuch nahi — bas ek hi tarah ki inheritance hoti hai.
- Parent ka constructor call karne ke liye `super().__init__(...)` likhte hain:

```python
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # Animal ka __init__ call ho raha hai
        self.breed = breed
```

---

## 9. Multiple Inheritance aur MRO

C++ mein multiple inheritance ka "diamond problem" hota hai jise fix karne ke liye `virtual` base class chahiye hoti hai. Python isko khud automatically ek fix, predictable tareeqe se solve karta hai (MRO — Method Resolution Order):

```python
class A:
    def hello(self):
        print("A")

class B(A):
    def hello(self):
        print("B")

class C(A):
    def hello(self):
        print("C")

class D(B, C):
    pass

d = D()
d.hello()             # "B" print hoga
print(D.__mro__)      # order dikha dega: D -> B -> C -> A
```

`__mro__` likh kar aap khud dekh sakte ho ke Python kis order mein methods dhoondta hai. Koi confusion nahi rehti.

**Mixins** — chhoti classes jo sirf ek extra kaam add karti hain (relationship nahi banati):

```python
class LoggerMixin:
    def log(self, msg):
        print(f"[{self.__class__.__name__}] {msg}")

class User(LoggerMixin):
    def __init__(self, name):
        self.name = name

u = User("Bilal")
u.log("user bana diya")
```

---

## 10. Polymorphism aur Duck Typing

C++ mein polymorphism ke liye inheritance + virtual functions zaroori hoti hain. Python ka andaz zyada relaxed hai — isko **duck typing** kehte hain: "agar bathak (duck) ki tarah chalta hai aur bathak ki tarah aawaz nikalta hai, to usay bathak samjho" — chahe koi common parent class ho ya na ho.

```python
class Duck:
    def sound(self):
        return "Quack"

class Dog:
    def sound(self):
        return "Woof"

def make_noise(cheez):
    print(cheez.sound())   # kisi bhi object pe chalega jispe .sound() method ho

for obj in [Duck(), Dog()]:
    make_noise(obj)
```

`Duck` aur `Dog` ka koi common parent nahi hai, phir bhi dono kaam kar rahe hain — bas dono ke paas `.sound()` method hai. C++ mein aisa aasani se nahi hota, wahan type-hierarchy compiler check karta hai.

---

## 11. Abstract Class (`abc`) — C++ ke Pure Virtual Jaisa

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h

    def area(self):
        return self.w * self.h

# Shape()   # Error! Abstract class ka object nahi ban sakta
r = Rectangle(3, 4)
print(r.area())   # 12
```

`Shape` ek "adhoori" class hai — isse seedha object nahi ban sakta. Sirf wo classes object bana sakti hain jinhone `area()` ko poora likha ho. Ye bilkul C++ ke pure virtual function (`= 0`) jaisa kaam karta hai, bas check compile time pe nahi, **run time** pe hota hai.

---

## 12. Dunder (Magic) Methods — Operator Overloading

C++ mein `operator+` likhte the. Python mein double-underscore wale special methods hote hain:

```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)             # Vector(4, 6) — ye __add__ chalata hai
print(v1 == Vector(1, 2))   # True — ye __eq__ chalata hai
```

Yaad rakhne wale important dunders:

| Dunder | Kab Chalta Hai |
|---|---|
| `__init__` | Object banate waqt |
| `__str__` / `__repr__` | `print(obj)` karte waqt |
| `__eq__` | `==` use karte waqt |
| `__add__` | `+` use karte waqt |
| `__len__` | `len(obj)` karte waqt |
| `__getitem__` | `obj[i]` likhte waqt |
| `__call__` | `obj()` likhte waqt (jaise function ho) |
| `__iter__`/`__next__` | `for x in obj` likhte waqt |
| `__enter__`/`__exit__` | `with obj:` likhte waqt |

---

## 13. Composition — "Has-A" Relationship

```python
class Engine:
    def start(self):
        print("Engine chaal raha hai...")

class Car:
    def __init__(self):
        self.engine = Engine()   # Car ke ANDAR ek Engine hai (has-a)

    def start(self):
        self.engine.start()
        print("Car ready hai")

c = Car()
c.start()
```

Simple rule: agar sach mein "is-a" relationship hai (Dog **hai ek** Animal), to inheritance use karo. Agar sirf ek cheez doosri cheez ke andar hai (Car **rakhti hai** ek Engine), to composition use karo. Python developers composition ko zyada pasand karte hain, deep inheritance chains (4-5 levels) ko buri aadat samjha jaata hai.

---

## 14. `@dataclass` — Boilerplate Khatam

```python
from dataclasses import dataclass, field

@dataclass
class Point:
    x: float
    y: float
    label: str = "origin"

p1 = Point(1.0, 2.0)
print(p1)              # Point(x=1.0, y=2.0, label='origin') — khud print bhi ban gaya
print(p1 == Point(1.0, 2.0))   # True — khud compare bhi ho gaya
```

Agar aapki class sirf data rakhne ke liye hai (jaise C++ ka simple `struct`), to `__init__`, `__repr__`, `__eq__` khud haath se likhne ki bajaye `@dataclass` laga do — Python khud sab bana dega.

---

## 15. Chhoti Chhoti Zaroori Baatein

```python
d = Dog("Rex")
print(type(d))                 # Dog class ka object hai
print(isinstance(d, Dog))      # True
print(d.__dict__)              # {'name': 'Rex'} — instance ki saari values dictionary mein!
setattr(d, "age", 3)           # object ke banne ke BAAD bhi naya attribute daal sakte ho!
```

Ye last wali baat C++ mein mumkin nahi — wahan object ka structure pehle hi fix ho jaata hai compile time pe. Python mein object banne ke baad bhi naya attribute jod sakte ho, jab tak `__slots__` use na kiya ho.

---

## 16. C++ Wale Log Kaunsi Galtiyan Karte Hain

1. **Shuru se hi getter/setter banana** — mat karo, seedha attribute use karo, baad mein zaroorat pade to `@property` lagao.
2. **Har jagah `__private` (double underscore) lagana** — single `_` kaafi hai zyada tar jagah.
3. **Lambi inheritance chain banana** — composition ko tarjeeh do.
4. **`self` bhool jaana** — Python khud add nahi karta, hamesha likhna padega.
5. **List/dict ko default argument banana** (`def f(self, items=[])`) — bug ban jayega, `None` use karo phir andar check karo.
6. **`__del__` pe bharosa karna file/connection band karne ke liye** — `with` statement use karo.

---

## 17. Practice Karne Ke Liye Projects

1. **Bank Account System** — `Account`, `SavingsAccount` classes, `@property` se balance check.
2. **Shapes** — `Shape` abstract class, `Circle`, `Rectangle` — sab ka `area()` nikaalo.
3. **Vector Math** — `__add__`, `__eq__`, `__repr__` use karke chhota vector calculator.
4. **Library System** — `Book`, `Member`, `Library` classes, composition ke saath.
5. **Custom Iterator** — `__iter__`/`__next__` use karke apna khud ka loop-able object banao.

Ye projects khud bana lo, dekh ke nahi — tab jaake pakka yaad rahega.

---