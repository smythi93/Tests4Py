The bug in PySnooper 2 does occur whenever the snoop function/decorator was used with the keyword `custom_repr`. The
keyword expects a tuple of a predicate and a transformer and applies the transformer whenever the predicate holds for
a traced variable.