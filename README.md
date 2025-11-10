# Visual Proof of the 2D Determinant Formula

This project provides a **visual illustration and geometric proof** of the 2×2 determinant formula using **Manim** (`manimlib` version).

\begin{vmatrix}
a & c \\
b & d
\end{vmatrix}
'=
\begin{vmatrix}
a & c \\
0 & d
\end{vmatrix}
+
\begin{vmatrix}
0 & c \\
b & d
\end{vmatrix}

The animation shows how the determinant, representing the **signed area** of a parallelogram formed by two vectors, can be expressed as the sum of areas corresponding to the vector's x- and y-components.  

Some steps use properties of projections that are not elaborated in the animation.

---

## Overview

The video begins with two vectors in the plane:
\[
\vec{u} = (a, b), \quad \vec{v} = (c, d)
\]

It constructs the parallelogram formed by these vectors, whose signed area equals \( ad - bc \). The animation then shows how this area can be split into two simpler parallelograms corresponding to the x- and y-components of \(\vec{u}\).

This illustrates the determinant's **linearity** property:
\[
\det(\vec{u}, \vec{v}) = \det(\text{x-component of } \vec{u}, \vec{v}) + \det(\text{y-component of } \vec{u}, \vec{v}).
\]

---

## Requirements

- [Manim](https://github.com/3b1b/manim) (original version using `manimlib`)  
- Python 3.7 or higher recommended  
- Optional: FFmpeg (for video export)
