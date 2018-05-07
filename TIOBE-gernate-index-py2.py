#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python 2.7
# TIOBE-gernate-index-py2.py

_index = 'TIOBE-index.html'
_templateData = \
	'PCFkb2N0eXBlIGh0bWw+DQo8aHRtbCBsYW5nPSJlbiI+DQo8aGVhZD4NCjxtZXRhIGNoYXJzZXQ9IlVU' \
	'Ri04Ij4NCjxtZXRhIG5hbWU9IkdlbmVyYXRvciIgY29udGVudD0iRWRpdFBsdXPCriI+DQo8dGl0bGU+' \
	'VElPQkUgSW5kZXg8L3RpdGxlPg0KPC9oZWFkPg0KPGJvZHk+DQoNCjxoMT5USU9CRSBJbmRleDwvaDE+' \
	'DQoNCjx1bCBpZD0ibGlzdCI+PC91bD4NCg0KPC9ib2R5Pg0KPC9odG1sPg0K'

_skipFiles = [ _index, '.git', 'TIOBE-gernate-index-py2.py', 'TIOBE-exchange-matrix-data.py']

import base64, os

_template  = base64.b64decode( _templateData )
_files = os.listdir('.')

# with open('aa.txt', 'wb') as fo:
# 	_data = base64.b64encode(_template.replace('Pa Utils JS 2017', 'TIOBE Index'))
# 	fo.write(' \\\n'.join([ '\'' + _data[i: i + 80] + '\'' for i in xrange(0, len(_data), 80) ]))

print _template
print _files

with open(_index, 'w') as fo:
	fo.write(
		_template.replace('<ul id="list"></ul>',
			'<ul id="list">\n' +
			 '\n'.join( [ '\t<li><a href="%s">%s</a></li>' % (f, f) for f in _files if f not in _skipFiles ] ) +
			'\n</ul>'
		)
	)
