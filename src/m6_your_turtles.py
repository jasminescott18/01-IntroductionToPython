"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Amanda Stouder,
         their colleagues and Jasmine Scott
"""
###############################################################################
# COMPLETED: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# COMPLETED: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################
import rosegraphics as rg
window = rg.TurtleWindow()

son_goku = rg.SimpleTurtle('arrow')
son_goku.pen = rg.Pen('orange',5)
son_goku.speed = 2

for k in range(3):

    son_goku.forward(100)
    son_goku.pen_up()
    son_goku.right(90)
    son_goku.forward(50)
    son_goku.pen_down()
    son_goku.right(90)
    son_goku.forward(100)
    son_goku.pen_up()
    son_goku.left(90)
    son_goku.forward(50)
    son_goku.left(90)
    son_goku.pen_down()

prince_vegeta = rg.SimpleTurtle('arrow')
prince_vegeta.pen = rg.Pen('blue',5)
prince_vegeta.speed = 2

prince_vegeta.right(90)
prince_vegeta.pen_up()
prince_vegeta.forward(25)

for k in range(3):

    prince_vegeta.pen_down()
    prince_vegeta.left(90)
    prince_vegeta.forward(100)
    prince_vegeta.pen_up()
    prince_vegeta.right(90)
    prince_vegeta.forward(50)
    prince_vegeta.pen_down()
    prince_vegeta.right(90)
    prince_vegeta.forward(100)
    prince_vegeta.pen_up()
    prince_vegeta.left(90)
    prince_vegeta.forward(50)

window.close_on_mouse_click()