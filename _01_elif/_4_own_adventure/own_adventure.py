from tkinter import simpledialog, messagebox, Tk
if __name__ == '__main__':

# TODO Tell the user a story, but give them options so they can decide the
#  path of the plot.
#  Use pop-ups, if statements, and your imagination to make an interesting
#  story
    window = Tk()
    window.withdraw()
    messagebox.showinfo(title=None, message='once upon a time, there was a royal family, and the prince was looking for a wife. In this story, you are the princes (James) mother, Elizabeth. You will be asked questions, and will reply with yes or no.')
    q1 = simpledialog.askstring(title=None, prompt='there is a terrible storm going on right now. you hear a knock at the door. will you open it?')
    if q1 =='yes':
        messagebox.showinfo(title=None, message='You open the door. There is a girl drenched in water and mud. She looks horrid!')
    if q1 =='no':
        messagebox.showinfo(title=None, message='you chose to ignore the knock and go on with your life. This is the end of your journey!')
        exit()
    q2 = simpledialog.askstring(title=None, prompt='the girl tells you that her name is mary. she claims that she is a princess in a faraway land and begs for you to let her stay the night, and shell do anything for you. You dont believe that she is a princess. Will you let her stay?')
    if q2 =='yes':
        messagebox.showinfo(title=None, message='you ignore your instinct, and let mary come inside. You tell her to wait in the main room while you prepare her bedroom.')
    if q2 == 'no':
        messagebox.showinfo(title=None, message='you tell mary that you cannot allow her to stay the night because she is extremely dirty. You wish her well and give her directions to the nearest hotel. This is the end of your journey!')
        exit()
    q3 = simpledialog.askstring(title=None, prompt='when you are preparing marys room, you decide that you can give her a test to see if shes actually a princess. real princesses can feel even the slightest inconvenience, so if you put a tiny thing at the bottom of her mattress, surely she will notice. If she really is a princess, James can marry her. Will you put a pea at the bottom of marys 30 mattresses?')
    if q3 =='yes':
        messagebox.showinfo(title=None, message='you grin deviously and carry on with the plan. When you are done, you go outside and invite Mary to her room. You can see that shes already been acquainted with the prince, so the plan is already going well! youre such a genius')
    if q3 == 'no':
        messagebox.showinfo(title=None, message='you decide that you will let mary have her own privacy, and you wont test her. In the morning she thanks you and gives you lots of money. You still have no idea if shes a princess or not, so you send her away. This is the end of your journey!')
        exit()
    messagebox.showinfo(title=None, message='in the morning, you see Mary walk out of her room. You invite her to breakfast and inquire about her sleep. She looks at you gratefully and thanks you for letting her stay. She then apologizes for being rude, but tells you that she had the worst sleep of her life. There was a lump on the bed bothering her the whole night! ')
    q4 = simpledialog.askstring(title=None, prompt='your plan worked! Mary uis a princess! Will you ask her to  marry your son?')
  if q3 =='yes':
        messagebox.showinfo(title=None, message='Mary agrees, and they live happily ever after! This is the end of your journey!')
    if q3 == 'no':
        messagebox.showinfo(title=None, message='at least you found out that shes a princess. This is the end of your journey!')
        exit()
