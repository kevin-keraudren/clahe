Cython interface to CLAHE (Graphics Gems IV)
==================================

This is a cython wrapper for the C code of CLAHE (Contrast Limited Adaptive
Histogram Equalization), available from "Graphics Gems IV". This is an
alternative to contrast-stretch, it slides a window over the image and locally
stretches the contrast while respecting a constraint on authorized gradient
jumps.

Example
-------

``python example.py``        

Raw image and simple contrast-stretch:        
<img src="nuclei.png" width="300"> &nbsp; <img src="contrast_stretched.png" width="300">

CLAHE with 2x2 window:     
<img src="result_2.png" width="300">

CLAHE with 5x5 window:     
<img src="result_5.png" width="300">

CLAHE with 20x20 window:     
<img src="result_20.png" width="300">

CLAHE with 50x50 window:     
<img src="result_50.png" width="300">


Reference
---------
ANSI C code from the article         
"Contrast Limited Adaptive Histogram Equalization"        
by Karel Zuiderveld, karel@cv.ruu.nl       
in "Graphics Gems IV", Academic Press, 1994       
