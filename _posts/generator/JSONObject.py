import json
import numbers
import os.path
import typing
from enum import IntEnum


class NodeType(IntEnum):
    String = 0
    Number = 1
    IntNumber = 1
    RealNumber = 1
    Boolean = 2
    Null = 3
    Dictionary = 4
    Array = 5


class NodeBase:

    @property
    def type(self):
        raise NotImplementedError


class StringNode(NodeBase, str):
    text: str

    def __init__(self, text: str):
        self.text = text

    @property
    def type(self):
        return NodeType.String


class NumberNode(NodeBase):
    value: numbers.Number

    def __init__(self, value: numbers.Number):
        self.value = value

    def __repr__(self):
        return str(self.value)

    @property
    def type(self):
        return NodeType.Number


class IntNumberNode(NumberNode, int):

    @property
    def type(self):
        return NodeType.IntNumber


class RealNumberNode(NumberNode, float):

    @property
    def type(self):
        return NodeType.RealNumber


class BooleanNumberNode(NumberNode, int):

    @property
    def type(self):
        return NodeType.Boolean


class DictionaryNode(NodeBase, dict):

    def __init__(self, data: dict):
        super().__init__()
        for key, value in data.items():
            self[key] = parse_node(value)

    @property
    def type(self):
        return NodeType.Dictionary


class ArrayNode(NodeBase, list[NodeBase]):

    def __init__(self, array: list):
        super().__init__()
        for item in array:
            self.append(parse_node(item))

    @property
    def type(self):
        return NodeType.Array


def parse_node(data: typing.Union[str, int, float, bool, None, dict, list]) -> typing.Union[NodeBase, None]:
    if isinstance(data, str):
        return StringNode(data)
    elif isinstance(data, bool):
        return BooleanNumberNode(data)
    elif isinstance(data, numbers.Integral):
        return IntNumberNode(data)
    elif isinstance(data, numbers.Real):
        return RealNumberNode(data)
    elif isinstance(data, dict):
        return DictionaryNode(data)
    elif isinstance(data, list):
        return ArrayNode(data)
    elif data is None:
        return None
    else:
        raise ValueError('{} is not JSON serializable')


class JSONObject(DictionaryNode):

    @typing.overload
    def __init__(self, data: dict):
        super().__init__(data)

    @typing.overload
    def __init__(self, fp):
        pass

    @typing.overload
    def __init__(self, filePath: str):
        pass

    def __init__(self, data: typing.Union[dict, str, typing.Any]):
        """Constructor of JSONObject

        Parameters
        ----------
        data : typing.Union[dict, str, typing.Any]
            Data provided for the JSON object, it could be a dictionary object, a string specify the file path of the
            Json file, or a file object that will be passed to json.load()
        """
        if isinstance(data, str):
            if not os.path.exists(data):
                raise FileNotFoundError('File {} not found'.format(data))
            with open(data, 'r+', encoding='utf-8') as file:
                data = json.load(file)
        elif not isinstance(data, (dict, str)):
            data = json.load(data)
        super().__init__(data)

    @classmethod
    def parse(cls, data: typing.Union[dict, str, typing.Any]):
        """Parse the Json object

        Parameters
        ----------
        data : typing.Union[dict, str, typing.Any]
            Data provided for the JSON object, it could be a dictionary object, a string specify the file path of the
            Json file, or a file object that will be passed to json.load()

        Returns
        -------
        obj : JSONObject
            A JSONObject object
        """
        return cls(data)
