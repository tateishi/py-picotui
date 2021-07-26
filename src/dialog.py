# -*- coding: utf-8 -*-

from picotui.context import Context
from picotui.dialogs import *

with Context():
    d = DTextEntry(25, "Hello, World", title="Wazzup?")
#    d = DMultiEntry(25, 5, "Hello, World".split("\n"), title="Comment:")
    res = d.result()

print(res)
