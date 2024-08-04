class Comment:
    def __init__(self, text):
        self.text = text
        self.votes_qnt = 0

    def upvote(self):
        self.votes_qnt += 1

    def __add__(self1, self2):
        return (f"{self1.text} {self2.text}", self1.votes_qnt+self2.votes_qnt)

    def __eq__(self1, self2):
        if self1.text == self2.text and self1.votes_qnt == self2.votes_qnt:
            return True
        else:
            return False


first_comment = Comment("First comment")
first_comment.upvote()
print(first_comment.text)
second_comment = Comment("Second comment")
second_comment.upvote()
print(second_comment.text)

print(first_comment+second_comment)


print("--------------------")
print(dir(first_comment))
print("--------------------")
print(dir(Comment))
print("--------------------")
print("--------------------")
third_comment = Comment("First comment")
third_comment.upvote()
print(first_comment == third_comment, first_comment.text, third_comment.text)
print(first_comment == second_comment)
