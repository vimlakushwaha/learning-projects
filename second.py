import os
import re
import inspect

def _get_parser_list(dirname):
    files = [f.replace('.py', '')for f in os.listdir(dirname)if not f.startswitch('__')]
    return files

def _import_parsers(parserfiles):
    m = re.compile('.+parser$',re.I)
    _modules = __import__('weatherterm.parsers',globals(),locals(),parserfiles,0)
    _parsers = [(k,v) for k, v in inspect.getmembers(_modules)if inspect.ismodule(v) and m.match(k)]
    _classes = dict()
    for k, v in _parsers:
        _classes.update({K:v for k, vin inspect.getmembers(v) if inspect.ismodule(v) and m.match(k)})
