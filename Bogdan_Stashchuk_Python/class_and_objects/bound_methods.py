class Comment:
    def __init__(self, text):
        self.text = text
        self.votes_qnt = 0

    def upvote(self):
        self.votes_qnt += 1


first_comment = Comment("First comment")
print()
print(first_comment.upvote)
print()
print(type(first_comment))
print()
print()
print(Comment.upvote)
# Comment.upvote()
# TypeError: Comment.upvote() missing 1 required
# positional argument: 'self'
print("----------------")
print("----Right_way---")
print("----------------")
first_comment.upvote()
print(first_comment.votes_qnt)
Comment.upvote(first_comment)
print(first_comment.votes_qnt)

print("----------------")

# first_comment=>Comment=>object
print("first_comment=>Comment=>object")
print("----------------")
print(Comment)
print(object)
print("----------------")
print(isinstance(first_comment, Comment), "first_comment vs comment")
print(isinstance(first_comment, object), "first_comment vs object")
print(isinstance(Comment, object), "Comment vs object")
print("----------------")
