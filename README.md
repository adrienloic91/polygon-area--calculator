# 📐 Polygon Area Calculator

## 📖 Project Description
This project demonstrates object-oriented programming concepts in Python, with a focus on **inheritance**.

It allows users to create rectangles and squares, modify their dimensions, calculate geometric properties, and determine how many shapes can fit inside another shape.

This project is part of freeCodeCamp’s *Scientific Computing with Python* certification.

---

## 🧠 Key Concepts
- Object-Oriented Programming (OOP)
- Class inheritance
- Method overriding
- Geometric calculations

---

## 📋 Features
- ✅ Create rectangles with custom width and height  
- ✅ Create squares as a specialized type of rectangle  
- ✅ Calculate area, perimeter, and diagonal  
- ✅ Generate a visual representation of shapes  
- ✅ Determine how many shapes can fit inside another  

---

## 🧪 Example Usage

```python
from polygon import Rectangle, Square

rect = Rectangle(10, 5)
square = Square(3)

print(rect.get_area())        # 50
print(square.get_area())      # 9
print(rect.get_amount_inside(square))  # 6
🧱 Class Overview
Rectangle