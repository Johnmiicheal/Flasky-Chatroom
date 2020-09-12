import tkinter as tk
import tkinter.ttk as ttk
from smilieselect import SmilieSelect

class ChatWindow(tk.Toplevel):
    def __init__(self, master, friend_name, friend_avatar, **kwargs):
        super().__init__(**kwargs)
        self.master = master
        self.title(friend_name)
        self.geometry('540x640')
        self.minsize(540,640)

    #Message or ChatRoom Area
        self.right_frame = tk.Frame(self)
        self.left_frame = tk.Frame(self)
        self.bottom_frame = tk.Frame(self.left_frame)

        self.message_area = tk.Text(self.left_frame, bg="white", fg="black", wrap=tk.WORD, width=30)
        self.scrollbar = ttk.Scrollbar(self.left_frame, orient='vertical',
                                         command = self.message_area.yview)
        self.message_area.configure(yscrollcommand = self.scrollbar.set)
        self.text_area = tk.Text(self.bottom_frame, bg="white", fg="black", height=3, width=30)
        self.send_button = ttk.Button(self.bottom_frame, text="Send", command=self.send_message)

    #Profile Picture Frame Area
        self.profile_picture = tk.PhotoImage(file="image/avatar4.png")

        self.friend_profile_picture = tk.PhotoImage(file = friend_avatar)

        self.profile_picture_area = tk.Label(self.right_frame, image=self.profile_picture, relief=tk.RIDGE)
        self.friend_profile_picture_area = tk.Label(self.right_frame, image = self.friend_profile_picture)

        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        self.scrollbar.pack(side=tk.LEFT, fill=tk.Y)
        self.message_area.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.message_area.configure(state='disabled')

        self.right_frame.pack(side=tk.LEFT, fill=tk.Y)
        self.profile_picture_area.pack(side=tk.BOTTOM)
        self.friend_profile_picture_area.pack(side=tk.TOP)

        self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.Y)
        self.text_area.pack(side=tk.LEFT, fill=tk.X, expand=1, pady=5)
        self.send_button.pack(side=tk.RIGHT, pady=5)

    #Smilie Characters Area
        self.text_area.smilies = []

        self.smilies_image = tk.PhotoImage(file="smilies/mikulka-smile-cool.png")
        self.smilie_button = ttk.Button(self.bottom_frame, 
                            image = self.smilies_image, command=self.smilie_chooser, style="smilie.TButton")

        self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.smilie_button.pack(side=tk.LEFT, pady=5)
        self.text_area.pack(side=tk.LEFT, fill=tk.X, expand=1, pady=5)
        self.send_button.pack(side=tk.RIGHT, pady=5)

        self.configure_styles()
        self.bind_events()


    def smilie_chooser(self, event=None):
        SmilieSelect(self)

    def add_smilie(self, smilie):
        smilie_index = self.text_area.index(self.text_area.image_create(tk.END, image=smilie))
        self.text_area.smilies.append((smilie_index, smilie))

    def bind_events(self):
        self.bind("<Return>", self.send_message)
        self.text_area.bind("<Return>", self.send_message)


    def send_message(self, event=None):
        message = self.text_area.get(1.0, tk.END)        

        if message.strip() or len(self.text_area.smilies):
            message = "Me: " + message
            self.message_area.configure(state='normal')
            self.message_area.insert(tk.END, message)

            if len(self.text_area.smilies):
                last_line_no = self.message_area.index(tk.END)
                last_line_no = str(last_line_no).split('.')[0]
                last_line_no = str(int(last_line_no) - 2)

            for index, file in self.text_area.smilies:
                char_index = str(index).split('.')[1]
                char_index =str(int(char_index) + 4)
                smilie_index = last_line_no + '.' + char_index
                self.message_area.image_create(smilie_index, image=file)

            self.text_area.smilies = []
            self.message_area.configure(state='disabled')
            self.text_area.delete(1.0, tk.END)
        return "break"        

        
     
        


    def configure_styles(self):
        style=ttk.Style()
        style.configure("send.TButton", background='#dddddd', foreground="black", padding=1)


if __name__ == '__main__':
    w = tk.Tk()
    c = ChatWindow(w, 'friend_', 'image/avatar4.png')
    c.protocol("WM_DELETE_WINDOW", w.destroy)
    w.mainloop()


                                    
        