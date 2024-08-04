class Comment:
    total_comments = 0

    def __init__(self, text):
        self.text = text
        self.votes_qnt = 0
        Comment.total_comments += 1


first_comment = Comment("First comment")
print("First:", Comment.total_comments)
second_comment = Comment("Second comment")
print("Second:", Comment.total_comments)
print("----------")
print(first_comment.__dict__)
print("----------")
first_comment.total_comments = 10
print(first_comment.__dict__)
print("----------")
print(first_comment.total_comments)
print(Comment.total_comments)
print("----------")
print(Comment.__dict__)

print("----------")


Comment.total_comments = 99

print("Comment.tot:", Comment.total_comments)
print("second_com:", second_comment.total_comments)
print("first_com:", first_comment.total_comments)
