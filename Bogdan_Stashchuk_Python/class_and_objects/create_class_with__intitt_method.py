class Comment:
    def __init__(self, text):
        self.text = text
        self.votes_qnt = 0

    def upvote(self):
        self.votes_qnt += 1


c = Comment('This is norm water')
print(c)
print(c.votes_qnt)
c.upvote()
print(c.votes_qnt)
print(c.text)

print()
print(c.__dict__)
print()
print(dir(c))
