__all__ = []

import pkgutil
import importlib
import inspect


'''
Little script that load every messages in the directory:
    - just call : from Packets.Messages.Server import *
    and every packets class will be callable (e.g: LoginOk() )

'''
for loader, name, is_pkg in pkgutil.walk_packages(__path__, prefix=__name__ + '.'):
    module = importlib.import_module(name)

    for attr_name, value in inspect.getmembers(module):
        if attr_name.startswith('__'):
            continue

        globals()[attr_name] = value
        __all__.append(attr_name)