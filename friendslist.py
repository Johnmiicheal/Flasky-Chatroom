#15/08/2020
#By MiTECH

import tkinter as tk
import tkinter.ttk as ttk
from chatwindow import ChatWindow

class FriendsList(tk.Tk):
    #main functions
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.title('Flasky')
        self.geometry('700x500') #Window default size

        #add_friend initializer
        self.menu = tk.Menu(self, bg="lightgrey", fg="white", tearoff=0)

        self.friends_menu = tk.Menu(self.menu, fg="white", bg="lightgrey",
                                    tearoff=0)
        self.friends_menu.add_command(label="Add Friend",
                                    command=self.add_friend)
        self.menu.add_cascade(label="Friends", menu=self.friends_menu)

        self.configure(menu=self.menu)


    #Making the scrollable frame within the canvas
        self.canvas = tk.Canvas(self, bg="black")
        self.canvas_frame = tk.Frame(self.canvas)

        self.scrollbar = ttk.Scrollbar(self, orient="vertical",
                                        command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side=tk.LEFT, fill=tk.Y)
        self.canvs.pack(side=tk.LEFT, expand=1, fill=tk.BOTH)

        self.friend_area = self.canvas.create_window((0,0),
                            window=self.canvas_frame, anchor="nw")
        
        self.bind_events()

        self.load_friends()

    def on_frame_resized(self, event=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    #The Friend list frame
    def load_friends(self):
        friend_frame = ttk.Frame(self.canvas_frame)

        profile_photo = tk.PhotoImage(file="image/avatar4.png")
        profile_photo_label = ttk.Label(friend_frame, image=profile_photo)
        profile_photo_label.image = profile_photo

        friend_name = ttk.Label(friend_frame, text="friend", anchor=tk.W)

        message_button = ttk.Button(friend_frame, text="Chat",
                                    command=self.open_chat_window)
        
        profile_photo_label.pack(side=tk.LEFT)
        friend_name.pack(side=tk.LEFT)
        message_button.pack(side=tk.RIGHT)

        friend_frame.pack(fill=tk.X, expand=1)

    #Add Friend Function
    def add_friend(self):
        self.load_friends()
 

    
    #Event Binders

    def bind_events(self):
        self.bind('<Configure>', self.on_frame_resized)
        self.canvas.bind('<Configure>', self.friends_width)

    def friends_width(self, event):
        canvas_width = event.width 
        self.canvas.itemconfig(self.friend_area, width=canvas_width)



    def open_chat_window(self):
        cw = ChatWindow(self, 'friend', 'image/avatar4.png')
