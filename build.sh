#!/bin/bash
rm -f miniwad.wad
deutex -iwad \
       -flats -patches -textures \
       -graphics -levels -lumps \
       -musics -sounds -textures \
       -sprites \
       -build wadinfo.txt miniwad.wad

