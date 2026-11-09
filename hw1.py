"""CSC 1001 - Programming Assignment 1.

Student starter file. Implement the eight required functions below.
The provided data types live in data.py; do not edit data.py.

For EVERY function, replace the TODO documentation with a short comment
explaining its purpose, input(s), and output. You may write helper functions.
"""

import math

import data


# Part 1: vowel_count
# Purpose: count how many vowels (a, e, i, o, u, upper or lowercase) appear
#   in a string.
# Input: text, the string to examine.
# Output: the number of vowels in text, as an int.
def vowel_count(text: str) -> int:
    count = 0
    for char in text:
        if char in "aeiouAEIOU":
            count = count + 1
    return count


# Part 2: short_lists
# Purpose: keep only the nested lists that have exactly two elements.
# Input: items, a list of lists of ints.
# Output: a new list holding the length-2 nested lists, in their original
#   order. The input list is not changed.
def short_lists(items: list[list[int]]) -> list[list[int]]:
    result = []
    for inner in items:
        if len(inner) == 2:
            result.append(inner)
    return result


# Part 3: ascending_pairs
# Purpose: put every length-2 nested list into non-descending order
#   (smaller value first) while leaving all other nested lists as they are.
# Input: items, a list of lists of ints.
# Output: a new list with the same nested lists in the same outer order;
#   each length-2 list has its values in non-descending order. The input
#   list and its nested lists are not changed.
def ascending_pairs(items: list[list[int]]) -> list[list[int]]:
    result = []
    for inner in items:
        if len(inner) == 2 and inner[0] > inner[1]:
            result.append([inner[1], inner[0]])
        else:
            result.append(list(inner))
    return result


# Part 4: add_prices
# Purpose: add two prices, carrying any extra cents into dollars.
# Input: first, a Price.
# Input: second, a Price.
# Output: a new Price equal to first + second, with cents between 0 and 99.
def add_prices(first: data.Price, second: data.Price) -> data.Price:
    total_cents = first.cents + second.cents
    dollars = first.dollars + second.dollars + total_cents // 100
    cents = total_cents % 100
    return data.Price(dollars, cents)


# Part 5: rectangle_area
# Purpose: compute the area of an axis-aligned rectangle.
# Input: rectangle, a Rectangle whose top_left corner is above and to the
#   left of its bottom_right corner.
# Output: the rectangle's area (width * height), as a float.
def rectangle_area(rectangle: data.Rectangle) -> float:
    width = rectangle.bottom_right.x - rectangle.top_left.x
    height = rectangle.top_left.y - rectangle.bottom_right.y
    return width * height


# Part 6: books_by_author
# Purpose: find every book written (or co-written) by a given author.
# Input: author, the author's name as a string.
# Input: books, a list of Book objects.
# Output: a new list of the Books whose authors list contains author, in
#   their original order.
def books_by_author(author: str, books: list[data.Book]) -> list[data.Book]:
    result = []
    for book in books:
        if author in book.authors:
            result.append(book)
    return result


# Helper: distance between two points.
# Input: p1, a Point.
# Input: p2, a Point.
# Output: the straight-line distance between p1 and p2, as a float.
def distance(p1: data.Point, p2: data.Point) -> float:
    return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)


# Part 7: circle_bound
# Purpose: build the smallest circle that encloses a rectangle.
# Input: rectangle, an axis-aligned Rectangle.
# Output: a new Circle centered at the rectangle's center, whose radius is
#   the distance from that center to a corner of the rectangle.
def circle_bound(rectangle: data.Rectangle) -> data.Circle:
    center_x = (rectangle.top_left.x + rectangle.bottom_right.x) / 2
    center_y = (rectangle.top_left.y + rectangle.bottom_right.y) / 2
    center = data.Point(center_x, center_y)
    radius = distance(center, rectangle.top_left)
    return data.Circle(center, radius)


# Part 8: below_pay_average
# Purpose: find the employees who are paid strictly less than the average
#   pay rate of the group.
# Input: employees, a list of Employee objects.
# Output: a list of the names (strings) of employees whose pay_rate is
#   strictly below the average, in their original order. An empty input
#   list gives an empty list.
def below_pay_average(employees: list[data.Employee]) -> list[str]:
    if len(employees) == 0:
        return []
    total = 0
    for employee in employees:
        total = total + employee.pay_rate
    average = total / len(employees)
    names = []
    for employee in employees:
        if employee.pay_rate < average:
            names.append(employee.name)
    return names