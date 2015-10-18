# Motion
Computer motion requires a timer, or draw loop (Something repetitive).

## Abstract
In Physics a **Scalar** is a numeric value. A **Vector** is a Magnitude and Direction.
In programming terms, a vector is basically an array/list.

## Principal of Motion
- The code here uses `lists` from `Python`, however it translates into [X, Y] Axis.
- Imagine a square canvas of `[500, 500]`
- Imagine a circle at the top left `[0, 0]`
- Within a timer, or draw loop you would continually cause movement with incrementation:
    - **X-Axis Right** position[0] += 1
    - **X-Axis Left** position[0] -= 1
    - **Y-Axis Down** position[1] += 1
    - **Y-Axis Up** position[1] -= 1

## Motion Example
This would move the above item faster to the

    while (true):
        # Remember: [X, Y]
        # Using the indexes of [0] for X and [1] for Y
        position[0] += 1
        position[1] += 2

The example above provides motion and speed. However, the position
is always changing at the same rate `X + 1` and `Y + 1`, therefore the
`Velocity = 0`.

## Speed
Speed is determined by the distance and time.
If I am at coordinates `X = 0` and go to `Y = 100` in 10 seconds,
the speed is `10 pixels per second` with this simple formula:

    speed = distance / time

## Velocity
Velocity is the rate which an object changes positions. It must
have a direction (displacement).

If we moved the coordinates `X = 0` to `X = 100` and
increase the speed a during a `keypress`, then we have velocity.

The way this might look in `Python` is with a mimick keypress() listener:

    # Define the rate of accelleration
    acceleration = 1

    # velocity [X, Y]
    velocity = [1, 3]

    def keyboardListener(keypress):
        if keypress == 'left'
            # X moves left with negative
            velocity[0] -= acceleration
        elif keypress == 'right'
            # X moves right with negative
            velocity[0] += acceleration
        elif keypress == 'down'
            # Y moves down with postive
            velocity[1] += acceleration
        elif keypress == 'up'
            # Y moves up with negative
            velocity[1] -= acceleration

    # The loop now no longer just moves position, but applies
    # continually more accelleration
    while (true):
        position[0] += velocity[0] + acceleration
        position[1] += velocity[3] + acceleration


## Acceleration
Velocity is Independent of Acceleration.
See how it applies in the above example.

The way this might look in `Python` is with a mimick keypress() listener:

## Friction
Causes things in motion to slow down at a constant rate.


    @ TODO


## Collision
Detects the position/shape (Radius for example) of two items.

Two circles