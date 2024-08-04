class Comment:
    def __init__(self, text):
        self.text = text

    @staticmethod
    def merge_comments(first, second):
        return f"{first},{second}"


my_comment = Comment("My comment")
m_1 = Comment.merge_comments("Thanks!", "Excelent.")
print(m_1)
m_2 = my_comment.merge_comments("Great", "OK")
print(m_2)
print("------------")
m_3 = my_comment.merge_comments(my_comment.text, "Great")
print(m_3)
print("------------")
print(my_comment.text)

print("------------")
m_4 = Comment.merge_comments(
    my_comment.text, "is very good but this comment is awesome!")
print(m_4)
print("------------")
print("id m1 is:", id(m_1))
print("id m2 is:", id(m_2))
print("id m3 is:", id(m_3))
print("id m4 is:", id(m_4))

if m_1 is m_2 or m_2 is m_3 or m_3 is m_4:
    print("Here is identical object!!!")
