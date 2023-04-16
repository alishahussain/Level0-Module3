from tkinter import simpledialog, messagebox, Tk
import webbrowser


# Use this function to play a video from the internet
def play_video(url):
    webbrowser.open(url)

# =================== DO NOT MODIFY THE CODE ABOVE ===========================


if __name__ == '__main__':
    # TODO 1) Make a new window variable, window = Tk()
    window = Tk()
    #      2) Hide the window using the window's .withdraw() method
    window.withdraw()
    #      3) Ask the user how many cats they have
    ask = simpledialog.askinteger(title=None, prompt='how many cats do you have?')
    #      4) If they have 3 or more cats, tell them they are a crazy cat lady
    if ask >= 3:
        messagebox.showinfo(title=None,message='youre a crazy cat lady!')
    #      5) If they have less than 3 cats AND more than 0 cats, call the
    #         play_video function below to show them a cat video
    if ask<3 and ask>0:
        play_video('https://www.youtube.com/watch?v=wkH9aQXep2s')
    #      6) If they have 0 cats, show them a video of A Frog Sitting on a
    #         Bench Like a Human
    if ask == 0:
        play_video('https://www.youtube.com/watch?v=oj_yLBltPE8')
    pass
