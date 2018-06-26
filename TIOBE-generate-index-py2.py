#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python 2.7
# TIOBE-gernate-index-py2.py

import base64, os, re

_index = 'TIOBE-index.html'

def TIOBE_gernate_index():

	_templateData = \
		'PCFkb2N0eXBlIGh0bWw+DQo8aHRtbCBsYW5nPSJlbiI+DQo8aGVhZD4NCjxtZXRhIGNoYXJzZXQ9IlVU' \
		'Ri04Ij4NCjxtZXRhIG5hbWU9IkdlbmVyYXRvciIgY29udGVudD0iRWRpdFBsdXPCriI+DQo8dGl0bGU+' \
		'VElPQkUgSW5kZXg8L3RpdGxlPg0KPC9oZWFkPg0KPGJvZHk+DQoNCjxoMT5USU9CRSBJbmRleDwvaDE+' \
		'DQoNCjx1bCBpZD0ibGlzdCI+PC91bD4NCg0KPC9ib2R5Pg0KPC9odG1sPg0K'

	_month = {
		'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
		'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December':12
	}

	_skipFiles = [ _index, '.git', 'TIOBE-gernate-index-py2.py', 'TIOBE-exchange-matrix-data.py']

	_template  = base64.b64decode( _templateData )

	_files = os.listdir('.')

	# with open('aa.txt', 'wb') as fo:
	# 	_data = base64.b64encode(_template.replace('Pa Utils JS 2017', 'TIOBE Index'))
	# 	fo.write(' \\\n'.join([ '\'' + _data[i: i + 80] + '\'' for i in xrange(0, len(_data), 80) ]))

	print _template
	print '\n'.join( _files )
	print '\n'

	n = 0
	_list = []
	for _file in _files:
		if _file not in _skipFiles:
			m = re.findall('TIOBE Index for ([A-Za-z]+)\s+([0-9]+)\.html', _file)
			if m:
				_list.append([_file, int(m[0][1]) * 100 + _month[m[0][0]]])
				# print _file, m
			else:
				_list.append([_file, n])
				n += 1

	def takeSecond(el):
		return el[1]

	_list.sort(key=takeSecond)

	# print _list
	print '\n'.join( [ f[0] for f in _list] )

	with open(_index, 'w') as fo:
		fo.write(
			_template.replace('<ul id="list"></ul>',
				'<ul id="list">\n' +
				 # '\n'.join( [ '\t<li><a href="%s">%s</a></li>' % (f, f) for f in _files if f not in _skipFiles ] ) +
				 '\n'.join( [ '\t<li>%s<a href="%s">%s</a></li>' % (str(f[1]) + ' ' if f[1] > 2000 else '', f[0], f[0]) for f in _list ] ) +
				'\n</ul>'
			)
		)

if __name__ == '__main__':

	TIOBE_gernate_index()
