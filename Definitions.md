<!--StartFragment-->

**Mode** - Faces, Joints, Edges, Bodies, etc.
This mode defines which type of object is given decorators


**Base Target** - A decorated item.


**Target Set -** A list of items, can be grabbed using “and” or by using a command like “\[face] edges” to grab the edges of a face


**View Commands -** 
Option to use anatomical or directional terms. Chaining terms will add resultant vector
|                  |                 |            |
| ---------------- | --------------- | ---------- |
| **Anatomical**   | **Directional** | **Result** |
| Dext (Dextal)    | Right           | \[1,0,0]   |
| Sin (Sinister)   | Left            | \[-1,0,0]  |
| Soup (Superior)  | Top             | \[0,1,0]   |
| Inf (Inferior)   | Bottom          | \[0,-1,0]  |
| Ant (Anterior)   | Front           | \[0,0,1]   |
| Post (Posterior) | Back            | \[0,0,-1]  |

**Focus** - Makes target origin for camera rotation


**Gui Commands -** 
Commands that relate to Fusion360 but not to a model


**Modifiers -** 
Actions that modify a target: Extrude, Rotate, Scale, etc.


**Root -** Root object of Fusion model

<!--EndFragment-->
