import tkinter as tk

from database.database import init_db

from screens.splash import SplashScreen
from screens.login import LoginScreen
from screens.register import RegisterScreen
from screens.dashboard import Dashboard
from screens.check_message import CheckMessageScreen
from screens.result import ResultScreen
from screens.history import HistoryScreen
from screens.statistics import StatisticsScreen
from screens.about import AboutScreen


class SmartSpamApp:

    def __init__(self):
        self.root = tk.Tk()

        
        self.current_username = None

       
        init_db()

        
        self.show_splash()

   

    def show_splash(self):
        self.clear_window()

        SplashScreen(
            self.root,
            self.show_login
        )

    

    def show_login(self):
        self.clear_window()

        LoginScreen(
            self.root,
            self.login_success,
            self.show_register
        )

    

    def login_success(self, username):
        self.current_username = username

        self.show_dashboard()

    

    def show_register(self):
        self.clear_window()

        RegisterScreen(
            self.root,
            self.registration_success,
            self.show_login
        )

   

    def registration_success(self):
        self.show_login()

    

    def show_dashboard(self):
        self.clear_window()

        Dashboard(
            self.root,
            self.current_username,
            self.show_check_message,
            self.show_history,
            self.show_statistics,
            self.show_about,
            self.logout
        )

    

    def show_check_message(self):
        self.clear_window()

        CheckMessageScreen(
            self.root,
            self.current_username,
            self.show_dashboard,
            self.show_result
        )

    

    def show_result(self, message, result, confidence):

        self.clear_window()

        ResultScreen(
            self.root,
            self.current_username,  
            message,                 
            result,                  
            confidence,              
            self.show_check_message, 
            self.show_dashboard     
        )

    

    def show_history(self):
        self.clear_window()

        HistoryScreen(
            self.root,
            self.current_username,
            self.show_dashboard
        )

    

    def show_statistics(self):
        self.clear_window()

        StatisticsScreen(
            self.root,
            self.current_username,
            self.show_dashboard
        )

    
    def show_about(self):
        self.clear_window()

        AboutScreen(
            self.root,
            self.show_dashboard
        )

    
    def logout(self):
        self.current_username = None

        self.show_login()

    

    def clear_window(self):

        for widget in self.root.winfo_children():
            widget.destroy()

    

    def run(self):
        self.root.mainloop()




if __name__ == "__main__":

    app = SmartSpamApp()

    app.run()