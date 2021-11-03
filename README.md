# cube-solver

## Cube Notation

The faces are named `U,D,L,R,F,B` (for up, down, left, right, front, back).

Moves can be described in the following format:
- X (rotate face X clockwise, 90º)
- X2 (rotate face X 180º)
- X' (rotate face X anticlockwise, 90º)

The initial configuration of a cube can be described by a string, such as:
```
"DRLUUBFBRBLURRLRUBLRDDFDLFUFUFFDBRDUBRUFLLFDDBFLUBLRBD"
```
The idea is that each face of solved cube has a colour uniquely determined by the square in its center. If we have a shuffled cube, the center square of each face will remain as in the start. We read the squares in the order:
```
U1, U2, U3, U4, U5, U6, U7, U8, U9, R1, R2, R3, R4, R5, R6, R7, R8, R9, F1, F2, F3, F4, F5, F6, F7, F8, F9, D1, D2, D3, D4, D5, D6, D7, D8, D9, L1, L2, L3, L4, L5, L6, L7, L8, L9, B1, B2, B3, B4, B5, B6, B7, B8, B9
```
We look at square `U1` and see what colour it has. Then the first element of the string will be labelled by the face which has said colour.
We look at square `U2` and see what colour it has. Then the second element of the string will be labelled by the face which has said colour.

For example, using the string above, we know that square `U1` has the colour corresponding with the down (`D`) face; square `U2`will have the colour corresponding to the right (`R`) face; etc ... .


## Kociemba Algorithm

We are using the **Kociemba Algorithm**, in particular [this](https://pypi.org/project/kociemba/) Python implementation.
For more details on Kociemba, see [this](https://www.jaapsch.net/puzzles/compcube.htm#:~:text=larger%20pruning%20tables.-,Kociemba%27s%20Algorithm,-All%20the%20discussion).

## Cube Pictures

https://www.kaggle.com/sebastianponce/rubiks-cubes-faces?select=WhatsApp+Image+2021-02-16+at+7.56.49+PM+%284%29.jpeg
