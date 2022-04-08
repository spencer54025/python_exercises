class Html:
    def __init__(self, content):
        self.content = content
    def render(self):
        raise NotImplementedError('subclass mush implement render method')

class Heading(Html):
    def render(self):
        return f'<h1>{self.content}</h1>'

class Div(Html):
    def render(self):
        return f'<div>{self.content}</div>'

tags = [
    Div('some content'),
    Heading('some big heading'),
    Div('another div')
]

for tag in tags:
    print(tag.render())