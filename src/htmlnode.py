class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props == None:
            return ""
        output = ""
        for prop in self.props:
            output += f' {prop}="{self.props[prop]}"'
        return output

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    


class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag, props)
        self.value = value

    def to_html(self):
        if self.value == None:
            raise Exception('All leaf nodes require a value')
        if self.tag == None:
            return self.value
        if self.props:
            return f"<{self.tag} {self.props_to_html(self.props)}>{self.value}</{self.tag}>"
        else: 
            return f"<{self.tag}>{self.value}</{self.tag}>"
        
