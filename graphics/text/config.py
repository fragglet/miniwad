# SPDX-License-Identifier: BSD-3-Clause
#
# Configuration file for textgen. This file defines the graphic lumps
# that are generated, and the text to show in each one.
#

white_graphics = {
	'm_doom': 'miniwad',

	'wibp1': 'P1',
	'wibp2': 'P2',
	'wibp3': 'P3',
	'wibp4': 'P4',
	'wicolon': ':',
	'm_skull1': '>',
	'm_skull2': '>',
}

white_graphics.update({
	'cwilv%02d' % i: '%d' % (i + 1) for i in range(32)
})

red_graphics = {
	'm_disopt': '',
	'm_episod': 'Episode:',
	'm_optttl': '',
	'm_skill': 'Skill:',

	'm_ngame': 'New',
	'm_option': 'Opts',
	'm_loadg': 'Load',
	'm_saveg': 'Save',
	'm_rdthis': 'Help',
	'm_quitg': 'Quit',

	'm_newg': '',
	'm_epi1': '1',
	'm_epi2': '2',
	'm_epi3': '3',
	'm_epi4': '4',

	'm_jkill': '1',
	'm_rough': '2',
	'm_hurt': '3',
	'm_ultra': '4',
	'm_nmare': '5',

	'm_lgttl': '',
	'm_sgttl': '',

	'm_endgam': 'End',
	'm_messg': 'Msgs:',
	'm_msgoff': 'off',
	'm_msgon': 'on',
	'm_msens': 'Mouse',
	'm_detail': 'Detail:',
	'm_gdhigh': 'high',
	'm_gdlow': 'low',
	'm_scrnsz': 'Screen Size',

	'm_svol': 'Sound',
	'm_sfxvol': 'Sfx',
	'm_musvol': 'Music',
	'm_lsleft': '[',
	'm_lsrght': ']',
	'm_therml': '[',
	'm_thermr': ']',
	'm_thermo': '|',

	'wif': '',
	'wiostk': 'kills',
	'wiosti': 'items',
	'wiscrt2': 'secret',
	'wiosts': 'scrt',
	'wifrgs': 'frgs',

	'witime': 'Time:',
	'wisucks': 'sucks',
	'wimstt': 'Total:',
	'wipar': 'Par:',
	'wip1': 'P1', 'wip2': 'P2', 'wip3': 'P3', 'wip4': 'P4',
	'wiostf': 'f.',
	'wimstar': 'you',
	'winum0': '0', 'winum1': '1', 'winum2': '2', 'winum3': '3',
	'winum4': '4', 'winum5': '5', 'winum6': '6', 'winum7': '7',
	'winum8': '8', 'winum9': '9',
	'wipcnt': '%',
	'wiminus': '-',
	'wienter': '',

	'm_pause': 'pause',
	'sttnum0': '0', 'sttnum1': '1', 'sttnum2': '2', 'sttnum3': '3',
	'sttnum4': '4', 'sttnum5': '5', 'sttnum6': '6', 'sttnum7': '7',
	'sttnum8': '8', 'sttnum9': '9',

}

red_graphics.update({
	'stcfn%03d' % i: ('%c' % i).lower()
	for i in list(range(33, 96)) + [123, 124, 125]
})

