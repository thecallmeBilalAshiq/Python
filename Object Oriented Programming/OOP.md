# Python OOP Mastery — From C++ to Pythonic Expert

*A complete guide, written for someone who already knows OOP in C++ and wants to become genuinely expert in Python OOP — not just "know the syntax."*

---

## How to use this guide

Since you already know OOP concepts (classes, inheritance, polymorphism, encapsulation) from C++, we won't re-teach *what OOP is*. Instead, every section will:

1. Show the Python way.
2. Explicitly compare it to how C++ does it.
3. Point out the "Pythonic" idiom — because writing C++-style code in Python (even if it works) is a sign you haven't really learned Python OOP yet.

Type out every example yourself. Don't copy-paste. Muscle memory matters.

---

## Table of Contents

1. [Classes and Objects — the basics](#1-classes-and-objects--the-basics)
2. [`self` vs `this`](#2-self-vs-this)
3. [Constructors, `__init__`, and object lifecycle](#3-constructors-__init__-and-object-lifecycle)
4. [Instance vs Class Attributes](#4-instance-vs-class-attributes)
5. [Methods: instance, class, and static](#5-methods-instance-class-and-static)
6. [Encapsulation — Python has no `private`, and that's on purpose](#6-encapsulation--python-has-no-private-and-thats-on-purpose)
7. [Properties — Pythonic getters/setters](#7-properties--pythonic-gettersetters)
8. [Inheritance](#8-inheritance)
9. [Multiple Inheritance and MRO](#9-multiple-inheritance-and-mro)
10. [Polymorphism and Duck Typing](#10-polymorphism-and-duck-typing)
11. [Abstraction with `abc`](#11-abstraction-with-abc)
12. [Magic / Dunder Methods (operator overloading)](#12-magic--dunder-methods-operator-overloading)
13. [Composition over Inheritance](#13-composition-over-inheritance)
14. [`dataclasses` — modern Python OOP](#14-dataclasses--modern-python-oop)
15. [Class introspection & special attributes](#15-class-introspection--special-attributes)
16. [Common mistakes C++ developers make in Python OOP](#16-common-mistakes-c-developers-make-in-python-oop)
17. [Practice Projects (do these to actually master it)](#17-practice-projects-do-these-to-actually-master-it)
18. [Cheat Sheet](#18-cheat-sheet)

---

## 1. Classes and Objects — the basics

```python
class Car:
    pass

my_car = Car()
print(type(my_car))   # <class '__main__.Car'>
```

**C++ comparison:**
```cpp
class Car {};
Car myCar;
```

Key differences immediately:
- No header/source file split. No `.h`/`.cpp`.
- No semicolons, no braces — indentation defines blocks.
- `Car()` in Python *always* means "create an object on the heap and give me a reference to it" — there is no stack-allocated object distinction like C++'s `Car myCar;` vs `Car* myCar = new Car();`. In Python, **everything is a reference to a heap object.** There is no manual `delete`; garbage collection (reference counting + cycle collector) handles it.

---

## 2. `self` vs `this`

In C++, `this` is implicit — you don't write it in the parameter list, but you can use it inside methods.

In Python, `self` is **explicit** in every instance method's parameter list, and Python passes the object automatically when you call `obj.method()`.

```python
class Dog:
    def bark(self):
        print(f"{self.name} says woof!")
```

`self` is not a keyword — it's just a convention (you *could* name it anything, but never do that; every Python developer expects `self`).

**Mental model:** `dog.bark()` is syntactic sugar for `Dog.bark(dog)`. Try it in a REPL — it works exactly the same:

```python
class Dog:
    def bark(self):
        print("woof")

d = Dog()
d.bark()        # normal call
Dog.bark(d)     # identical — proves self is just the first parameter
```

---

## 3. Constructors, `__init__`, and object lifecycle

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

**C++ comparison:**
```cpp
class Car {
public:
    string brand, model;
    int year;
    Car(string b, string m, int y) : brand(b), model(m), year(y) {}
};
```

Important distinctions:
- `__init__` is **not** technically the constructor — `__new__` is (it actually creates the object). `__init__` *initializes* an already-created object. You'll almost never touch `__new__` except for metaclasses, singletons, or immutable-type subclassing.
- There's no constructor **overloading** in Python (no multiple `__init__` with different signatures like C++). Instead you use **default arguments**, `*args`/`**kwargs`, or classmethods as "alternate constructors."

```python
class Car:
    def __init__(self, brand, model, year=2024):
        self.brand = brand
        self.model = model
        self.year = year

    @classmethod
    def from_string(cls, car_str):
        # "Toyota-Corolla-2022"
        brand, model, year = car_str.split("-")
        return cls(brand, model, int(year))

car2 = Car.from_string("Honda-Civic-2021")
```

This `classmethod`-as-alternate-constructor pattern is a core idiom you should adopt — it's Python's answer to C++ constructor overloading.

Destructor equivalent: `__del__` exists but is **rarely used** — Python's garbage collector handles memory. Use context managers (`with` statement, `__enter__`/`__exit__`) instead of destructors for resource cleanup (files, sockets, locks). This is a major mindset shift from C++'s RAII-via-destructors.

```python
class ManagedFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, "w")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with ManagedFile("log.txt") as f:
    f.write("hello")
# file auto-closed here, even if an exception occurred
```

---

## 4. Instance vs Class Attributes

```python
class Dog:
    species = "Canis familiaris"   # class attribute — shared by ALL instances

    def __init__(self, name):
        self.name = name           # instance attribute — unique per object

d1 = Dog("Rex")
d2 = Dog("Fido")
print(d1.species, d2.species)   # same for both
Dog.species = "Canis lupus familiaris"
print(d1.species, d2.species)   # both change — it's shared
```

**C++ comparison:** `species` is the equivalent of a `static` member variable in C++.

**The classic beginner trap** — mutable default class attributes:

```python
class Dog:
    tricks = []   # DANGER: shared across ALL instances

    def add_trick(self, trick):
        self.tricks.append(trick)

d1 = Dog()
d2 = Dog()
d1.add_trick("sit")
print(d2.tricks)  # ['sit']  <- BUG! d2 never learned this trick
```

Always initialize mutable attributes (lists, dicts, sets) inside `__init__`, not as class attributes:

```python
class Dog:
    def __init__(self):
        self.tricks = []   # each instance gets its own list
```

This is the Python equivalent of the C++ trap where a `static` member is accidentally used when you meant a per-object member.

---

## 5. Methods: instance, class, and static

Python has three method types — C++ only really distinguishes instance methods and `static` methods, so `classmethod` is new territory for you.

```python
class Circle:
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius

    # INSTANCE METHOD — needs an object, accesses self
    def area(self):
        return Circle.pi * self.radius ** 2

    # CLASS METHOD — receives the class itself (cls), not an instance
    @classmethod
    def unit_circle(cls):
        return cls(radius=1)

    # STATIC METHOD — no self, no cls — just lives in the class namespace
    @staticmethod
    def is_valid_radius(r):
        return r > 0
```

| Type | Decorator | First param | C++ equivalent |
|---|---|---|---|
| Instance method | none | `self` | regular member function |
| Class method | `@classmethod` | `cls` | none exactly — closest is a `static` factory function that knows the class |
| Static method | `@staticmethod` | none | `static` member function |

Use `@classmethod` for alternate constructors or anything that needs to know *which subclass* called it (important with inheritance — `cls` respects the actual subclass, unlike hardcoding `Circle(...)`).

Use `@staticmethod` for utility functions that logically belong to the class but need no class/instance state — pure organizational grouping.

---

## 6. Encapsulation — Python has no `private`, and that's on purpose

This is the single biggest mental shift coming from C++.

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance          # public (convention: no underscore)
        self._pin = "1234"              # "protected" — convention only
        self.__account_number = "9999"  # "private" — name-mangled
```

- `self.balance` — public. Anyone can read/write it directly.
- `self._pin` — a **single leading underscore** is a *convention* meaning "internal use, don't touch this from outside." Python does **nothing** to enforce it. It's a signal to other developers, not a compiler rule.
- `self.__account_number` — a **double leading underscore** triggers **name mangling**: Python internally renames it to `_BankAccount__account_number`. This isn't true privacy either — it's designed to prevent *accidental* name clashes in subclasses, not to lock outsiders out.

```python
b = BankAccount(1000)
print(b._pin)                        # works — "protected" is not enforced
print(b._BankAccount__account_number)  # works — name mangling is just obfuscation
```

**Why does Python do this?** Python's philosophy is "we're all consenting adults here" — trust the developer, don't build walls, use convention and documentation instead of compiler enforcement. This is philosophically very different from C++'s `private`/`protected`/`public` access specifiers which are enforced at compile time.

**The Pythonic idiom:** use a single underscore for "internal," and use **properties** (next section) when you actually need controlled access — not double underscores.

---

## 7. Properties — Pythonic getters/setters

In C++ you write `getBalance()` / `setBalance()`. In Python, you rarely do this directly — you use `@property` so the caller can still use plain attribute syntax while you keep validation logic.

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        """Getter — called when you do account.balance"""
        return self._balance

    @balance.setter
    def balance(self, value):
        """Setter — called when you do account.balance = value"""
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value

    @balance.deleter
    def balance(self):
        print("Deleting balance...")
        del self._balance


acc = BankAccount(500)
print(acc.balance)     # calls the getter — looks like a plain attribute!
acc.balance = 1000     # calls the setter — validation runs
acc.balance = -50      # raises ValueError
```

This is the **big Pythonic idiom**: start with plain public attributes. Only add `@property` later, when you actually need validation/computation — and callers' code doesn't have to change (`obj.balance` still works, whether it's a raw attribute or a property). In C++, you'd have designed getters/setters from day one because retrofitting them changes the calling syntax (`obj.balance` vs `obj.getBalance()`). Python doesn't force that upfront decision.

---

## 8. Inheritance

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

d = Dog("Rex")
print(d.speak())   # Rex says Woof!
```

**C++ comparison:**
```cpp
class Animal {
public:
    string name;
    Animal(string n) : name(n) {}
    virtual string speak() = 0;  // pure virtual
};
class Dog : public Animal {
public:
    Dog(string n) : Animal(n) {}
    string speak() override { return name + " says Woof!"; }
};
```

Key differences:
- No `virtual` keyword needed. **Every method in Python is virtual by default** — overriding "just works" through normal method lookup.
- No `public`/`private`/`protected` inheritance modes — Python only has one kind of inheritance.
- Call the parent constructor with `super().__init__(...)`, not `Animal::Animal(...)`:

```python
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # calls Animal.__init__
        self.breed = breed
```

`super()` is smarter than it looks — it doesn't just mean "my parent class," it follows the **Method Resolution Order (MRO)**, which matters a lot once you hit multiple inheritance (next section).

---

## 9. Multiple Inheritance and MRO

C++ supports multiple inheritance too, but with the infamous "diamond problem" requiring `virtual` base classes to resolve ambiguity. Python solves this differently, with a deterministic algorithm called **C3 linearization**, exposed via the **Method Resolution Order (MRO)**.

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
d.hello()             # prints "B"
print(D.__mro__)      # (D, B, C, A, object)
```

Python always resolves to a single, predictable, linear order — you can inspect it directly with `ClassName.__mro__` or `ClassName.mro()`. No ambiguity, no need for `virtual` inheritance tricks.

**Mixins** — Python's favorite use of multiple inheritance — are small classes meant to *add* a capability, not represent a "is-a" relationship:

```python
class JSONMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

class LoggerMixin:
    def log(self, msg):
        print(f"[{self.__class__.__name__}] {msg}")

class User(JSONMixin, LoggerMixin):
    def __init__(self, name):
        self.name = name

u = User("Bilal")
u.log("created user")
print(u.to_json())
```

This composition-via-mixins pattern is extremely common in real Python codebases (Django's class-based views are built almost entirely on mixins) — it has no clean C++ equivalent, so pay extra attention here.

---

## 10. Polymorphism and Duck Typing

C++ polymorphism is achieved through inheritance + virtual functions (or templates for compile-time polymorphism). Python has that too — but its default, idiomatic style is **duck typing**: "if it walks like a duck and quacks like a duck, treat it as a duck." No common base class required.

```python
class Duck:
    def sound(self):
        return "Quack"

class Dog:
    def sound(self):
        return "Woof"

class Car:
    def sound(self):
        return "Vroom"

def make_noise(thing):
    print(thing.sound())   # works on ANY object with a .sound() method

for obj in [Duck(), Dog(), Car()]:
    make_noise(obj)
```

None of these classes share a base class or interface. Python doesn't care — it only checks at runtime whether `.sound()` exists. This is **structural typing**, and it's central to how Python OOP differs philosophically from C++'s nominal typing (where the compiler checks the type hierarchy explicitly).

If you want more structure/safety, use `typing.Protocol` (Python's answer to structural interfaces, checkable by static type checkers like `mypy`):

```python
from typing import Protocol

class SoundMaker(Protocol):
    def sound(self) -> str: ...

def make_noise(thing: SoundMaker) -> None:
    print(thing.sound())
```

No inheritance needed even here — any class with a matching `sound()` method satisfies the protocol. This is the modern, type-checked evolution of duck typing.

---

## 11. Abstraction with `abc`

Python's version of C++ pure virtual functions / abstract classes uses the `abc` (Abstract Base Classes) module.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)

# Shape()          # TypeError: Can't instantiate abstract class
r = Rectangle(3, 4)
print(r.area())     # 12
```

If `Rectangle` doesn't implement all abstract methods, instantiating it raises `TypeError` at object-creation time — this is the closest Python gets to C++'s compile-time enforcement of pure virtual functions, except it's a **runtime** check, not compile-time (Python has no compile step in the C++ sense).

---

## 12. Magic / Dunder Methods (operator overloading)

C++ operator overloading uses `operator+`, `operator<<`, etc. Python uses **dunder methods** (double-underscore methods) — this is one of the most powerful and distinctly Python parts of OOP.

```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"        # for developers (repr(obj))

    def __str__(self):
        return f"({self.x}, {self.y})"               # for users (print(obj))

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __len__(self):
        return int((self.x**2 + self.y**2) ** 0.5)

    def __getitem__(self, index):
        return (self.x, self.y)[index]

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)       # Vector(4, 6)  -- calls __add__
print(v1 == Vector(1, 2))   # True -- calls __eq__
print(v1[0])          # 1 -- calls __getitem__
```

Common dunder methods worth memorizing:

| Dunder | Triggered by | C++ equivalent |
|---|---|---|
| `__init__` | `Obj()` | constructor |
| `__del__` | garbage collection | destructor (rarely used) |
| `__repr__` | `repr(obj)`, debugger | (no direct equivalent — closest: `operator<<` for debug) |
| `__str__` | `print(obj)`, `str(obj)` | `operator<<` |
| `__eq__` | `==` | `operator==` |
| `__lt__`, `__le__`, etc. | `<`, `<=`, ... | `operator<`, etc. |
| `__add__`, `__sub__`, etc. | `+`, `-`, ... | `operator+`, etc. |
| `__len__` | `len(obj)` | `.size()` method (not operator-based) |
| `__getitem__` | `obj[i]` | `operator[]` |
| `__call__` | `obj()` | `operator()` (functor) |
| `__iter__` / `__next__` | `for x in obj` | custom iterator class |
| `__enter__` / `__exit__` | `with obj:` | RAII / destructors |

`__call__` deserves a highlight — it makes any object callable like a function, Python's version of a C++ functor:

```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor

double = Multiplier(2)
print(double(5))   # 10 -- obj used like a function
```

---

## 13. Composition over Inheritance

You know this principle from C++ too ("has-a" vs "is-a"), but Python culture leans on it *even more heavily* than C++ culture does, largely because Python's flexible duck typing makes deep inheritance hierarchies less necessary.

```python
class Engine:
    def start(self):
        print("Engine starting...")

class Car:
    def __init__(self):
        self.engine = Engine()   # Car HAS-A Engine (composition)

    def start(self):
        self.engine.start()
        print("Car ready to drive")

c = Car()
c.start()
```

**Rule of thumb:** favor composition unless there's a genuine "is-a" relationship *and* you need polymorphism (treating subclasses uniformly through a common interface). Deep inheritance chains (4-5 levels) are considered a code smell in Python, just as they often are in modern C++ too — but Python developers enforce this more strictly.

---

## 14. `dataclasses` — modern Python OOP

Python 3.7+ gives you `@dataclass`, which auto-generates `__init__`, `__repr__`, `__eq__`, and more — eliminating a huge amount of boilerplate for classes that mostly just hold data (similar in spirit to C++20's aggregate initialization or a simple `struct`, but far more powerful).

```python
from dataclasses import dataclass, field

@dataclass
class Point:
    x: float
    y: float
    label: str = "origin"

p1 = Point(1.0, 2.0)
p2 = Point(1.0, 2.0)
print(p1)              # Point(x=1.0, y=2.0, label='origin')  -- auto __repr__
print(p1 == p2)         # True -- auto __eq__

@dataclass
class Team:
    name: str
    members: list = field(default_factory=list)   # correct way to default a mutable field
```

Use `@dataclass` whenever a class is primarily a data container. Reach for a plain class when behavior/encapsulation is the point.

---

## 15. Class introspection & special attributes

Python OOP includes runtime introspection tools with no real C++ equivalent (C++ has no built-in reflection):

```python
class Dog:
    def __init__(self, name):
        self.name = name

d = Dog("Rex")

print(type(d))                 # <class '__main__.Dog'>
print(isinstance(d, Dog))      # True
print(d.__dict__)              # {'name': 'Rex'}  -- instance attributes as a dict!
print(Dog.__dict__.keys())     # class attributes/methods
print(hasattr(d, "name"))      # True
print(getattr(d, "name"))      # "Rex"
setattr(d, "age", 3)           # dynamically add an attribute — legal in Python!
```

That last line is a big one: in Python, **you can add attributes to an object after it's created**, on the fly, unless the class explicitly forbids it with `__slots__`. This is impossible in C++, where an object's memory layout is fixed at compile time.

```python
class Point:
    __slots__ = ("x", "y")   # locks the attribute set — saves memory, prevents typos

    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(1, 2)
p.z = 5   # AttributeError: 'Point' object has no attribute 'z'
```

`__slots__` is the closest thing Python has to C++'s fixed-layout objects, and it's a real performance/memory optimization worth knowing for production code.

---

## 16. Common mistakes C++ developers make in Python OOP

1. **Writing getters/setters for everything upfront.** Don't. Use plain attributes; add `@property` later only if needed.
2. **Using `__double_underscore` everywhere for "private."** Use single `_underscore` by convention; reserve double-underscore for genuine name-clash prevention in inheritance.
3. **Deep, rigid inheritance hierarchies.** Prefer composition and duck typing.
4. **Forgetting `self` in method definitions.** Python won't auto-insert it like C++'s implicit `this`.
5. **Mutable default arguments** (`def f(self, items=[])`) — this is the Python equivalent of a dangling-reference bug. Always use `None` and initialize inside the method:
   ```python
   def add(self, item, items=None):
       if items is None:
           items = []
       items.append(item)
   ```
6. **Manually calling `__del__` expecting deterministic destruction like C++ RAII.** Use context managers (`with`) instead.
7. **Assuming `==` compares memory addresses by default like it might conceptually.** Python's default `__eq__` compares identity (same as `is`) unless you override it — always override `__eq__` (and `__hash__` if needed) for value-based comparison.

---

## 17. Practice Projects (do these to actually master it)

Reading isn't enough — build these, in order, without looking things up until you're stuck:

1. **Bank Account System** — classes for `Account`, `SavingsAccount`, `CheckingAccount` (inheritance), with `@property` for balance validation, custom exceptions for insufficient funds.
2. **Shape Hierarchy** — abstract `Shape` base class (`abc`), subclasses `Circle`, `Rectangle`, `Triangle`, each implementing `area()`/`perimeter()`; write a function that computes total area of a list of mixed shapes (polymorphism in action).
3. **Vector/Matrix math library** — heavy use of dunder methods (`__add__`, `__mul__`, `__eq__`, `__repr__`, `__getitem__`).
4. **A small Library Management System** — `Book`, `Member`, `Library` classes using composition (`Library` *has* `Book`s and `Member`s), with mixins for `Loggable` and `Serializable` (JSON export).
5. **Custom Iterator/Context Manager** — build a class that's iterable (`__iter__`/`__next__`) representing, say, a paginated dataset, and a separate class using `__enter__`/`__exit__` to manage a fake "database connection."
6. **Refactor project #4 using `@dataclass`** wherever it simplifies things, and add `__slots__` where appropriate — compare code size/readability before and after.

Once you've built all six without heavy reference-checking, you genuinely know Python OOP at an expert level.

---

## 18. Cheat Sheet

```python
class MyClass(BaseClass):
    class_var = 0                      # shared across instances

    def __init__(self, x):             # constructor (initializer)
        self.x = x                     # instance attribute
        self._y = 0                    # "protected" (convention)
        self.__z = 0                   # "private" (name-mangled)
        super().__init__()             # call parent constructor

    def instance_method(self):
        return self.x

    @classmethod
    def alt_constructor(cls, data):
        return cls(data)

    @staticmethod
    def utility():
        return True

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    def __repr__(self):
        return f"MyClass({self.x})"

    def __eq__(self, other):
        return self.x == other.x
```

| Concept | Python | C++ |
|---|---|---|
| Instance ref | always heap, reference semantics | stack (value) or heap (pointer/ref) |
| Constructor | `__init__` (+ `__new__`) | class-name method |
| Destructor | `__del__` (rare); prefer `with` | destructor (RAII) |
| Access control | convention only (`_`, `__`) | enforced (`private`, `protected`, `public`) |
| Virtual functions | all methods virtual by default | need `virtual` keyword |
| Abstract class | `abc.ABC` + `@abstractmethod` | pure virtual (`= 0`) |
| Multiple inheritance | supported, resolved via MRO/C3 | supported, needs `virtual` base to fix diamond |
| Operator overload | dunder methods (`__add__`, ...) | `operator+`, etc. |
| Interfaces | duck typing / `Protocol` | abstract base class as interface |
| Static typing | optional (`typing` module, checked by `mypy`) | mandatory, compiler-enforced |

---