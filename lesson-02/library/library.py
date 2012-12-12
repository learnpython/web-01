"""
=======
library
=======

Functions to easify dumping Python objects to JSON.

to_json
=======

Dump Python object to JSON, using pre-defined indent.

"""

import json


def to_json(var, **kwargs):
    """
    Converts ``var`` to JSON using pre-defined indent, equals to 4 spaces.
    """
    kwargs.setdefault('indent', 4)
    return json.dumps(var, **kwargs)
