
import os
import config

def escape(s):
	return "".join(
		'\\' + c if c in "\"'\\" else c
		for c in s
	)

CMD_FORMAT = """
convert -background transparent -font Minimal5x7-Regular \
        -fill {color} -pointsize 8 \
        +antialias "label:{label}" {filename}
"""

cmds = []
for filename, text in config.red_graphics.items():
	filename = "../%s.png" % filename
	cmds.append(dict(filename=filename, label=escape(text), color="red"))
for filename, text in config.white_graphics.items():
	filename = "../%s.png" % filename
	cmds.append(dict(filename=filename, label=text, color="white"))

for cmd in cmds:
	print(CMD_FORMAT.format(**cmd))
