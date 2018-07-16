import parser
import symbol
import token

from .models import Node, Source, SourceType

class Dismantler:
    def __init__(self, source):
        if type(source) != Source:
            raise TypeError("'source' must be instance of Source class")
        
        self._source = source
        
        if source.source_type == SourceType.SUITE:
            self._st = parser.suite(source.source)
        elif source.source_type == SourceType.EXPR:
            self._st = parser.expr(source.source)
        else:
            raise ValueError("Dismantler cannot accept any undefined values")
        
        self._code = self._st.compile()
        self._tup = self._st.totuple()
        self._token_list = list()
        self._symbol_list = list()
        self._node_tree = self.__get_node_tree()

    def dictionary(self):
        return self._node_tree.to_dict()

    def json(self, indent=4):
        return self._node_tree.to_json(indent=indent)

    def tokens(self):
        return [tok.to_dict() for tok in self._token_list]

    def symbols(self):
        return [{
            "type": "symbol",
            "name": sym.const
        } for sym in self._symbol_list]
    
    def __get_node_tree(self, recursive=False, recur_tup=None):
        temp_tup = recur_tup if recursive else self._tup

        node_type, node_name = self.__get_type_and_name(temp_tup[0])
            
        if node_type == "symbol":
            node_value = list()
            for idx in range(1, len(temp_tup)):
                node_value.append(self.__get_node_tree(recursive=True, recur_tup=temp_tup[idx]))
        elif node_type == "token":
            node_value = temp_tup[1]
        else:
            raise TypeError("Node type is undefined")

        node = Node.get_node_from_raw(node_type, node_name, node_value)

        if node_type == "token":
            self._token_list.append(node)
        else:
            self._symbol_list.append(node)
        
        return node

    def __get_type_and_name(self, origin):
        if origin in symbol.sym_name:
            return "symbol", symbol.sym_name[origin]
        elif origin in token.tok_name:
            return "token", token.tok_name[origin]
        else:
            return "undefined_node", None
