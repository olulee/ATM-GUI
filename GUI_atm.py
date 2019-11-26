# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 10:43:58 2019

@author: Oluleye
"""

from tkinter import*
import mysql.connector
class Atm():
    
    def __init__(self):
        self.root = Tk()
        self.root.title('Geolee ATM')
        self.root.geometry('550x600')
        self.frm_lb_header = LabelFrame(self.root, width=550, height=50, bg='blue')
        self.prev = Label(self.frm_lb_header, text='GeoLee', fg='white', bg='blue', font=('Verdana',10,'normal'))
        self.prev.place(x=10, y=4)
        self.prev2 = Label(self.frm_lb_header, text='ATM', fg='white', bg='blue', font=('Verdana',15,'bold'))
        self.prev2.place(x=10, y=20)
        self.frm_lb_header.grid(row=0, column=0, columnspan=4)

        self.con=mysql.connector.connect(host='localhost', user='root', password='', database='leyeatm_db')
        self.mycur = self.con.cursor()
        #self.mycur.execute('CREATE DATABASE leyeatm_db')
        #self.mycur.execute('CREATE TABLE customers (username VARCHAR(20),accountnum VARCHAR(20), pin VARCHAR(20))')
        #self.mycur.execute('ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY')
        
        self.side_btn1 = Button(self.root, text='>>>', width=12, height=2, command=self.open_account)
        self.side_btn1.grid(row=2, column=0)
        
        self.side_btn2 = Button(self.root, text='>>>', width=12, height=2, command=self.login)
        self.side_btn2.grid(row=3, column=0)
        
        self.side_btn3 = Button(self.root, text='>>>', width=12, height=2)
        self.side_btn3.grid(row=4, column=0)
        
        self.side_btn4 = Button(self.root, text='<<<', width=12, height=2)
        self.side_btn4.grid(row=2, column=3)
        
        self.side_btn5 = Button(self.root, text='<<<', width=12, height=2)
        self.side_btn5.grid(row=3, column=3)
        
        self.side_btn6 = Button(self.root, text='<<<', width=12, height=2)
        self.side_btn6.grid(row=4, column=3)
        
        self.btn_frm = Frame(self.root, width=250, height=150, bg='grey')
        self.btn_frm.grid(row=5, column=2, rowspan=9)
        
        
        self.num_1 = Button(self.btn_frm, text='1', width=6, bg='grey', height=2)
        self.num_1.grid(row=5, column=0)
        
        self.num_2 = Button(self.btn_frm, text='2', width=6, bg='grey', height=2)
        self.num_2.grid(row=5, column=1)
        
        self.num_3 = Button(self.btn_frm, text='3', width=6, bg='grey', height=2)
        self.num_3.grid(row=5, column=2)
        
        self.num_cnl = Button(self.btn_frm, text='Cancel', width=6, bg='red', height=2)
        self.num_cnl.grid(row=5, column=3)
        
        self.num_4 = Button(self.btn_frm, text='4', width=6, bg='grey', height=2)
        self.num_4.grid(row=6, column=0)
        
        self.num_5 = Button(self.btn_frm, text='5', width=6, bg='grey', height=2)
        self.num_5.grid(row=6, column=1)
        
        self.num_6 = Button(self.btn_frm, text='6', width=6, bg='grey', height=2)
        self.num_6.grid(row=6, column=2)
        
        self.num_clr = Button(self.btn_frm, text='Clear', width=6, bg='yellow', height=2)
        self.num_clr.grid(row=6, column=3)
        
        self.num_7 = Button(self.btn_frm, text='7', width=6, bg='grey', height=2)
        self.num_7.grid(row=7, column=0)
        
        self.num_8 = Button(self.btn_frm, text='8', width=6, bg='grey', height=2)
        self.num_8.grid(row=7, column=1)
        
        self.num_9 = Button(self.btn_frm, text='9', width=6, bg='grey', height=2)
        self.num_9.grid(row=7, column=2)
        
        self.num_enter = Button(self.btn_frm, text='Enter', width=6, bg='green', height=2)
        self.num_enter.grid(row=7, column=3)
        
        self.num_f1 = Button(self.btn_frm, text='', width=6, bg='grey', height=2)
        self.num_f1.grid(row=8, column=0)
        
        self.num_2 = Button(self.btn_frm, text='0', width=6, bg='grey', height=2)
        self.num_2.grid(row=8, column=1)
        
        self.num_f3 = Button(self.btn_frm, text='', width=6, bg='grey', height=2)
        self.num_f3.grid(row=8, column=2)
        
        self.num_fcnl = Button(self.btn_frm, text='', width=6, bg='grey', height=2)
        self.num_fcnl.grid(row=8, column=3)
        self.my_atm()
        self.root.mainloop()
        
    def my_atm(self):
        self.screen_home = LabelFrame(self.root, width=350, height=200, bg='blue')
        
        self.view = Label(self.screen_home, text='welcome to GeoLee Bank', fg='blue',font=('Verdana',10,'normal'))
        self.view.place(x=105, y=30)
        self.lb_openacct = Label(self.screen_home, text='Open Account', fg='blue')
        self.lb_openacct.place(x=10, y=20)
        self.lb_dsc = Label(self.screen_home, text='We are here', fg='blue',font=('Verdana',10,'normal'))
        self.lb_dsc.place(x=145, y=80)
        self.lb_login = Label(self.screen_home, text='Login', fg='blue')
        self.lb_login.place(x=10, y=80)
        self.lb_dcs2 = Label(self.screen_home,text='To serve yo better', fg='blue',font=('Verdana',10,'normal'))
        self.lb_dcs2.place(x=120, y=120)
        self.lb_exit = Label(self.screen_home, text='Exit', fg='blue')
        self.lb_exit.place(x=10, y=160)
        #self.lb_proceed = Label(self.screen_home, text='Proceed', fg='blue')
        #self.lb_proceed.place(x=290, y=160)
        self.side_btn1.config(command=self.open_account)
        self.side_btn2.config(command=self.login)
        self.side_btn3.config(command=self.free)
        self.side_btn4.config(command=self.free)
        self.side_btn5.config(command=self.free)
        self.side_btn6.config(command=self.free)
        self.screen_home.grid(row=2, column=2,rowspan=3, pady=5)
        
        
    def login_proc(self):
        self.loginacctnum = self.login_acctnum.get()
        self.loginpin = self.login_pin.get()
        self.sql_sel = 'SELECT * FROM customers WHERE accountnum = %s and pin = %s'
        self.sql_rl = (self.loginacctnum,self.loginpin,)
        self.mycur.execute(self.sql_sel, self.sql_rl)
        self.result = self.mycur.fetchall()
        print('Total number of rows in customers is: ', self.mycur.rowcount)
        self.mydata = self.result[0]
        print('yes',self.mydata)
        self.sql_acctnum = self.mydata[1]
        self.sql_pin = self.mydata[2]
        if self.loginacctnum == self.sql_acctnum and self.loginpin == self.sql_pin:
            print('Welcome', self.mydata[0])
            self.id = self.mydata[3]
            self.balance = self.mydata[4]
            
        else:
            print('Invalid Details')
        self.screen_login.destroy()
        self.screen_logproc = LabelFrame(self.root, width=350, height=200, bg='blue')
        
        self.view = Label(self.screen_logproc, text='please wait while your transaction \n is processing', fg='blue')
        self.view.place(x=75, y=20)
        self.screen_logproc.grid(row=2, column=2,rowspan=3, pady=5)
        self.screen_logproc.after(1000,self.welcome)
        
    def login(self):
        self.screen_home.destroy()
        self.screen_login = LabelFrame(self.root, width=350, height=200, bg='blue')
        self.login_acctnum = StringVar()
        self.login_pin = StringVar()
        self.view = Label(self.screen_login, text='welcome to GeoLee Bank', fg='blue')
        self.view.place(x=105, y=20)
        self.lb_acctnum = Label(self.screen_login, text='Enter Account Num', fg='blue')
        self.lb_acctnum.place(x=10, y=80)
        self.ent = Entry(self.screen_login, textvariable=self.login_acctnum)
        self.ent.place(x=130, y=80)
        self.lb_pin = Label(self.screen_login, text='Enter pin', fg='blue')
        self.lb_pin.place(x=10, y=120)
        self.ent = Entry(self.screen_login, textvariable=self.login_pin)
        self.ent.place(x=130, y=120)
        self.lb_proceed = Label(self.screen_login, text='Proceed', fg='blue')
        self.lb_proceed.place(x=290, y=160)
        self.side_btn6.config(command=self.login_proc)
        self.side_btn1.config(command=self.free)
        self.side_btn2.config(command=self.free)
        self.side_btn3.config(command=self.free)
        self.side_btn4.config(command=self.free)
        self.side_btn5.config(command=self.free)
        #self.side_btn6.config(command=self.free)
        self.screen_login.grid(row=2, column=2,rowspan=3, pady=5)
        
    def login_fail(self):
        self.screen_logproc.destroy()
        self.screen_loginfail = LabelFrame(self.root, width=350, height=200, bg='blue')
        
        self.view = Label(self.screen_loginfail, text='Incorrect Login Details', fg='blue')
        self.view.place(x=100, y=100)
        self.lb_home = Label(self.screen_loginfail, text='Home', fg='blue')
        self.lb_home.place(x=300, y=160)
        self.side_btn1.config(command=self.free)
        self.side_btn2.config(command=self.free)
        self.side_btn3.config(command=self.free)
        self.side_btn4.config(command=self.free)
        self.side_btn5.config(command=self.free)
        self.side_btn6.config(command=self.my_atm)
        self.screen_loginfail.grid(row=2, column=2,rowspan=3, pady=5)
        
    def welcome(self):
        self.screen_logproc.destroy()
        self.screen_welcome = LabelFrame(self.root, width=350, height=200, bg='blue')
        
        self.view = Label(self.screen_welcome, text='welcome', fg='blue', font=('Verdana',10,'normal'))
        self.view.place(x=80, y=3)
        self.acct_detail = StringVar()
        self.acct_detail.set(self.mydata[0])
        self.detail = Label(self.screen_welcome, textvariable=self.acct_detail, fg='blue', font=('Verdana',10,'normal'))
        self.detail.place(x=150, y=3)
        self.lb_withdraw = Label(self.screen_welcome, text='Withdraw', fg='blue')
        self.lb_withdraw.place(x=10, y=20)
        self.lb_deposit = Label(self.screen_welcome, text='Deposit', fg='blue')
        self.lb_deposit.place(x=10, y=90)
        self.lb_balance = Label(self.screen_welcome, text='Balance', fg='blue')
        self.lb_balance.place(x=10, y=160)
        self.lb_quickteller = Label(self.screen_welcome, text='QuickTeller', fg='blue')
        self.lb_quickteller.place(x=270, y=20)
        self.lb_proceed = Label(self.screen_welcome, text='Quit', fg='blue')
        self.lb_proceed.place(x=290, y=160)
        self.side_btn1.config(command=self.withdraw)
        self.side_btn2.config(command=self.deposit)
        self.side_btn3.config(command=self.tbalance)
        self.side_btn4.config(command=self.quickteller)
        self.side_btn5.config(command=self.free)
        self.side_btn6.config(command=self.free)
        self.screen_welcome.grid(row=2, column=2,rowspan=3, pady=5)
        
    def withdraw(self):
        self.screen_welcome.destroy()
        self.screen_withdraw = LabelFrame(self.root, width=350, height=200, bg='blue')
        
        self.view = Label(self.screen_withdraw, text='welcome to withdraw', fg='blue', font=('Verdana',5,'normal'))
        self.view.place(x=60, y=3)
        self.lb_withdraw = Label(self.screen_withdraw, text='1000', fg='blue')
        self.lb_withdraw.place(x=10, y=20)
        self.lb_deposit = Label(self.screen_withdraw, text='2000', fg='blue')
        self.lb_deposit.place(x=10, y=90)
        self.lb_balance = Label(self.screen_withdraw, text='5000', fg='blue')
        self.lb_balance.place(x=10, y=160)
        self.lb_quickteller = Label(self.screen_withdraw, text='10000', fg='blue')
        self.lb_quickteller.place(x=300, y=20)
        self.lb_quickteller = Label(self.screen_withdraw, text='20000', fg='blue')
        self.lb_quickteller.place(x=300, y=90)
        self.lb_other = Label(self.screen_withdraw, text='Others', fg='blue')
        self.lb_other.place(x=300, y=160)
        self.side_btn1.config(command=self.withdraw_1)
        self.side_btn2.config(command=self.withdraw_2)
        self.side_btn3.config(command=self.withdraw_3)
        self.side_btn4.config(command=self.withdraw_4)
        self.side_btn5.config(command=self.withdraw_5)
        self.side_btn6.config(command=self.others)
        self.screen_withdraw.grid(row=2, column=2,rowspan=3, pady=5)
    def withdraw_1(self):
        self.input_withdraw = 1000
        if self.balance <= int(self.input_withdraw):
            self.insufficient_bal()
            
        else:
            self.balance = self.balance - self.input_withdraw
            print(self.balance)
            sql_withdraw = 'UPDATE customers set balance=%s where id = %s'
            val_withdraw = (self.balance, self.id)
            self.mycur.execute(sql_withdraw,val_withdraw)
            self.con.commit()
            print('1000 withdrawn sucessfully')
            self.take_cash()
    def withdraw_2(self):
        self.input_withdraw = 2000
        if self.balance <= int(self.input_withdraw):
            self.insufficient_bal()
            
        else:
            self.balance = self.balance - self.input_withdraw
            print(self.balance)
            sql_withdraw = 'UPDATE customers set balance=%s where id = %s'
            val_withdraw = (self.balance, self.id)
            self.mycur.execute(sql_withdraw,val_withdraw)
            self.con.commit()
            print('2000 withdrawn sucessfully')
            self.take_cash()
    def withdraw_3(self):
        self.input_withdraw = 5000
        if self.balance <= int(self.input_withdraw):
            self.insufficient_bal()
            
        else:
            self.balance = self.balance - self.input_withdraw
            print(self.balance)
            sql_withdraw = 'UPDATE customers set balance=%s where id = %s'
            val_withdraw = (self.balance, self.id)
            self.mycur.execute(sql_withdraw,val_withdraw)
            self.con.commit()
            print('5000 withdrawn sucessfully')
            self.take_cash()
    def withdraw_4(self):
        self.input_withdraw = 10000
        if self.balance <= int(self.input_withdraw):
            self.insufficient_bal()
            
        else:
            self.balance = self.balance - self.input_withdraw
            print(self.balance)
            sql_withdraw = 'UPDATE customers set balance=%s where id = %s'
            val_withdraw = (self.balance, self.id)
            self.mycur.execute(sql_withdraw,val_withdraw)
            self.con.commit()
            print('10000 withdrawn sucessfully')
            self.take_cash()
    def withdraw_5(self):
        self.input_withdraw = 20000
        if self.balance <= int(self.input_withdraw):
            self.insufficient_bal()
            
        else:
            self.balance = self.balance - self.input_withdraw
            print(self.balance)
            sql_withdraw = 'UPDATE customers set balance=%s where id = %s'
            val_withdraw = (self.balance, self.id)
            self.mycur.execute(sql_withdraw,val_withdraw)
            self.con.commit()
            print('20000 withdrawn sucessfully')
            self.take_cash()
    def others(self):
        self.screen_welcome.destroy()
        self.screen_with_other = LabelFrame(self.root, width=350, height=200, bg='blue')
        
        self.view = Label(self.screen_with_other, text='welcome to Withdraw', fg='blue', font=('Verdana',5,'normal'))
        self.view.place(x=60, y=3)
        self.lb_enter = Label(self.screen_with_other, text='Please enter your amount', fg='blue')
        self.lb_enter.place(x=100, y=40)
        self.my_withdraw_amt = IntVar()
        self.ent_withdraw = Entry(self.screen_with_other, textvariable=self.my_withdraw_amt)
        self.ent_withdraw.place(x=100, y=150)
        self.lb_proceed = Label(self.screen_with_other, text='Proceed', fg='blue')
        self.lb_proceed.place(x=300, y=160)
        self.side_btn2.config(command=self.free)
        self.side_btn6.config(command=self.with_other_proc)
        self.side_btn1.config(command=self.free)
        self.side_btn2.config(command=self.free)
        self.side_btn3.config(command=self.free)
        self.side_btn4.config(command=self.free)
        self.side_btn5.config(command=self.free)
        self.screen_with_other.grid(row=2, column=2,rowspan=3, pady=5)
    def with_other_proc(self):
        self.withdrawothers = self.my_withdraw_amt.get()
        if self.balance <= int(self.withdrawothers):
            self.insufficient_bal()
        else:
            self.balance = self.balance - self.withdrawothers
            print(self.balance)
            sql_withdraw = 'UPDATE customers set balance=%s where id = %s'
            val_withdraw = (self.balance, self.id)
            self.mycur.execute(sql_withdraw,val_withdraw)
            self.con.commit()
            print('withdrawn sucessfully')
            self.take_cash()
    def deposit(self):
        self.screen_welcome.destroy()
        self.screen_deposit = LabelFrame(self.root, width=350, height=200, bg='blue')
        
        self.view = Label(self.screen_deposit, text='welcome to Deposit', fg='blue', font=('Verdana',5,'normal'))
        self.view.place(x=60, y=3)
        self.lb_enter = Label(self.screen_deposit, text='Please enter your amount', fg='blue')
        self.lb_enter.place(x=100, y=40)
        self.deposit_amt = IntVar()
        self.ent_deposit = Entry(self.screen_deposit, textvariable=self.deposit_amt)
        self.ent_deposit.place(x=100, y=150)
        self.lb_proceed = Label(self.screen_deposit, text='Proceed', fg='blue')
        self.lb_proceed.place(x=300, y=160)
        self.side_btn2.config(command=self.free)
        self.side_btn6.config(command=self.dep_proc)
        self.side_btn1.config(command=self.free)
        self.side_btn2.config(command=self.free)
        self.side_btn3.config(command=self.free)
        self.side_btn4.config(command=self.free)
        self.side_btn5.config(command=self.free)
        self.screen_deposit.grid(row=2, column=2,rowspan=3, pady=5)
    def dep_proc(self):
        self.screen_deposit.destroy()
        self.screen_depproc = LabelFrame(self.root, width=350, height=200, bg='blue')
        self.deposit_new = self.deposit_amt.get()
        self.balance = self.balance + self.deposit_new
        sql_deposit = 'UPDATE customers set balance=%s where id = %s'
        val_deposit = (self.balance, self.id)
        self.mycur.execute(sql_deposit,val_deposit)
        self.con.commit()
        print(self.deposit_new)
        self.view = Label(self.screen_depproc, text='please wait while your transaction \n is processing', fg='blue')
        self.view.place(x=75, y=20)
        self.screen_depproc.grid(row=2, column=2,rowspan=3, pady=5)
        self.screen_depproc.after(1000,self.dep_successful)
    def dep_successful(self):
        self.screen_depproc.destroy()
        self.screen_depsucess = LabelFrame(self.root, width=350, height=200, bg='blue')
        self.view = Label(self.screen_depsucess, text='deposited successfully', fg='blue')
        self.view.place(x=100, y=100)
        self.lb_proceed = Label(self.screen_depsucess, text='Another Transaction', fg='blue')
        self.lb_proceed.place(x=230, y=160)
        self.side_btn1.config(command=self.free)
        self.side_btn2.config(command=self.free)
        self.side_btn3.config(command=self.free)
        self.side_btn4.config(command=self.free)
        self.side_btn5.config(command=self.free)
        self.side_btn6.config(command=self.my_atm)
        self.screen_depsucess.grid(row=2, column=2,rowspan=3, pady=5)
        
    def tbalance(self):
        self.screen_welcome.destroy()
        self.screen_balance = LabelFrame(self.root, width=350, height=200, bg='blue')
        self.total_bal = StringVar()
        self.total_bal.set(self.balance)
        self.view = Label(self.screen_balance, text='your account balance is: ', fg='blue')
        self.view.place(x=100, y=100)
        self.lb_bal = Label(self.screen_balance,textvariable=self.total_bal, fg='blue')
        self.lb_bal.place(x=250, y=100)
        self.lb_proceed = Label(self.screen_balance, text='Another Transaction', fg='blue')
        self.lb_proceed.place(x=230, y=160)
        self.side_btn1.config(command=self.free)
        self.side_btn2.config(command=self.free)
        self.side_btn3.config(command=self.free)
        self.side_btn4.config(command=self.free)
        self.side_btn5.config(command=self.free)
        self.side_btn6.config(command=self.my_atm)
        self.screen_balance.grid(row=2, column=2,rowspan=3, pady=5)
        
    def quickteller(self):
        self.screen_welcome.destroy()
        self.screen_quickteller = LabelFrame(self.root, width=350, height=200, bg='blue')
        
        self.lb_quickteller = Label(self.screen_quickteller, text='Air Time', fg='blue')
        self.lb_quickteller.place(x=10, y=20)
        self.lb_transfer = Label(self.screen_quickteller, text='Transfer', fg='blue')
        self.lb_transfer.place(x=10, y=90)
        self.side_btn1.config(command=self.air_time)
        self.side_btn2.config(command=self.free)
        self.side_btn3.config(command=self.free)
        self.side_btn4.config(command=self.free)
        self.side_btn5.config(command=self.free)
        self.side_btn6.config(command=self.free)
        self.screen_quickteller.grid(row=2, column=2,rowspan=3, pady=5)
        
    def air_time(self):
        self.screen_quickteller.destroy()
        self.screen_airtime = LabelFrame(self.root, width=350, height=200, bg='blue')
        self.lb_airtime = Label(self.screen_airtime, text='Please Enter the number', fg='blue')
        self.lb_airtime.place(x=10, y=50)
        self.enter_num = Entry(self.screen_airtime)
        self.enter_num.place(x=150, y=50)
        #self.side_btn1.config(command=self.air_time)
        #self.side_btn2.config(command=self.free)
        #self.side_btn3.config(command=self.free)
        #self.side_btn4.config(command=self.free)
        #self.side_btn5.config(command=self.free)
        self.side_btn6.config(command=self.airtime_proc)
        self.screen_airtime.grid(row=2, column=2,rowspan=3, pady=5)
        
    def airtime_proc(self):
        self.screen_airtime.destroy()
        self.screen_airtimeproc = LabelFrame(self.root, width=350, height=200, bg='blue')
        
        self.view = Label(self.screen_airtimeproc, text='please wait while your transaction \n is processing', fg='blue')
        self.view.place(x=75, y=20)
        self.side_btn1.config(command=self.free)
        self.side_btn2.config(command=self.free)
        self.side_btn3.config(command=self.free)
        self.side_btn4.config(command=self.free)
        self.side_btn5.config(command=self.free)
        self.side_btn6.config(command=self.free)
        self.screen_airtimeproc.grid(row=2, column=2,rowspan=3, pady=5)
        self.screen_airtimeproc.after(1000,self.airtime_successful)
    def airtime_successful(self):
        self.screen_airtimeproc.destroy()
        self.screen_airtimesucess = LabelFrame(self.root, width=350, height=200, bg='blue')
        
        self.view = Label(self.screen_airtimesucess, text='Transaction successfully', fg='blue')
        self.view.place(x=100, y=100)
        self.side_btn1.config(command=self.free)
        self.side_btn2.config(command=self.free)
        self.side_btn3.config(command=self.free)
        self.side_btn4.config(command=self.free)
        self.side_btn5.config(command=self.free)
        self.side_btn6.config(command=self.free)
        self.screen_airtimesucess.grid(row=2, column=2,rowspan=3, pady=5)
        
    def sign_up(self):
        self.username = self.ent_username.get()
        self.accountnum = self.ent_accountnum.get()
        self.pin = self.ent_pin.get()
        print(self.username)
        print(self.accountnum)
        print(self.pin)
        sql = 'INSERT INTO customers(username, accountnum, pin) VALUES(%s, %s,%s)'
        val = (self.username, self.accountnum, self.pin)
        self.mycur.execute(sql,val)
        self.con.commit()
        self.screen_home.destroy()
        self.screen_signup = LabelFrame(self.root, width=350, height=200, bg='blue')
        self.lb_reg = Label(self.screen_signup, text = 'Thank you for siging-up with us', fg='blue')
        self.lb_home = Label(self.screen_signup, text='Home', fg='blue')
        self.lb_home.place(x=300, y=160)
        self.lb_reg.place(x=105, y=20)
        self.side_btn1.config(command=self.free)
        self.side_btn2.config(command=self.free)
        self.side_btn3.config(command=self.free)
        self.side_btn4.config(command=self.free)
        self.side_btn5.config(command=self.free)
        self.side_btn6.config(command=self.my_atm)
        self.screen_signup.grid(row=2, column=2,rowspan=3, pady=5)
        
    def open_account(self):
        self.screen_home.destroy()
        self.screen_open = LabelFrame(self.root, width=350, height=200, bg='blue')
        self.ent_username = StringVar()
        self.ent_accountnum = StringVar()
        self.ent_pin = IntVar()
        self.view = Label(self.screen_open, text='welcome to GeoLee Bank', fg='blue')
        self.view.place(x=105, y=20)
        self.lb_username = Label(self.screen_open, text='Enter your fullname', fg='blue')
        self.lb_username.place(x=10, y=50)
        self.entry_username = Entry(self.screen_open,textvariable=self.ent_username)
        self.entry_username.place(x=140, y=50)
        self.lb_accountnum = Label(self.screen_open, text='Enter your account No', fg='blue')
        self.lb_accountnum.place(x=10, y=80)
        self.entry_accountnum = Entry(self.screen_open, textvariable=self.ent_accountnum)
        self.entry_accountnum.place(x=140, y=80)
        self.lb_pin = Label(self.screen_open, text='Enter your pin', fg='blue')
        self.lb_pin.place(x=10, y=110)
        self.entry_pin = Entry(self.screen_open, textvariable=self.ent_pin, show='*')
        self.entry_pin.place(x=140, y=110)
        self.lb_proceed = Label(self.screen_open, text='Proceed', fg='blue')
        self.lb_proceed.place(x=290, y=160)
        self.side_btn1.config(command=self.free)
        self.side_btn2.config(command=self.free)
        self.side_btn3.config(command=self.free)
        self.side_btn4.config(command=self.free)
        self.side_btn5.config(command=self.free)
        self.side_btn6.config(command=self.sign_up)
        self.screen_open.grid(row=2, column=2,rowspan=3, pady=5)
    
    def free(self):
        pass
        
    def insufficient_bal(self):
        self.screen_withdraw.destroy()
        self.screen_insufficient = LabelFrame(self.root, width=350, height=200, bg='blue')
        self.view = Label(self.screen_insufficient, text='Insufficient Balance ', fg='blue')
        self.view.place(x=100, y=100)
        self.lb_proceed = Label(self.screen_insufficient, text='Another Transaction', fg='blue')
        self.lb_proceed.place(x=230, y=160)
        self.side_btn1.config(command=self.free)
        self.side_btn2.config(command=self.free)
        self.side_btn3.config(command=self.free)
        self.side_btn4.config(command=self.free)
        self.side_btn5.config(command=self.free)
        self.side_btn6.config(command=self.my_atm)
        self.screen_insufficient.grid(row=2, column=2,rowspan=3, pady=5)
        
    def take_cash(self):
        self.screen_withdraw.destroy()
        self.screen_takecash = LabelFrame(self.root, width=350, height=200, bg='blue')
        self.view = Label(self.screen_takecash, text='Please take your cash', fg='blue')
        self.view.place(x=100, y=100)
        self.lb_proceed = Label(self.screen_takecash, text='Another Transaction', fg='blue')
        self.lb_proceed.place(x=230, y=160)
        self.side_btn1.config(command=self.free)
        self.side_btn2.config(command=self.free)
        self.side_btn3.config(command=self.free)
        self.side_btn4.config(command=self.free)
        self.side_btn5.config(command=self.free)
        self.side_btn6.config(command=self.my_atm)
        self.screen_takecash.grid(row=2, column=2,rowspan=3, pady=5)
        

at = Atm()