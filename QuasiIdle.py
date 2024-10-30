from SaveAsClass import SaveAsWindow
import subprocess
import os
from SaveAsClass import  read_file_content
from PyQt6.QtWidgets import (  
    QApplication,  
    QMainWindow,  
    QTextEdit,  
    QWidget, 
    QHBoxLayout,
    QPlainTextEdit  
)  
from PyQt6.QtGui import  QAction, QColor 
      
class MainWindow(QMainWindow):  
    def __init__(self):  
        super().__init__()
        self.setWindowTitle("littleIDLE")
       
        self.setGeometry(100, 100, 800, 800)  

       
        central_widget = QWidget()  
        self.setCentralWidget(central_widget)  

      
        layout = QHBoxLayout()  
        central_widget.setLayout(layout)  

        self.code_edit = QTextEdit(self)  
        self.code_edit.setPlaceholderText("Write your Python code here...")
        line_count = self.code_edit.blockCount()
        layout.addWidget(self.code_edit)

        line_number = ""
        for i in range(1,line_count+1):
            line_number += "i\n"
        self.line_number = QTextEdit(self) 
        self.line_number.setFixedSize(20, 800) 
        self.line_number.setPlaceholderText(line_number)
        self.line_number.setReadOnly(True)
        layout.addWidget(self.line_number)
       
        self.output_edit = QTextEdit()  
        self.output_edit.setReadOnly(True)  
        layout.addWidget(self.output_edit) 

        if "Error" in self.output_edit.toPlainText():
             self.output_edit.selectAll()  
             self.output_edit.setTextColor(QColor("red")) 
             self.output_editt.setCurrentFont(self.output_edit.font()) 

        
        menu_bar = self.menuBar()  

       
        file_menu = menu_bar.addMenu("File")  
        new_action = QAction("New", self)  
        open_action = QAction("Open", self)  
        save_action = QAction("Save", self)
        saveAs_action = QAction("Save As", self)  
        exit_action = QAction("Exit", self)  
        exit_action.triggered.connect(self.close) 
        save_action.triggered.connect(self.save_file)
        saveAs_action.triggered.connect(self.saveAs_file)
       # saveAs_action.triggered.connect(SaveAsWindow)

        file_menu.addAction(new_action)  
        file_menu.addAction(open_action)  
        file_menu.addAction(save_action)
        file_menu.addAction(saveAs_action)  
        file_menu.addSeparator()  
        file_menu.addAction(exit_action)  

          
        edit_menu = menu_bar.addMenu("Edit")  
        undo_action = QAction("Undo", self)  
        redo_action = QAction("Redo", self)  
        cut_action = QAction("Cut", self)  
        copy_action = QAction("Copy", self)  
        paste_action = QAction("Paste", self)  
        select_all_action = QAction("Select All", self)  
        find_action = QAction("Find", self)  
        replace_action = QAction("Replace", self)  
 
        undo_action.triggered.connect(self.code_edit.undo)  
        redo_action.triggered.connect(self.code_edit.redo)  
        cut_action.triggered.connect(self.code_edit.cut)  
        copy_action.triggered.connect(self.code_edit.copy)  
        paste_action.triggered.connect(self.code_edit.paste)  
        select_all_action.triggered.connect(self.code_edit.selectAll)  

          
        find_action.triggered.connect(self.find_text)  

         
        replace_action.triggered.connect(self.replace_text)  

       
        edit_menu.addAction(undo_action)  
        edit_menu.addAction(redo_action)  
        edit_menu.addSeparator()  
        edit_menu.addAction(cut_action)  
        edit_menu.addAction(copy_action)  
        edit_menu.addAction(paste_action)  
        edit_menu.addSeparator()  
        edit_menu.addAction(select_all_action)  
        edit_menu.addSeparator()  
        edit_menu.addAction(find_action)  
        edit_menu.addAction(replace_action)  

         
        run_menu = menu_bar.addMenu("Run")  
        run_action = QAction("Run Module", self)   
        run_action.triggered.connect(self.run_file)   
        run_menu.addAction(run_action) 

    def run_file(self):  
        script = self.code_edit.toPlainText()
        with open("empty.py", "w") as f:
           f.write(script)

        p01 = subprocess.getoutput(["python", "empty.py"])
        self.output_edit.setText(p01)
    
    def save_file(self):
        counter = 1
        script = self.code_edit.toPlainText()
        if os.path.exists(f"newfile{counter}.txt"):
            counter += 1
            with open(f"newfile{counter}.txt", "w") as f:
             f.write(script)
            
        else:
            with open(f"newfile{counter}.txt", "w") as f:
             f.write(script)


         
       
    def saveAs_file(self):
                       
        subprocess.getoutput(["python", "SaveAsClass.py"])
    
    def find_text(self):  
         
        print("Find action triggered")  

    def replace_text(self):  
        print("Replace action triggered")  

if __name__ == "__main__":  
    app = QApplication([])  
    window = MainWindow()  
    window.show()  
    app.exec()  