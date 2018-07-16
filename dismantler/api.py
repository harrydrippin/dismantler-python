from .dismantler import Dismantler
from .models import Node, Source, SourceType

def run_from_string(source, src_type='expr'):
    """Dismantle given string to node tree.

    Positional arguments:
    source -- expression string

    Keyword arguments:
    type -- 'suite' or 'expr' (default 'expr')

    Usage:
        >>> import dismantler
        >>> dismantler.run_from_string('a + 5')
    """
    if type(source) != str:
        raise TypeError("Source must be string")

    source = Source.get_source_from_string(src_type, source)

    return Dismantler(source)

def run_from_file(file_path, src_type='suite'):
    """Dismantle given file to node tree.

    Positional arguments:
    file_path -- file path

    Keyword arguments:
    type -- 'suite' or 'expr' (default 'suite')

    Usage:
        >>> import dismantler
        >>> dismantler.run_from_file('source.py')
    """
    if type(file_path) != str:
        raise TypeError("Source must be string")

    source = Source.get_source_from_file_path(src_type, file_path)

    return Dismantler(source)

