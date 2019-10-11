## zelbet - basic concrete reinforcement calculator
The idea of this project is to learn python and to help Civil Engineering students.
Project made by student for students. I do not recommend using it to real projects.

This program is easier to understand how do reinforcement wotks than Robot Structural Analysis or AxisVM, where we can do this automatically.
With this calculator you can easily check what is important when we want to reinforce some pillars. The most important factors are compressive force and bending moment, which are causing eccentricity. Eccentricity can strongly reduce compression of concrete and increase steel reinforcement extension.

### Based on EN 1992-1-1: Eurocode 2: Design of concrete structures

To do list:
-[x] check and fix symmetric reinforcement
-[x] check and fix asymmetric reinforcement
-[] check diagnostic of reinforcement

### Basic values:
- Es = 200,000 MPa
- fyd = 434.78 MPa
- Epsilon c3 = 0.00175
- Epsilon cu3 = 0.0035
- Alpha c = 1.0
- Gamma c = 1.4

###Used libraries:
- numpy - roots, polynomials
- tkinter - GUI
