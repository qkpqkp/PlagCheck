# encoding: utf-8
# module ruamel_yaml.ext._ruamel_yaml
# from C:\Users\Doly\Anaconda3\lib\site-packages\ruamel_yaml\ext\_ruamel_yaml.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import ruamel_yaml.error as __ruamel_yaml_error
import ruamel_yaml.events as __ruamel_yaml_events
import ruamel_yaml.nodes as __ruamel_yaml_nodes
import ruamel_yaml.tokens as __ruamel_yaml_tokens


class ScalarToken(__ruamel_yaml_tokens.Token):
    # no doc
    def __init__(self, value, plain, start_mark, end_mark, style=None): # reliably restored by inspect
        # no doc
        pass

    plain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    style = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    id = '<scalar>'
    __slots__ = (
        'value',
        'plain',
        'style',
    )


