#!/usr/bin/env python

from PIL import Image

from glob import glob
import colorsys
import sys

PALETTE = [
	(0x00, 0x00, 0x00),     # black
	(0x97, 0x97, 0x97),     # light grey
	(0x43, 0x43, 0x43),     # dark grey
	(0x33, 0x2b, 0x13),     # dark brown
	(0x77, 0x5f, 0x4b),     # light brown
	(0x00, 0x00, 0xb3),     # blue
	(0x73, 0x00, 0x00),     # red
	(0x2f, 0x37, 0x1f),     # grass green
]

def color_code(rgb):
	return "#%02x%02x%02x" % rgb

def rgb_to_hsv(rgb):
        return colorsys.rgb_to_hsv(float(rgb[0]), float(rgb[1]), float(rgb[2]))

def nearest(needle, haystack):
	#print("Finding %s" % (color_code(needle)))
	nh, ns, nv = rgb_to_hsv(needle)
	min_diff = sys.maxint
	min_idx = -1
	for i, rgb in enumerate(haystack):
		h, s, v = rgb_to_hsv(rgb)
		# Hue matters less when unsaturated or dark.
		hdiff = (nh - h) * ns * nv * 8 / 256.0
		sdiff = (ns - s) * nv / 256.0
		vdiff = (nv - v) / 128.0
		diff = hdiff*hdiff + sdiff*sdiff + vdiff*vdiff
		#print("%s, diff %f" % (color_code(rgb), diff))
		#print("\t%.3f, %.3f, %.3f" % (hdiff, sdiff, vdiff))
		if diff < min_diff:
			min_diff = diff
			min_idx = i
	#print("Winner is %s with %f" % (color_code(PALETTE[min_idx]), min_diff))
	return min_idx

def squashed_image(im, darken=False):
	im = im.convert('RGB')
	rtotal, gtotal, btotal = 0, 0, 0
	for y in range(im.height):
		for x in range(im.width):
			r, g, b = im.getpixel((x, y))
			rtotal += r
			gtotal += g
			btotal += b
	npixels = im.width * im.height
	rgb = (
		float(rtotal) / npixels,
		float(gtotal) / npixels,
		float(btotal) / npixels,
	)
	fillrgb = PALETTE[nearest(rgb, PALETTE)]
	if darken:
		fillrgb = (
			int(fillrgb[0] * 0.9),
			int(fillrgb[1] * 0.9),
			int(fillrgb[2] * 0.9),
		)
	return Image.new('RGB', (im.width, im.height),
	                 color=fillrgb)

files = glob("src/*/*.png")
for filename in files:
	im = Image.open(filename)
	im = squashed_image(im, "/flats/" in filename)
	outfile = filename[4:]
	print(outfile)
	im.save(outfile)

