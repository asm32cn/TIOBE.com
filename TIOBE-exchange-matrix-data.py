#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python 2.7
#

_data = '''Apr 2018	Apr 2017	Change	Programming Language	Ratings	Change
1	1		Java	15.777%	+0.21%
2	2		C	13.589%	+6.62%
3	3		C++	7.218%	+2.66%
4	5	change	Python	5.803%	+2.35%
5	4	change	C#	5.265%	+1.69%
6	7	change	Visual Basic .NET	4.947%	+1.70%
7	6	change	PHP	4.218%	+0.84%
8	8		JavaScript	3.492%	+0.64%
9	-	change	SQL	2.650%	+2.65%
10	11	change	Ruby	2.018%	-0.29%
11	9	change	Delphi/Object Pascal	1.961%	-0.86%
12	15	change	R	1.806%	-0.33%
13	16	change	Visual Basic	1.798%	-0.26%
14	13	change	Assembly language	1.655%	-0.51%
15	12	change	Swift	1.534%	-0.75%
16	10	change	Perl	1.527%	-0.89%
17	17		MATLAB	1.457%	-0.59%
18	14	change	Objective-C	1.250%	-0.91%
19	18	change	Go	1.180%	-0.79%
20	20		PL/SQL	1.173%	-0.45%'''

_data2 = '\tvar _matrixData = [' + ',\n\t\t'.join( [ '[' + ', '.join( [ '\'' + c + '\'' for c in r.split('\t') ] ) + ']' for r in _data.split('\n')] ) + '];\n\n'
print _data2

with open('TIOBE_matrixData.txt', 'w') as fo:
	fo.write(_data2)
