from tkinter import Tk, simpledialog, messagebox


if __name__ == '__main__':
    # TODO: Look at the AreYouHappy.png image
    #       Use pop-ups to recreate the chart using if and elif statements
    window = Tk()
    window.withdraw()
    happy = simpledialog.askstring(title='', prompt='are you happy?')
    if happy == 'yes':
        messagebox.showinfo(title='', message='Keep doing whatever youre doing')
    if happy == 'no':
        q2 = simpledialog.askstring(title='', prompt='do you want to be happy?')
        if q2 == 'yes':
            messagebox.showinfo(title='', message='change something')
        if q2 == 'no':
            messagebox.showinfo(title='', message='Keep doing whatever youre doing')
    pass
