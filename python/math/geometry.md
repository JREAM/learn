# Geometry
Some formulas and geometry to remember when I forget. And while taking notes I recall
and relearn things from old days!

## Polygons
A polygon is a series of line that creates a closed shape.

- Side: A line from point to point
- Vertex: Where two points meet
- Polgygon: The complete shape of closed lines

There are several types of Polygons:

- Regular - Equiangular and Equilateral (below).
- Equiangular - All angles are equal
- Equilateral - All sides are equal length
- Convex - You could only draw a straight line through it and touch two sides. (Line a Stop Sign)
- Concave - You can draw a straight line and touch more than two sides (Like a Mountain Top with a line)

There are some Polygon Names:

- Special Polygons
    - Quadrilaterals
        - square
        - rhombus
        - parallelogram
        - rectangle
        - trapezoid
    - Triangles
        - right
        - equilateral
        - isosceles
        - scalene
        - acute
        - obtuse

- Polygon Names based on vertexes
    - n: N-gon
    - 2: __(Obviously 2 lines can't make a polygon :) )__
    - 3: triangle
    - 4: quadrilateral
    - 5: pentagon
    - 6: hexagon
    - 7: heptagon __(weird, never remember this)__
    - 8: Octagon
    - 9: Nonogon __(Not certain, but it's here for the sake of being numeric)__
    - 10: Decagon
    - 12: Dodecagon __(Not sure, lol)


## Area of an Object
This is how much space is taken up inside the object

#### Square
Formula: side<sup>2</sup>

    side = 5
    side ** 2

#### Rectangle
Formula: ab

    side_a = 5
    side_b = 12
    side_a * side_b

#### Circle
Formula: pi r<sup>2</sup>

Pi is the magic number, which is the diameter of a full circle (from left to right), then how
many times the diameter wraps around the circle. Which comes to 3.141~

    radius = 8
    math.pi * (radius ** 2)

#### Ellipse
Formula: pi r<sub>1</sub> r<sub>2</sub>

Since an ellipse is not a perfect circle it has two radial distances. The 1 and 2 are just for referencing radius 1 and radius 2.

    radius_1 = 8
    radius_2 = 12
    math.pi * (radius_1) * (radius_2)

#### Triangle
There are three types of triangles:

- Equilateral: All sides the same length
- Isosceles: Two sides the same length
- Scalene: All sides different lengths

For Isosceles or Scalene triangles, The formula for a triangle is: 0.5 * (base * height).

I asked my brother about this, and the tricky part to a  this is that the height is not always easy to find because
it's not necessarily the other legs length. [Example](http://www.teacherschoice.com.au/Maths_Library/Area%20and%20SA/area_74.gif)

For Equilateral Triangles, the formula is: sqrt(3)/4 * (a<sup>2</sup>). Note: sqrt(3)/4 is a fraction and we are using decimal approximation (From my brother).


## Perimeters
This is the total length of all sides added together.

#### Square
Formula: 4a

    side = 5
    area = side * 4

#### Rectangle
Formula: 2a + 2b

    side_a = 25
    side_b = 30
    result = (2 * side_a) + (2 * side_b)

#### Triangle
Formula: a + b + c

    side_a = 12
    side_b = 14
    side_c = 10
    result = side_a + side_b + side_c

#### Circle
Formula: 2pi r
Formula: pi d (Diameter)

    # With Radius
    radius = 5
    result = 2 * math.pi * radius

    # With Diameter
    diameter = 10
    result = math.pi * d


## Volumetric
This has to do with Three (3) Dimensions. Volume is like area, but in 3d space. One thing
to consider is:

- a<sup>2</sup>: means __a squared__ (or __a to the second power__)
- b<sup>3</sup>: means __b cubed__ (or __b to the third power__)

Remember, these are 3d objects now not 2d.

#### Cube
Formula: a<sup>3</sup>

    side = 5
    result = side ** 3

#### Rectangle
Formula: a b c

    side_1 = 50
    side_2 = 25
    side_3 = 30
    result = side_1 * side_2 * side_3

#### Pyramid
Formula: (1/3) bh

__Hopefully I got this right__

    base = 25
    height = 60
    result = ((1/3) * base) * height

#### Sphere
Formula: (4/3) pi r<sup>3</sup>

Like a Circle, but it's perfect

    radius = 25
    result = ((4/3) * pi) * radius ** 3

#### Ellipsoid
Formula: (4/3) pi r<sub>1</sub> r<sub>2</sub> r<sub>3</sub>

Like an Ellipse, with more radius' to factor in!

    radius_1 = 25
    radius_2 = 30
    radius_3 = 20
    result = ((4/3) * pi) * radius_1 * radius_2 * radius_3