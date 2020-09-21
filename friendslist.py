#15/08/2020
#11/09/2020
#By CRiTEK

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from chatwindow import ChatWindow
from requester import Requester

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

        self.show_login_screen()    

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


    def show_friends(self):
        self.configure(menu=self.menu)
        self.login_frame.pack_forget()
        
        self.canvas = tk.Canvas(self, bg="white")
        self.canvas_frame = tk.Frame(self.canvas)

        self.scrollbar = ttk.Scrollbar(self, orient="vertical",
                                    command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side=tk.LEFT, fill=tk.Y)
        self.canvas.pack(side=tk.LEFT, expand=1, fill=tk.BOTH)

        self.friends_area = self.canvas.create_window((0,0),
                     window = self.canvas_frame, anchor="nw")

        self.bind_events()
        self.load_friends()

    def show_login_screen(self):
        self.login_frame = ttk.Frame(self)
        username_label = ttk.Label(self.login_frame, text="Username")
        self.username_entry = ttk.Entry(self.login_frame)

        real_name_label = ttk.Label(self.login_frame, text="Real Namme")
        self.real_name_entry = ttk.Entry(self.login_frame)

        login_button = ttk.Button(self.login_frmae, text="Login", command=self.login)
        create_account_button = ttk.Button(self.login_frame, text="Create Account", command=self.create_account)

        username_label.grid(row=0, column=0, sticky='e')
        self.username_entry.grid(row=0, column=1)

        real_name_label.grid(row=1, column=0, sticky='e')
        self.real_name_entry.grid(row=1, column=1)

        login_button.grid(row=2, column=0, sticky='e')
        create_account_button.grid(row=2, column=1)

        for i in range(3):
            tk.Grid.rowconfigure(self.login_frame, i, weight=1)
            tk.Grid.columnconfigure(self.login_frame, i, weight=1)
        self.login_frame.pack(fill=tk.BOTH, expand=1)

    def login(self):
        username = self.username_entry.get()
        real_name = self.real_name_entry.get()

        if self.requester.login(username, real_name):
            self.username = username
            self.real_name = real_name
            self.show_friends()
        else:
            msg.showerror("Failed! ", f"Could not login as {username}")

    def create_account(self):
        username = self.username_entry.get()
        real_name = self.real_name_entry.get()

        if self.requester.create_account(username, real_name):
            self.username =  username
            self.real_name = real_name
            self.show_friends()
        else:
            msg.showerror("Failed", "Account already exists")


    def on_frame_resized(self, event=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    #The Friend list frame
    def iload_friends(self):
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

    def load_friends(self):
        all_users = self.requester.get_all_users()
        for user in all_users:
            if user['username'] != self.username:
                friend_frame = ttk.Frame(self.canvas_frame)

        profile_photo = tk.PhotoImage (file="image/avatar4.png")
        profile_photo_label = ttk.Label(friend_frame, image=profile_photo)
        profile_photo_label.image = profile_photo

        friend_name = ttk.Label(friend_frame, text=user['real_name'], anchor=tk.W)

        message_this_friend = partial(self.open_chat_window, username=user["username"], real_name=user['real_name'])
        message_button = ttk.Button(friend_frame, text="Chat", command=message_this_friend)

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



    def open_chat_window(self, username, real_name):
        cw = ChatWindow(self, real_name, username, 'image/avatar4.png')

