import os
import symbol
import token
import json

SYMBOL_MAP = symbol.sym_name
TOKEN_MAP = token.tok_name

class Serializable():
    def __expr__(self):
        return self.__str__()

    def __str__(self):
        return __name__

class SourceType():
    SUITE = 'suite'
    EXPR = 'expr'
    UNDEFINED = 'undefined_source'

    @classmethod
    def get_source_type(cls, source_type):
        if source_type == "suite":
            return cls.SUITE
        elif source_type == "expr":
            return cls.EXPR
        else:
            return cls.UNDEFINED

class Source:
    def __init__(self, source_type=None, source=None):
        source_type = SourceType.UNDEFINED if source_type == None else source_type
        source = str() if source == None else source

        self.source_type = source_type
        self.source = source

    @staticmethod
    def get_source_from_string(source_type, source):
        if type(source_type) != str:
            raise TypeError("Source type must have string type")
        if type(source) != str:
            raise TypeError("Source must have string type")

        source_type = SourceType.get_source_type(source_type)
        if source_type == SourceType.UNDEFINED:
            raise ValueError("Could not identify the given source type, should be 'expr' or 'suite'")

        return Source(source_type, source)

    @staticmethod
    def get_source_from_file_path(source_type, file_path):
        if type(source_type) != str:
            raise TypeError("Source type must have string type")
        if type(file_path) != str:
            raise TypeError("File path must have string type")

        if not os.path.exists(file_path):
            raise ValueError("No file was found by given file path")

        source_type = SourceType.get_source_type(source_type)
        if source_type == SourceType.UNDEFINED:
            raise ValueError("Could not identify the given source type, should be 'expr' or 'suite'")

        with open(file_path, "r") as raw_source:
            source = raw_source.read()
        
        return Source(source_type, source)

class NodeType():
    TOKEN = 'token'
    SYMBOL = 'symbol'
    UNDEFINED = 'undefined_node'

    @classmethod
    def get_node_type(cls, type_str):
        if type_str == "token": 
            return cls.TOKEN
        elif type_str == "symbol":
            return cls.SYMBOL
        else:
            return cls.UNDEFINED

class Node:
    def __init__(self, node_type=None, const=None, value=None):
        node_type = NodeType.UNDEFINED if node_type == None else node_type
        value = [] if value == None else value

        self.node_type = node_type
        self.const = const
        self.value = value

    def to_dict(self):
        temp = dict()
        temp["type"] = str(self.node_type)
        temp["name"] = str(self.const)

        if self.node_type == NodeType.TOKEN:
            temp["value"] = self.value
        else:
            children = list()
            for idx in range(0, len(self.value)):
                if type(self.value[idx]) != Node:
                    raise TypeError("Symbol node must have nodes in value list")
                children.append(self.value[idx].to_dict())
            temp["value"] = children

        return temp

    def to_json(self, indent=4):
        gen_dict = self.to_dict()
        return json.dumps(gen_dict, indent=indent)
            
    @staticmethod
    def get_node_from_raw(node_type, const, value):
        if type(node_type) != str: 
            raise TypeError("Node must have node type with string type")
        if type(const) != str: 
            raise TypeError("Node must have constant with string type")
        if type(value) != str and type(value) != list: 
            raise TypeError("Node must have value with string or list type")

        node_type = NodeType.get_node_type(node_type)
        if node_type == NodeType.UNDEFINED:
            raise ValueError("Could not identify the given node type, should be 'token' or 'symbol")
        
        if node_type == NodeType.TOKEN:
            if type(value) != str:
                raise ValueError("Token must have value with string type")
        else:
            if type(value) != list:
                raise ValueError("Symbol must have value with list type")

        return Node(node_type, const, value)