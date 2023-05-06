from tkinter import *
from PIL import ImageTk, Image
from otp import otp,solve,otpcheck
import time
class LoginPage:
    def __init__(self, window):
        self.window = window
        self.window.geometry('850x650')
        self.window.resizable(0, 0)
        #self.window.state('zoomed')
        self.window.title('OTP Generator')
        self.email_address=''
        LoginPage.otp=''
        LoginPage.otp_org=''
        LoginPage.otp_en=''
        # ========================================================================
        # ============================background image============================
        # ========================================================================
        self.bg_frame = Image.open('images\\1.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo,bg='white')
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')
        # ====== Login Frame =========================
        self.lgn_frame = Frame(self.window, bg='white', width=300, height=350)
        self.lgn_frame.place(x=500, y=230)

        # ========================================================================
        # ========================================================
        # ========================================================================
        self.txt = "OTP GENERATOR"
        self.heading = Label(self.window, text=self.txt, font=('Montserrat Classic', 25, "bold"), bg='white',bd=5,
fg='#2e1468',relief=FLAT)
        self.heading.place(x=500, y=30, width=300, height=30)

        # ========================================================================
        # ============ Left Side Image ================================================
        # ========================================================================
        '''self.side_image = Image.open('images\\vector.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=100)
'''
        # ========================================================================
        # ============ Sign In Image =============================================
        # ========================================================================
        self.sign_in_image = Image.open('images\\icon.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.window, image=photo, bg='white')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=580, y=80)
        self.frame1()
        # ========================================================================
        # ============ Sign In label =============================================
        # ========================================================================
    # self.sign_in_label = Label(self.lgn_frame, text="Sign In", bg="#040405", fg="#2e1468",
       #                             font=("yu gothic ui", 17, "bold"))
       # self.sign_in_label.place(x=5, y=60)

        # ========================================================================
        # ============================username====================================
        # ========================================================================
    def frame1(self):
        self.username_label = Label(self.lgn_frame, text="Email", bg="white", fg="#2e1468",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=30, y=10)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#eeeeee", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"),insertbackground = '#d9d9d9',borderwidth=2)

        self.username_entry.place(x=30, y=45, width=270, height=30)
        self.username_entry.focus()


        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=30, y=75)
        # ===== Username icon =========
       #self.username_icon = Image.open('images\\username_icon.png')
        #photo = ImageTk.PhotoImage(self.username_icon)
        #self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        #self.username_icon_label.image = photo
        #self.username_icon_label.place(x=31, y=232)'''

        # ========================================================================
        # ============================login button================================
        # ========================================================================
       # self.lgn_button = Image.open('images\\btn1.png')
        #photo = ImageTk.PhotoImage(self.lgn_button)
        #self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
        #self.lgn_button_label.image = photo
        #self.lgn_button_label.place(x=550, y=450)
        self.login = Button(self.lgn_frame, text='Generate OTP', font=("yu gothic ui", 14, "bold"), width=15, bd=0,
                           command=self.gen_otp, bg='#5496d2', cursor='hand2', activebackground='#3047ff', fg='white')
        self.login.place(x=70, y=105)
        # ========================================================================
        # ============================Forgot password=============================
        # ========================================================================
        self.forgot_button = Button(self.lgn_frame, text="Resend OTP",
                                    font=("yu gothic ui", 12, "bold underline"), fg="#2e1468", relief=FLAT,activebackground="#040405"
                                    ,command=self.gen_otp, borderwidth=0, background="white", cursor="hand2")
        self.forgot_button.place(x=150, y=155)

        #self.signup_img = ImageTk.PhotoImage(file='images\\register.png')
        #self.signup_button_label = Button(self.lgn_frame, image=self.signup_img, bg='white', cursor="hand2",
         #                                 borderwidth=0, background="#040405", activebackground="#040405")
        #self.signup_button_label.place(x=670, y=555, width=111, height=35)

    '''# ========================================================================
        # ============================password====================================
        # ========================================================================
        self.password_label = Label(self.lgn_frame, text="Password", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=550, y=380)

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"), show="*", insertbackground = '#6b6a69')
        self.password_entry.place(x=580, y=416, width=244)

        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=550, y=440)
        # ======== Password icon ================
        self.password_icon = Image.open('images\\password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=414)
        # ========= show/hide password ==================================================================
        self.show_image = ImageTk.PhotoImage \
            (file='images\\show.png')

        self.hide_image = ImageTk.PhotoImage \
            (file='images\\hide.png')

        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)

    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=860, y=420)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)
        self.password_entry.config(show='*')
    
'''
    def backtowindow(self):
        self.clear_frame()
        self.frame1()
    def clear_frame(self):
     for widgets in self.lgn_frame.winfo_children():
       widgets.destroy()
    def gen_otp(self):
        print('clicked',self.username_entry.get(),solve(self.username_entry.get()))
        if solve(self.username_entry.get()):
           #print(otp(self.username_entry.get()))
           LoginPage.otp_org=otp(self.username_entry.get())
           if LoginPage.otp_org!=False: #if otp sent
                #otp_org=otp(self.username_entry.get())
                print(LoginPage.otp_org)
                self.gen_otp_label1 = Label(self.lgn_frame, text='OTP sent successfully!', font=("yu gothic ui", 13, "bold"),
                                relief=FLAT, borderwidth=0, background="white", fg='#83e877')
                self.gen_otp_label1.place(x=60, y=200)
                self.lgn_frame.after(1000)
                #self.lgn_frame.update()
                time.sleep(2)
                self.clear_frame()
                self.lgn_frame = Frame(self.window, bg='white', width=300, height=350)
                self.lgn_frame.place(x=500, y=230)
                self.otp_label1 = Label(self.lgn_frame, text="One-Time Password", bg="white", fg="#2e1468",
                    font=("yu gothic ui", 13, "bold"))
                self.otp_label1.place(x=50, y=10)
                self.otp_entry1 = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#d9d9d9", fg="#6b6a69",
                        font=("yu gothic ui ", 12, "bold"), insertbackground = '#d9d9d9',borderwidth=2)
                self.otp_entry1.place(x=50, y=50, width=30, height=30)
                self.otp_entry1.focus()
                self.otp_entry2 = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#d9d9d9", fg="#6b6a69",
                        font=("yu gothic ui ", 12, "bold"), insertbackground = '#d9d9d9',borderwidth=2)
                self.otp_entry2.place(x=90, y=50, width=30, height=30)
                self.otp_entry2.focus()
                self.otp_entry3 = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#d9d9d9", fg="#6b6a69",
                        font=("yu gothic ui ", 12, "bold"), insertbackground = '#d9d9d9',borderwidth=2)
                self.otp_entry3.place(x=130, y=50, width=30, height=30)
                self.otp_entry3.focus()
                self.otp_entry4 = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#d9d9d9", fg="#6b6a69",
                        font=("yu gothic ui ", 12, "bold"), insertbackground = '#d9d9d9',borderwidth=2)
                self.otp_entry4.place(x=170, y=50, width=30, height=30)
                self.otp_entry4.focus()
                self.otp_entry5 = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#d9d9d9", fg="#6b6a69",
                        font=("yu gothic ui ", 12, "bold"), insertbackground = '#d9d9d9',borderwidth=2)
                self.otp_entry5.place(x=210, y=50, width=30, height=30)
                self.otp_entry5.focus()
                self.otp_entry6 = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#d9d9d9", fg="#6b6a69",
                        font=("yu gothic ui ", 12, "bold"), insertbackground = '#d9d9d9',borderwidth=2)
                self.otp_entry6.place(x=250, y=50, width=30, height=30)
                self.otp_entry6.focus()
                self.verify = Button(self.lgn_frame, text='Verify OTP', font=("yu gothic ui", 14, "bold"), width=15, bd=0,
                command=self.check,bg='#5496d2', cursor='hand2', activebackground='#3047ff', fg='white')
                self.verify.place(x=70, y=110)
                self.forgot_button2 = Button(self.lgn_frame, text="Try Again!",
                            font=("yu gothic ui", 12, "bold underline"), fg="#2e1468", relief=FLAT,activebackground="#040405"
                            ,command=self.backtowindow, borderwidth=0, background="white", cursor="hand2")
                self.forgot_button2.place(x=150, y=150)
           else:
                self.gen_otp_label2 = Label(self.lgn_frame, text='An error occured.\nPlease try again', font=("yu gothic ui", 12, "bold"),
            relief=FLAT, borderwidth=0, background="white", fg='red')
                self.gen_otp_label2.place(x=60, y=200)
        else:
            self.gen_otp_label3 = Label(self.lgn_frame, text='Invalid email address!', font=("yu gothic ui", 12, "bold"),
            relief=FLAT, borderwidth=0, background="white", fg='red')
            self.gen_otp_label3.place(x=60, y=200)
    def check(self):
        LoginPage.otp_en=self.otp_entry1.get()+self.otp_entry2.get()+self.otp_entry3.get()+self.otp_entry4.get()+self.otp_entry5.get()+self.otp_entry6.get()
        print(LoginPage.otp_en)
        print(LoginPage.otp_org,"en",LoginPage.otp_en)
        if otpcheck(LoginPage.otp_org,LoginPage.otp_en):
            self.ver_otp_label1 = Label(self.lgn_frame, text='OTP verified successfully!', font=("yu gothic ui", 13, "bold"),
            relief=FLAT, borderwidth=0, background="white", fg='#83e877')
            self.ver_otp_label1.place(x=80, y=195)
        else:
            self.ver_otp_label2 = Label(self.lgn_frame, text='Unable to verify this OTP. Try again!', font=("yu gothic ui", 13, "bold"),
            relief=FLAT, borderwidth=0, background="white", fg='red')
            self.ver_otp_label2.place(x=80, y=195)
def page():
    window = Tk()
    LoginPage(window)
    window.mainloop()



if __name__ == '__main__':
    page()