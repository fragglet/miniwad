# Minimal Doom IWAD

What's the smallest a Doom IWAD can be while still being vaguely playble?
An exercise in minimalism.

The result is a WAD file less than a quarter of a megabyte that can in
theory be used to play any WAD from the idgames archive.

Features:

* Flat-shaded walls and floors
* An assortment of identical looking enemies that look like
  creepy silhouettes
* Nine variations of the same gun
* Two sound effects
* No music
* No real levels (Bring Your Own Levels)
* Usable menus!
* Minimalist status bar

## How?

The whole WAD is built to take advantage of
[wadptr](https://soulsphere.org/projects/wadptr/)'s merging features,
specifically:

* Multiple copies of the same lump are merged. The textures are reduced to
  a very small color palette so that many of them will look identical and
  be merged. Similarly, the same two sound effects are reused for many
  different purposes.
* wadptr can merge identical columns within a Doom graphic. To take
  advantage of this, many of the graphics are deliberately simplistic or
  mirrored in appearance so save space.

