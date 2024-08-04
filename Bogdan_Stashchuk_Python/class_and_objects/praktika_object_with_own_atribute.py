class Comment:
    def __init__(self, text, initial_votes_qnt=0):
        self.text = text
        self.votes_qnt = initial_votes_qnt

    def upvote(self, qnt):
        self.votes_qnt += qnt

    def reset_comment_qnt(self):
        self.votes_qnt = 0


my_comment = Comment('My comment')
print(my_comment)
print(type(my_comment))
print(my_comment.__dict__)
print()
print(dir(my_comment))
print()
print(my_comment.text)
print(my_comment.votes_qnt)
my_comment.upvote(5)
print(my_comment.votes_qnt)

my_comment.upvote = 10
print(my_comment.__dict__)
print()
print(dir(my_comment))
print(my_comment.upvote)
print()
print("----New object----")
new_com = Comment('It is new object :)', 88)
print(new_com.text)
print(new_com.votes_qnt)

new_com.upvote(22)

print(new_com.votes_qnt)
new_com.reset_comment_qnt()
print(new_com.votes_qnt)
