from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import re
from PyQt5.uic import loadUiType
import mysql.connector as con
import datetime
from xlrd import *
from xlsxwriter import *
ui,_=loadUiType('login.ui')
ui_form,_=loadUiType('library.ui')

class Mess():
    def message_warning(self,message):
        msg = QMessageBox()      
        msg.setWindowTitle("Info")
        msg.setText(message)
        msg.setIcon(QMessageBox.Warning)
        x = msg.exec_()
    def message_critical(self,message):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText(message)
        msg.setIcon(QMessageBox.Critical)
        x = msg.exec_()
    def message_information(self,message):
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText(message)
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()  
j=0
class Login(QWidget,ui):
    c=Mess()
    try:
        def __init__(self):
            QWidget.__init__(self)
            self.setupUi(self)
            self.pushButton.clicked.connect(self.Handle_login)
            style = open("Theme/dark_blue.css", 'r')
            style = style.read()
            self.setStyleSheet(style)
            self.db = con.connect(host='localhost', user='root', password='root', db='library')
            self.cur = self.db.cursor()

        def Handle_login(self):
            username = self.lineEdit.text()
            password = self.lineEdit_2.text()
            if username!='' and password!='':
                self.cur.execute('''SELECT user_password FROM users where user_name=%s''',[(username)])
                data = self.cur.fetchall()
                if len(data)!=0:
                    if password==data[0][0]:
                        self.window2=MainApp()
                        self.close()
                        self.window2.show()
                    else:
                        self.c.message_warning("Your password does not match")
                else:
                    self.c.message_warning("Your username and password does not match")
                    self.lineEdit.setText('')
                    self.lineEdit_2.setText('')
                    self.lineEdit.setFocus()
            else:
                self.c.message_critical("Please Insert Entry!")
                self.lineEdit.setFocus()
    except Exception as e:
        print("Error is ",e)
        self.Mess.message_warning("Something Went Wrong")

o=0
list_book=[]

class MainApp(QMainWindow,ui_form):
    c=Mess()
    def __init__(self):
        self.db = con.connect(host='localhost', user='root', password='root', db='library')
        self.cur = self.db.cursor()
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_UI_Changes()
        self.Handel_Buttons()
        self.Show_category()
        self.Show_author()
        self.Show_publisher()
        self.Show_category_list()
        self.Show_authors_list()
        self.Show_publisher_list()
        self.Dark_Blue_Theme()
        self.Show_All_Student()
        self.Show_All_Books()
        self.Show_Handle_Operation()
        self.Sethover_text()
        type=self.comboBox.currentText()
        if type=='Retrieve':
            self.comboBox_2.setFrame(False)
        else:
            self.comboBox_2.setFrame(True)

    def Handel_UI_Changes(self):
        self.Hiding_Themes()
        #To hide The tab bar
        self.tabWidget_3.tabBar().setVisible(False)
            
    def Sethover_text(self):
        self.pushButton.setToolTip("Day to Day Operation")
        self.pushButton_2.setToolTip("Books")
        self.pushButton_3.setToolTip("Users")
        self.pushButton_4.setToolTip("Setting")
        self.pushButton_5.setToolTip("Theme")
        self.pushButton_22.setToolTip("Student")

    def Handel_Buttons(self):
        self.pushButton_5.clicked.connect(self.Show_Themes)
        self.pushButton_21.clicked.connect(self.Hiding_Themes)
        self.pushButton.clicked.connect(self.Open_Day_To_Day_tab)
        self.pushButton_2.clicked.connect(self.Open_Book_Tab)
        self.pushButton_3.clicked.connect(self.Open_Users_Tab)
        self.pushButton_4.clicked.connect(self.Open_Settings_Tab)
        self.pushButton_22.clicked.connect(self.Open_Student_Tab)
        self.pushButton_14.clicked.connect(self.Add_category)
        self.pushButton_15.clicked.connect(self.Add_Author)
        self.pushButton_16.clicked.connect(self.Add_Publisher)

        self.pushButton_7.clicked.connect(self.Add_New_Books)
        self.pushButton_10.clicked.connect(self.Search_Books)
        self.pushButton_8.clicked.connect(self.Edit_Books)
        self.pushButton_9.clicked.connect(self.Delete_Books)
        self.pushButton_11.clicked.connect(self.Add_New_User)
        self.pushButton_13.clicked.connect(self.Login)
        self.pushButton_12.clicked.connect(self.Edit_User)

        self.pushButton_17.clicked.connect(self.Dark_Blue_Theme)
        self.pushButton_18.clicked.connect(self.Dark_Gray_Theme)
        self.pushButton_19.clicked.connect(self.Dark_Orange_Theme)
        self.pushButton_20.clicked.connect(self.Q_Dark_Theme)

        self.pushButton_26.clicked.connect(self.Add_Student)
        self.pushButton_25.clicked.connect(self.Search_Student)
        self.pushButton_23.clicked.connect(self.Edit_Student)
        self.pushButton_24.clicked.connect(self.Delete_Student)

        self.pushButton_6.clicked.connect(self.Handle_Day_Operation)
        self.pushButton_28.clicked.connect(self.Excel_Day_Operations)
        self.pushButton_27.clicked.connect(self.Excel_Books)
        self.pushButton_29.clicked.connect(self.Excel_Students)

        self.pushButton_30.clicked.connect(self.Search_Day_Books)
        self.pushButton_31.clicked.connect(self.Back_Button)
        self.pushButton_32.clicked.connect(self.Next_Button)
        self.pushButton_33.clicked.connect(self.log_out)

    def Show_Themes(self):
        self.groupBox_3.show()
    def Hiding_Themes(self):
        self.groupBox_3.hide()
    #######################Opening Tab##############################################
    def Open_Day_To_Day_tab(self):
        self.tabWidget_3.setCurrentIndex(0)
    def Open_Book_Tab(self):
        self.tabWidget_3.setCurrentIndex(1)
    def Open_Student_Tab(self):
        self.tabWidget_3.setCurrentIndex(2)
    def Open_Users_Tab(self):
        self.tabWidget_3.setCurrentIndex(3)
    def Open_Settings_Tab(self):
        self.tabWidget_3.setCurrentIndex(4)        

    ########################  Logout Section ############################################################
    def log_out(self):
        response = QMessageBox.warning(self, "Logout", "Are you want to logout",QMessageBox.Yes | QMessageBox.No)
        if response == QMessageBox.Yes:
            self.close()
            self.window2=Login()
            self.window2.show()
        else:
            self.lineEdit.setFocus()
    ############################# Handle Day to day Operation ##############################################
    def Show_Handle_Operation(self):
        self.cur.execute('''SELECT book_name,roll_no,type,date,to_date FROM dayoperation''')
        data=self.cur.fetchall()
        if data:
            self.tableWidget.setRowCount(0)
            self.tableWidget.insertRow(0)
            for row,form in enumerate(data):
                for column,item in enumerate(form):
                    self.tableWidget.setItem(row,column,QTableWidgetItem(str(item)))
                    column+=1
                row_position=self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_position)
        else:
            self.tableWidget.clearContents()
    def Handle_Day_Operation(self):
        book_name=self.lineEdit.text()
        roll_no=self.lineEdit_2.text()
        type=self.comboBox.currentText()
        days=self.comboBox_2.currentIndex()+1
        today_date=datetime.date.today()
        to_date=today_date + datetime.timedelta(days=int(days))

        self.cur.execute('''SELECT book_name,total_books FROM book''')
        book_data = self.cur.fetchall()
        self.cur.execute('''SELECT roll_no FROM student''')
        student_data=self.cur.fetchall()
            
        student_list = list(sum(student_data, ()))   
        book_list=[]
        total_book=[]
        for each in book_data:
            book_list.append(each[0])
            total_book.append(each[1])    
        if book_name!='' and roll_no!='':
            if book_name not in book_list:
                self.c.message_critical("Book does not Exist in Our Library")                    
            elif roll_no not in student_list:
                self.c.message_critical("Roll no. does not Exist in Our Database")
            else:
                book_index=book_list.index(book_name)
                total_books=total_book[book_index]
                if total_books!=0:
                    if type=='Rent':
                        total_books-=1
                    if type=='Retrieve':
                        total_books+=1
                    self.cur.execute('''INSERT INTO dayoperation(book_name,roll_no,type,date,to_date) VALUES (%s,%s,%s,%s,%s) ''',(book_name,roll_no,type,today_date,to_date))
                    self.cur.execute('''UPDATE book SET total_books=%s WHERE book_name=%s''',(total_books,book_name))
                    self.db.commit()
                    self.lineEdit.setText('')
                    self.lineEdit_2.setText('')
                    self.comboBox.setCurrentIndex(0)
                    self.comboBox_2.setCurrentIndex(0)
                    self.Show_Handle_Operation()
                    self.Show_All_Books()
                    self.c.message_information("Add Successfully!")
                else:
                    self.c.message_critical("Book is not Available in Our Library")
        else:
            self.c.message_critical("Please Insert Entry!")
            self.lineEdit.setFocus()

    ############################# Search Books ##############################################
    def Search_Day_Books(self):
        global j,o,list_book
        list_book=[]
        book_name=self.lineEdit_37.text()
        if book_name!='':
            self.cur.execute('''SELECT book_name,roll_no,type,date,to_date FROM dayoperation where book_name=%s''',[(book_name)])
            data=self.cur.fetchall()
            if len(data)!=0:
                for each in data:
                    list_book.append(each)                   
            else:
                self.c.message_warning("Book is not Exist in list")
                self.lineEdit_37.setFocus()    
                self.lineEdit_37.setText('')
                self.lineEdit_3.setText('')
                self.lineEdit_4.setText('')
                self.lineEdit_5.setText('')
                self.lineEdit_6.setText('')
                self.lineEdit_7.setText('')                  
            if list_book:  
                self.groupBox_5.setEnabled(True)
                self.lineEdit_3.setText(list_book[0][0])
                self.lineEdit_4.setText(list_book[0][1])
                self.lineEdit_5.setText(list_book[0][2])
                self.lineEdit_6.setText(str(list_book[0][3]))
                self.lineEdit_7.setText(str(list_book[0][4]))
                j=1
        else:
            self.c.message_critical("Please Insert Entry!")
            self.lineEdit_37.setFocus()

    def Back_Button(self):
        global list_book,o,j
        i=len(list_book)
        if i!=1:
            if o>0:
                self.lineEdit_3.setText(list_book[0][0])
                self.lineEdit_4.setText(list_book[o][1])
                self.lineEdit_5.setText(list_book[o][2])
                self.lineEdit_6.setText(str(list_book[o][3]))
                self.lineEdit_7.setText(str(list_book[o][4]))
                o-=1 
                j=o+1
            else:
                self.lineEdit_3.setText(list_book[0][0])
                self.lineEdit_4.setText(list_book[o][1])
                self.lineEdit_5.setText(list_book[o][2])
                self.lineEdit_6.setText(str(list_book[o][3]))
                self.lineEdit_7.setText(str(list_book[o][4]))
                j=1
    def Next_Button(self):
        global list_book,j,o
        i=len(list_book)
        if i!=1:
            if j<i-1:
                self.lineEdit_3.setText(list_book[j][0])
                self.lineEdit_4.setText(list_book[j][1])
                self.lineEdit_5.setText(list_book[j][2])
                self.lineEdit_6.setText(str(list_book[j][3]))
                self.lineEdit_7.setText(str(list_book[j][4]))
                j+=1
                o=j-1
            else:
                self.lineEdit_3.setText(list_book[j][0])
                self.lineEdit_4.setText(list_book[j][1])
                self.lineEdit_5.setText(list_book[j][2])
                self.lineEdit_6.setText(str(list_book[j][3]))
                self.lineEdit_7.setText(str(list_book[j][4]))
                o=j-1

    ############################# Books ##############################################
    def Show_All_Books(self):
        self.cur.execute('''SELECT book_name,book_category,book_code,book_description,book_author,book_publisher,book_price,total_books FROM book''')
        data = self.cur.fetchall()
        if data:
            self.tableWidget_5.setRowCount(0)
            self.tableWidget_5.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_5.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1
                row_position = self.tableWidget_5.rowCount()
                self.tableWidget_5.insertRow(row_position)
        else:
            self.tableWidget_5.clearContents()

    def Add_New_Books(self):
        book_name=self.lineEdit_8.text()
        book_code=self.lineEdit_9.text()
        book_price = self.lineEdit_10.text()
        book_description=self.textEdit.toPlainText()
        book_category=self.comboBox_3.currentText()
        book_author=self.comboBox_4.currentText()
        book_publisher=self.comboBox_5.currentText()
        total_books= self.lineEdit_40.text()

        if book_name!='' and book_code!='' and book_price!='' and book_description!='' and total_books!='':
            self.cur.execute('''INSERT INTO book(book_name,book_category,book_code,book_description,book_author,book_publisher,book_price,total_books) 
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s)''',(book_name,book_category,book_code,book_description,book_author,book_publisher,book_price,total_books))
            self.db.commit()
            self.lineEdit_8.setText('')
            self.lineEdit_9.setText('')
            self.lineEdit_10.setText('')
            self.lineEdit_40.setText('')
            self.textEdit.setPlainText('')
            self.comboBox_3.setCurrentIndex(0)
            self.comboBox_4.setCurrentIndex(0)
            self.comboBox_5.setCurrentIndex(0)
            self.Show_All_Books()
            self.c.message_information("Add Successfully!")
        else:
            self.c.message_critical("Please Insert Entry!")
            self.lineEdit_2.setFocus()
    ###############################################  Searching Books ##########################################
    def setText_book(self):
        self.lineEdit_11.setText('')
        self.lineEdit_12.setText('')
        self.lineEdit_13.setText('')
        self.lineEdit_14.setText('')
        self.lineEdit_41.setText('')
        self.textEdit_2.setPlainText('')
        self.comboBox_6.setCurrentIndex(0)
        self.comboBox_7.setCurrentIndex(0)
        self.comboBox_8.setCurrentIndex(0)
        self.groupBox_6.setEnabled(False)
        self.Show_All_Books()
        self.lineEdit_11.setFocus()
    def Search_Books(self):
        book_name=self.lineEdit_11.text()
        if book_name!='':
            self.cur.execute('''SELECT * FROM book WHERE book_name=%s''',[(book_name)])
            data=self.cur.fetchone()
            if data!=None:
                self.groupBox_6.setEnabled(True)
                self.lineEdit_12.setText(data[1])
                self.lineEdit_13.setText(data[3])
                self.comboBox_8.setCurrentText(data[2])
                self.textEdit_2.setPlainText(data[4])
                self.comboBox_7.setCurrentText(data[5])
                self.comboBox_6.setCurrentText(data[6])
                self.lineEdit_14.setText(str(data[7]))
                self.lineEdit_41.setText(str(data[8]))
            else:
                self.c.message_warning("Book is not Exist in Library")
                self.setText_book()
        else:
            self.c.message_critical("Please Insert Entry!")
            self.lineEdit_11.setFocus()
    ##################################################### Edit Details Of Book #############################################
    def Edit_Books(self):
        search_book_name = self.lineEdit_11.text()
        book_name = self.lineEdit_12.text()
        book_code = self.lineEdit_13.text()
        book_price = self.lineEdit_14.text()
        total_books= self.lineEdit_41.text()
        book_description = self.textEdit_2.toPlainText()
        book_category = self.comboBox_8.currentText()
        book_author = self.comboBox_7.currentText()
        book_publisher = self.comboBox_6.currentText()

        response = QMessageBox.warning(self, "Update", "Do you want to update book details",QMessageBox.Yes | QMessageBox.No)
        if response == QMessageBox.Yes:
            self.cur.execute('''UPDATE book SET book_name=%s,book_category=%s,book_code=%s,book_description=%s,
            book_author=%s,book_publisher=%s,book_price=%s,total_books=%s WHERE book_name=%s''',(book_name,book_category,book_code,book_description,
                                                                    book_author,book_publisher,book_price,total_books,search_book_name))
            self.db.commit()
            self.setText_book()
            self.c.message_information("Update Successfully!")
        else:
            self.lineEdit_11.setFocus()
    def Delete_Books(self):
        book_name = self.lineEdit_12.text()
        response=QMessageBox.warning(self,"Delete Book","Are you want to delete this book",QMessageBox.Yes|QMessageBox.No)
        if response ==QMessageBox.Yes:
            self.cur.execute('''DELETE FROM book WHERE book_name=%s''',[(book_name)])
            self.db.commit()
            self.setText_book()
            self.c.message_information("Delete Successfully!")
        else:
            self.lineEdit_11.setFocus()
    ###################### Student ####################################################
    def Show_All_Student(self):
        self.cur.execute('''SELECT roll_no,student_name,branch,mobile_no,email FROM student''')
        data=self.cur.fetchall()
        if data:
            self.tableWidget_6.setRowCount(0)
            self.tableWidget_6.insertRow(0)
            for row,form in enumerate(data):
                for column,item in enumerate(form):
                    self.tableWidget_6.setItem(row,column,QTableWidgetItem(str(item)))
                    column+=1
                row_position = self.tableWidget_6.rowCount()
                self.tableWidget_6.insertRow(row_position)
        else:
            self.tableWidget_6.clearContents()
    def check(self,email): 
        # Make a regular expression 
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        # for custom mails use: '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'  
        if(re.search(regex,email)):  
            return True  
        else:  
            return False

    def Add_Student(self):
        roll_no = self.lineEdit_15.text()
        student_name=self.lineEdit_16.text()
        branch=self.lineEdit_17.text()
        mobile_no=self.lineEdit_18.text()
        email=self.lineEdit_38.text()

        if roll_no!='' and student_name!='' and branch!='' and mobile_no!='' and email!='':
            val=self.check(email)
            if val==True:
                if re.search(r'([6789]\d{9}?)',mobile_no) and len(mobile_no) == 10:
                    self.cur.execute('''INSERT INTO student(roll_no,student_name,branch,mobile_no,email) VALUES (%s,%s,%s,%s,%s)''',(roll_no,student_name,branch,mobile_no,email))
                    self.db.commit()
                    self.lineEdit_15.setText('')
                    self.lineEdit_16.setText('')
                    self.lineEdit_17.setText('')
                    self.lineEdit_18.setText('')
                    self.lineEdit_38.setText('')
                    self.Show_All_Student()
                    self.c.message_information("Add Successfully!")
                    self.lineEdit_15.setFocus()
                else:
                    self.c.message_warning("Please insert Valid Mobile No.")
            else:
                self.c.message_warning("Please insert Valid Email-id")
        else:
            self.c.message_critical("Please Insert Entry!")
            self.lineEdit_15.setFocus()
    ##############################################  Search Details of Student  ########################################
    def setText_student(self):
        self.groupBox_7.setEnabled(False)
        self.lineEdit_22.setText('')
        self.lineEdit_23.setText('')
        self.lineEdit_24.setText('')
        self.lineEdit_25.setText('')
        self.lineEdit_26.setText('')
        self.lineEdit_39.setText('')
        self.lineEdit_23.setFocus()
        self.Show_All_Student()
    def Search_Student(self):
        roll_no=self.lineEdit_22.text()
        if roll_no!='':
            self.cur.execute('''SELECT * FROM student WHERE roll_no=%s''', [(roll_no)])
            data=self.cur.fetchone()
            if data!=None:
                self.groupBox_7.setEnabled(True)
                self.lineEdit_23.setText(data[1])
                self.lineEdit_24.setText(data[2])
                self.lineEdit_25.setText(data[3])
                self.lineEdit_26.setText(data[4])
                self.lineEdit_39.setText(data[5])
            else:
                self.c.message_warning("Roll No. is not exist")
                self.setText_student()
        else:
            self.c.message_critical("Please Insert Entry!")
            self.lineEdit_22.setFocus()
    ##################################################### Edit Details Of Student #############################################
    def Edit_Student(self):
        original_roll_no=self.lineEdit_22.text()
        roll_no = self.lineEdit_23.text()
        student_name = self.lineEdit_24.text()
        branch = self.lineEdit_25.text()
        mobile_no = self.lineEdit_26.text()
        email= self.lineEdit_39.text()
        val=self.check(email)
        if roll_no!='' and student_name!='' and branch!='' and mobile_no!='' and email!='': 
            if val==True:
                if re.search(r'([6789]\d{9}?)',mobile_no) and len(mobile_no) == 10:
                    response=QMessageBox.warning(self,"Warning","Are you want to update detail",QMessageBox.Yes|QMessageBox.No)
                    if response==QMessageBox.Yes:
                        self.cur.execute('''UPDATE student SET roll_no=%s,student_name=%s,branch=%s,mobile_no=%s,email=%s WHERE roll_no=%s''',(roll_no,student_name,branch,mobile_no,
                                                                                                                    email,original_roll_no))
                        self.db.commit()
                        self.setText_student()
                        self.c.message_information("Update Successfully!")
                    else:
                        self.lineEdit_23.setFocus()
                else:
                    self.c.message_warning("Please insert Valid Mobile No.")
            else:
                self.c.message_warning("Please insert Valid Email-id")
        else:
            self.c.message_critical("Please Insert Entry!")
            self.lineEdit_22.setFocus()

    def Delete_Student(self):
        roll_no = self.lineEdit_23.text()
        response = QMessageBox.warning(self, "Delete Book", "Are you want to delete this student details",QMessageBox.Yes | QMessageBox.No)
        if response == QMessageBox.Yes:
            self.cur.execute('''DELETE FROM student WHERE roll_no=%s''', [(roll_no)])
            self.db.commit()
            self.setText_student()
            self.c.message_information("Delete Successfully!")
        else:
            self.lineEdit_23.setFocus()
    ###################### Users ####################################################
    def Add_New_User(self):
        username=self.lineEdit_27.text()
        email=self.lineEdit_28.text()
        password=self.lineEdit_29.text()
        password2=self.lineEdit_30.text()
        if username!='' and email!='' and password!='' and password2!='':
            if password==password2:
                self.cur.execute('''INSERT INTO USERS(user_name,user_email,user_password) VALUES (%s,%s,%s)''',(username,email,password))
                self.db.commit()
                self.lineEdit_27.setText('')
                self.lineEdit_28.setText('')
                self.lineEdit_29.setText('')
                self.lineEdit_30.setText('')
                self.c.message_information("Add Successfully!")
            else:
                self.label_30.setText('Password does not Match!')
                self.lineEdit_29.setText('')
                self.lineEdit_30.setText('')
                self.lineEdit_29.setFocus()
        else:
            self.c.message_critical("Please Insert Entry!")
            self.lineEdit_27.setFocus()

    def Login(self):
        username=self.lineEdit_31.text()
        password=self.lineEdit_32.text()
        if username!='' and password!='':
            self.cur.execute('''SELECT * FROM users''')
            data=self.cur.fetchall()
            for row in data:
                if username==row[1] and password==row[3]:
                    self.groupBox_4.setEnabled(True)
                    self.lineEdit_33.setText(row[1])
                    self.lineEdit_34.setText(row[2])
                    self.lineEdit_35.setText(row[3])
                    self.lineEdit_36.setText(row[3])
                    self.c.message_information("Login Successfully!")
        else:
            self.c.message_critical("Please Insert Entry!")
            self.lineEdit_31.setFocus()

    def Edit_User(self):
        original_name=self.lineEdit_31.text()
        username = self.lineEdit_33.text()
        email = self.lineEdit_34.text()
        password = self.lineEdit_35.text()
        password2 = self.lineEdit_36.text()

        if password==password2:
            response=QMessageBox.warning(self,"Update","Do you want to update details",QMessageBox.Yes|QMessageBox.No)
            if response==QMessageBox.Yes:
                self.cur.execute('''UPDATE users SET user_name=%s,user_email=%s,user_password=%s WHERE user_name=%s''',(username,email,password,original_name))
                self.db.commit()
                self.lineEdit_33.setText('')
                self.lineEdit_34.setText('')
                self.lineEdit_35.setText('')
                self.lineEdit36.setText('')
                self.label_31.setText('')
                self.lineEdit_31.setFocus()
                self.groupBox_4.setEnabled(False)
                self.c.message_information("Update Successfully!")
        else:
            self.label_31.setText('Password does not Match!')
            self.lineEdit_31.setText('')
            self.lineEdit_32.setText('')
            self.lineEdit_31.setFocus()
    ######################################## Setting ####################################################
    def Add_category(self):
        category_name=self.lineEdit_19.text()
        if category_name != "":
            self.cur.execute('''INSERT INTO category(category_name) VALUES (%s)''',(category_name,))
            self.db.commit()
            self.Show_category()
            self.Show_category_list()
            self.c.message_information("Add Successfully!")
            self.lineEdit_19.setText('')
            self.lineEdit_19.setFocus()
        else:
            self.c.message_critical("Please Insert Entry!")
            self.lineEdit_19.setFocus()

    def Show_category(self):
        self.cur.execute('''SELECT category_name FROM category''')
        data_category=self.cur.fetchall()

        if data_category:
            self.tableWidget_2.setRowCount(0)
            self.tableWidget_2.insertRow(0)
            for row,form in enumerate(data_category):
                for column,item in enumerate(form):
                    self.tableWidget_2.setItem(row,column,QTableWidgetItem(str(item)))
                    column+=1
                row_position=self.tableWidget_2.rowCount()
                self.tableWidget_2.insertRow(row_position)
        else:
            self.tableWidget_2.clearContents()

    def Add_Author(self):
        author_name = self.lineEdit_20.text()
        if author_name!='':
            self.cur.execute('''INSERT INTO authors(author_name) VALUES (%s)''', (author_name,))
            self.db.commit()
            self.Show_author()
            self.Show_authors_list()
            self.c.message_information("Add Successfully!")
            self.lineEdit_20.setText('')
            self.lineEdit_20.setFocus()
        else:
            self.c.message_critical("Please Insert Entry!")
            self.lineEdit_20.setFocus()

    def Show_author(self):
        self.cur.execute('''SELECT author_name FROM authors''')
        data_author=self.cur.fetchall()

        if data_author:
            self.tableWidget_3.setRowCount(0)
            self.tableWidget_3.insertRow(0)
            for row,form in enumerate(data_author):
                for column,item in enumerate(form):
                    self.tableWidget_3.setItem(row,column,QTableWidgetItem(str(item)))
                    column+=1
                row_position = self.tableWidget_3.rowCount()
                self.tableWidget_3.insertRow(row_position)
        else:
            self.tableWidget_3.clearContents()

    def Add_Publisher(self):
        publisher_name = self.lineEdit_21.text()
        if publisher_name!='':
            self.cur.execute('''INSERT INTO publisher(publisher_name) VALUES (%s)''', (publisher_name,))
            self.db.commit()
            self.Show_publisher()
            self.Show_publisher_list()
            self.c.message_information("Add Successfully!")
            self.lineEdit_21.setText('')
            self.lineEdit_21.setFocus()
        else:
            self.c.message_critical("Please Insert Entry!")
            self.lineEdit_21.setFocus()

    def Show_publisher(self):
        self.cur.execute('''SELECT publisher_name FROM publisher''')
        data_publisher=self.cur.fetchall()

        if data_publisher:
            self.tableWidget_4.setRowCount(0)
            self.tableWidget_4.insertRow(0)
            for row,form in enumerate(data_publisher):
                for column,item in enumerate(form):
                    self.tableWidget_4.setItem(row,column,QTableWidgetItem(str(item)))
                    column+=1
                row_position = self.tableWidget_4.rowCount()
                self.tableWidget_4.insertRow(row_position)
        else:
            self.tableWidget_4.clearContents()

    ############################ Show Setting data in UI ############################################
    def Show_category_list(self):
        self.cur.execute('''SELECT category_name FROM category''')
        data_category=self.cur.fetchall()

        self.comboBox_3.clear()
        for item in data_category:
            self.comboBox_3.addItem(item[0])
            self.comboBox_8.addItem(item[0])

    def Show_authors_list(self):
        self.cur.execute('''SELECT author_name FROM authors''')
        data_author = self.cur.fetchall()

        self.comboBox_4.clear()
        for item in data_author:
            self.comboBox_4.addItem(item[0])
            self.comboBox_7.addItem(item[0])

    def Show_publisher_list(self):
        self.cur.execute('''SELECT publisher_name FROM publisher''')
        data_publisher = self.cur.fetchall()

        self.comboBox_5.clear()
        for item in data_publisher:
            self.comboBox_5.addItem(item[0])
            self.comboBox_6.addItem(item[0])

    ############################ Export Section ############################################
    def Excel_Day_Operations(self):
        # book_name = self.lineEdit.text()
        self.cur.execute('''SELECT book_name,roll_no,type,date,to_date FROM dayoperation''')
        data = self.cur.fetchall()
        wb=Workbook('Day_Operations.xlsx')
        sheet1=wb.add_worksheet()

        sheet1.write(0,0,'Book Name')
        sheet1.write(0,1, 'roll_no')
        sheet1.write(0,2, 'Type')
        sheet1.write(0,3, 'From - Date')
        sheet1.write(0,4, 'To - Date')

        row_number=1
        for row in data:
            column=0
            for item in row:
                sheet1.write(row_number,column,str(item))
                column+=1
            row_number+=1
        wb.close()
        self.c.message_information("Export Successfully!")

    def Excel_Books(self):
        self.cur.execute('''SELECT book_name,book_category,book_code,book_description,book_author,book_publisher,book_price FROM book''')
        data = self.cur.fetchall()

        wb=Workbook('Books.xlsx')
        sheet1=wb.add_worksheet()
        sheet1.write(0,0,'Book Name')
        sheet1.write(0,1,'Book Category')
        sheet1.write(0,2,'Book Code')
        sheet1.write(0,3,'Book Description')
        sheet1.write(0,4,'Book Author')
        sheet1.write(0,5,'Book Publisher')
        sheet1.write(0,6,'Book Price')

        row_number = 1
        for row in data:
            column = 0
            for item in row:
                sheet1.write(row_number, column, str(item))
                column += 1
            row_number += 1
        wb.close()
        self.c.message_information("Export Successfully!")

    def Excel_Students(self):
        self.cur.execute('''SELECT roll_no,student_name,branch,mobile_no FROM student''')
        data = self.cur.fetchall()

        wb=Workbook('Students.xlsx')
        sheet1=wb.add_worksheet()
        sheet1.write(0,0,'Roll No.')
        sheet1.write(0,1,'Student Name')
        sheet1.write(0,2,'Email Id')
        sheet1.write(0,3,'Mobile No.')

        row_number = 1
        for row in data:
            column = 0
            for item in row:
                sheet1.write(row_number, column, str(item))
                column += 1
            row_number += 1
        wb.close()
        self.c.message_information("Export Successfully!")

    ############################ Theme Section ############################################
    def Dark_Blue_Theme(self):
        style=open("Theme/dark_blue.css",'r')
        style=style.read()
        self.setStyleSheet(style)
    def Dark_Orange_Theme(self):
        style = open("Theme/dark_orange.css", 'r')
        style = style.read()
        self.setStyleSheet(style)
    def Dark_Gray_Theme(self):
        style = open("Theme/dark_gray.css", 'r')
        style = style.read()
        self.setStyleSheet(style)
    def Q_Dark_Theme(self):
        style = open("Theme/qdark.css", 'r')
        style = style.read()
        self.setStyleSheet(style)
    
    
def main():
    app=QApplication(sys.argv)
    window=Login()
    window.show()
    app.exec_()

if __name__=='__main__':
    main()
