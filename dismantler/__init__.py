"""
Dismantler
====================

Dismantler changes the python code to parse tree, and export it to dictionary, or json.

Usage:
   >>> import dismantler
   >>> d = dismantler.run_from_string('a + 5').dictionary()
   >>> print(d)
   {
       "type": "symbol",
       "name": "stmt",
       "value": [
           // Nodes...
       ]
   }
   >>> d = dismantler.run_from_file('file.py').json()
   >>> print(d)
   "{
       "type": "symbol",
       "name": "stmt",
       "value": [
           // Nodes...
       ]
   }"


:copyright: Copyright 2018 Seunghwan Hong.
:license: Apache 2.0, see LICENSE for more details.
"""

from .api import run_from_file, run_from_string