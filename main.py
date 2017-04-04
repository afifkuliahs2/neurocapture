from Tkinter import *

class NeuroCapture(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initGUI()

    def initGUI(self):
        self.parent.title("Neurosky Capture Tool")
        self.pack(fill=BOTH, expand=True)

        # Subject's Name Frame
        subjectFrame = Frame(self)
        subjectFrame.pack(fill=X)

        subjectLabel = Label(subjectFrame, text="Name :", width=6)
        subjectLabel.pack(side=LEFT, padx=5, pady=20)

        subjectEntry = Entry(subjectFrame)
        subjectEntry.pack(fill=X, padx=10, expand=True)

        # Start Button Frame
        startFrame = Frame(self)
        startFrame.pack(fill=X)

        startButton = Button(startFrame, text="Start")
        startButton.pack(fill=X, padx=10)

        # Start Button Frame
        stopFrame = Frame(self)
        stopFrame.pack(fill=X)

        stopButton = Button(stopFrame, text="Stop")
        stopButton.pack(fill=X, padx=10)

        # Log Frame
        logFrame = Frame(self)
        logFrame.pack(fill=BOTH, expand=True)

        logText = Text(logFrame, bg="grey", state="disabled")
        logText.pack(fill=BOTH, padx=10, pady=5, expand=True)


def main():
    root = Tk()
    root.geometry("400x300")
    app = NeuroCapture(root)
    root.mainloop()

if __name__ == '__main__':
    main()