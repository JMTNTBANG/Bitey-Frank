from os import listdir

__all__ = []

for command in listdir('commands'):
    if command.endswith('py'):
        __all__.append(command[:-3])