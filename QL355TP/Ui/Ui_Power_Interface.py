'''
Created on 7 mag 2020

@author: andrea
'''
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from icons import *

Ui_TTi_Ver = "0.2.0 alpha"
class Ui_Interface(QMainWindow):
    def __init__(self, parent = None):
        super(Ui_Interface, self).__init__(parent)
        # ---- Setting Intarface Base --------------
        self.Central_Widget = QWidget()
        self.setWindowIcon(QIcon(':/Panoratux.png'))
        self.setGeometry(QRect(160,140,650,500))
        #------ Displays ----------------------------
        Font_Display = QFont()
        Font_Display.setPointSize(25)
        Font_Display.setItalic(True)
        Font_Display.setBold(True)
        Frame_10 = self.Make_Frame()
        Frame_11 = self.Make_Frame()
        self.Status_Bar = self.statusBar()
        self.Display_V_10 = self.Make_Display('-----')
        self.Display_I_10 = self.Make_Display('-----')
        self.Display_V_11 = self.Make_Display('-----')
        self.Display_I_11 = self.Make_Display('-----')
        Label_V_10 = QLabel('Volts')
        Label_V_11 = QLabel('Volts')
        Label_I_10 = QLabel('Amps')
        Label_I_11 = QLabel('Amps')
     
        
        self.Table_10 = QGridLayout()
        self.Table_10.addWidget(self.Display_V_10 ,0,0)
        self.Table_10.addWidget(self.Display_I_10 ,0,1)
        self.Table_10.addWidget(Label_V_10, 1,0)
        self.Table_10.addWidget(Label_I_10, 1,1)
        Frame_10.setLayout(self.Table_10) #imposta la tabella dentra  al frame
        
        self.Table_11 = QGridLayout()
        self.Table_11.addWidget(self.Display_V_11 ,0,0)
        self.Table_11.addWidget(self.Display_I_11 ,0,1)
        self.Table_11.addWidget(Label_V_11, 1,0)
        self.Table_11.addWidget(Label_I_11, 1,1)
        Frame_11.setLayout(self.Table_11) #imposta la tabella dentra  al frame
        
        
        
        # --- select Range V-I -----------------------------
        Frame_20 = self.Make_Frame()
        Frame_21 = self.Make_Frame()
        Label_20 = QLabel('15V-5A')
        Label_21 = QLabel('35-3A')
        Label_22 = QLabel('35-0.5A')
        self.Led_20 = QLabel()
        self.Led_20.setPixmap(self.Make_Led('Led_Spento.png'))
        self.Led_21 = QLabel()
        self.Led_21.setPixmap(self.Make_Led('Led_Spento.png'))
        self.Led_22 = QLabel()
        self.Led_22.setPixmap(self.Make_Led('Led_Spento.png'))
        self.Button_20 = QPushButton()
        self.Button_20.setMaximumWidth(40)
        self.Button_21 = QPushButton()
        self.Button_21.setMaximumWidth(40)
        self.Button_22 = QPushButton()
        self.Button_22.setMaximumWidth(40)
        
        Label_23 = QLabel('15V-5A')
        Label_24 = QLabel('35-3A')
        Label_25 = QLabel('35-0.5A')
        self.Led_23 = QLabel()
        self.Led_23.setPixmap(self.Make_Led('Led_Spento.png'))
        self.Led_24 = QLabel()
        self.Led_24.setPixmap(self.Make_Led('Led_Spento.png'))
        self.Led_25 = QLabel()
        self.Led_25.setPixmap(self.Make_Led('Led_Spento.png'))
        self.Button_23 = QPushButton()
        self.Button_23.setMaximumWidth(40)
        self.Button_24 = QPushButton()
        self.Button_24.setMaximumWidth(40)
        self.Button_25 = QPushButton()
        self.Button_25.setMaximumWidth(40)
        
        Table_20 = QGridLayout()
        Table_20.addWidget(Label_20 ,0,0, Qt.Alignment(Qt.AlignCenter))
        Table_20.addWidget(Label_21 ,0,1, Qt.Alignment(Qt.AlignCenter))
        Table_20.addWidget(Label_22 ,0,2, Qt.Alignment(Qt.AlignCenter))
        Table_20.addWidget(self.Led_20 ,1,0, Qt.Alignment(Qt.AlignCenter))
        Table_20.addWidget(self.Led_21 ,1,1, Qt.Alignment(Qt.AlignCenter))
        Table_20.addWidget(self.Led_22 ,1,2, Qt.Alignment(Qt.AlignCenter))
        Table_20.addWidget(self.Button_20 ,2,0, Qt.Alignment(Qt.AlignCenter))
        Table_20.addWidget(self.Button_21 ,2,1, Qt.Alignment(Qt.AlignCenter))
        Table_20.addWidget(self.Button_22 ,2,2, Qt.Alignment(Qt.AlignCenter))
        Frame_20.setLayout(Table_20)
        
        Table_21 = QGridLayout()
        Table_21.addWidget(Label_23 ,0,0, Qt.Alignment(Qt.AlignCenter))
        Table_21.addWidget(Label_24 ,0,1, Qt.Alignment(Qt.AlignCenter))
        Table_21.addWidget(Label_25 ,0,2, Qt.Alignment(Qt.AlignCenter))
        Table_21.addWidget(self.Led_23 ,1,0, Qt.Alignment(Qt.AlignCenter))
        Table_21.addWidget(self.Led_24 ,1,1, Qt.Alignment(Qt.AlignCenter))
        Table_21.addWidget(self.Led_25 ,1,2, Qt.Alignment(Qt.AlignCenter))
        Table_21.addWidget(self.Button_23 ,2,0, Qt.Alignment(Qt.AlignCenter))
        Table_21.addWidget(self.Button_24 ,2,1, Qt.Alignment(Qt.AlignCenter))
        Table_21.addWidget(self.Button_25 ,2,2, Qt.Alignment(Qt.AlignCenter))
        Frame_21.setLayout(Table_21)
        
        #---- set v(out) I(max out) --------------
        
        Frame_30 = self.Make_Frame() #istanzia un frame (tramite funzione)
        Frame_31 = self.Make_Frame() #istanzia un frame (tramite funzione)
        Label_30 = QLabel('Set V')
        Label_31 = QLabel('Set I')
        self.Set_V_30 = QDoubleSpinBox()
        self.Set_V_30.setDecimals(3)
        self.Set_V_30.setMaximum(35)
        self.Set_I_30 = QDoubleSpinBox()
        self.Set_I_30.setDecimals(3)
        self.Set_I_30.setMaximum(5)
        self.Button_30 = QPushButton("Confirm")
                
        Label_32 = QLabel('Set V')
        Label_33 = QLabel('Set I')
        self.Set_V_31 = QDoubleSpinBox()
        self.Set_V_31.setDecimals(3)
        self.Set_V_31.setMaximum(35)
        self.Set_I_31 = QDoubleSpinBox()
        self.Set_I_31.setDecimals(3)
        self.Set_I_31.setMaximum(5)
        self.Button_31 = QPushButton("Confirm")

        Table_30 = QHBoxLayout() #crea tabella orrizontale per le label V/I (1)
        Table_30.addWidget(Label_30)
        Table_30.addWidget(Label_31)
        Table_31 = QHBoxLayout() #crea tabella orrizontale per i dublespin V/I (1)
        Table_31.addWidget(self.Set_V_30)
        Table_31.addWidget(self.Set_I_30)

        Table_33 = QVBoxLayout() #crea uan tabella verticale dove inserire le tue tabelle + pulsante
        Table_33.addLayout(Table_30)
        Table_33.addStretch() #aggiunge un elatico tar i layout
        Table_33.addLayout(Table_31)
        Table_33.addStretch()
        Table_33.addWidget(self.Button_30)
        Frame_30.setLayout(Table_33)# inserisce la table33 in un frame
        
        Table_310 = QHBoxLayout() #crea tabella orrizontale per le label V/I (2)
        Table_310.addWidget(Label_32)
        Table_310.addWidget(Label_33)
        Table_311 = QHBoxLayout() #crea tabella orrizontale per i dublespin V/I (2)
        Table_311.addWidget(self.Set_V_31)
        Table_311.addWidget(self.Set_I_31)

        Table_313 = QVBoxLayout()
        Table_313.addLayout(Table_310)
        Table_313.addStretch()
        Table_313.addLayout(Table_311)
        Table_313.addStretch()
        Table_313.addWidget(self.Button_31)
        Frame_31.setLayout(Table_313)
        
        #------ On / OFF (Vout) ------------------
        Frame_40 = self.Make_Frame()
        Frame_41 = self.Make_Frame()
        self.Button_ONOFF_40 = QPushButton('ON-OFF')
        self.Button_ONOFF_40.setCheckable(True)
        self.Led_40 = QLabel()
        self.Led_40.setPixmap(self.Make_Led('Led_Verde.png', Dim=60))
        
        self.Button_ONOFF_41 = QPushButton('ON-OFF')
        self.Button_ONOFF_41.setCheckable(True)
        self.Led_41 = QLabel()
        self.Led_41.setPixmap(self.Make_Led('Led_Verde.png', Dim=60))
        
        Table_40 = QHBoxLayout()
        Table_40.addWidget(self.Button_ONOFF_40)
        Table_40.addStretch()
        Table_40.addWidget(self.Led_40)
        Frame_40.setLayout(Table_40)
        
        Table_410 = QHBoxLayout()
        Table_410.addWidget(self.Button_ONOFF_41)
        Table_410.addStretch()
        Table_410.addWidget(self.Led_41)
        Frame_41.setLayout(Table_410)
        
        #----- ALL ON / OFF (Vout double) --------
        Frame_50 = self.Make_Frame()
        self.Button_ON_ALL_50 = QPushButton('All ON')
        self.Button_OFF_ALL_50 = QPushButton('All OFF')
        self.Led_ON_ALL_50 =QLabel()
        self.Led_ON_ALL_50.setPixmap(self.Make_Led('Led_Spento.png', Dim=60))
        self.Led_OFF_ALL_50 = QLabel()
        self.Led_OFF_ALL_50.setPixmap(self.Make_Led('Led_Verde.png', Dim=60))
        
        Table_50 = QHBoxLayout()
        Table_50.addWidget(self.Led_OFF_ALL_50)
        Table_50.addWidget(self.Led_ON_ALL_50)
        Table_50.addStretch()
        Table_50.addWidget(self.Button_OFF_ALL_50)
        Table_50.addWidget(self.Button_ON_ALL_50)
        Frame_50.setLayout(Table_50)
        

        
        #------ tables ---------------------------
        Frame_Pow1 = self.Make_Frame()
        Frame_Pow2 = self.Make_Frame()
        self.Table_PowerS_1 = QVBoxLayout()
        self.Table_PowerS_1.addWidget(Frame_10)
        self.Table_PowerS_1.addWidget(Frame_20)
        self.Table_PowerS_1.addSpacing(20)
        self.Table_PowerS_1.addWidget(Frame_30)
        self.Table_PowerS_1.addSpacing(50)
        self.Table_PowerS_1.addWidget(Frame_40)
        self.Table_PowerS_1.addStretch()
        Frame_Pow1.setLayout(self.Table_PowerS_1)
        
        self.Table_PowerS_2 = QVBoxLayout()
        self.Table_PowerS_2.addWidget(Frame_11)
        self.Table_PowerS_2.addWidget(Frame_21)
        self.Table_PowerS_2.addSpacing(20)
        self.Table_PowerS_2.addWidget(Frame_31)
        self.Table_PowerS_2.addSpacing(50)
        self.Table_PowerS_2.addWidget(Frame_41)
        self.Table_PowerS_2.addStretch()
        Frame_Pow2.setLayout(self.Table_PowerS_2)
        
        #---- sezione per la creazione finale della tabella  o centralW ----
        self.Tabella_test = QHBoxLayout()
        #self.Tabella_test.addLayout(self.Table_PowerS_1)
        #self.Tabella_test.addLayout(self.Table_PowerS_2)
        self.Tabella_test.addWidget(Frame_Pow1)
        self.Tabella_test.addWidget(Frame_Pow2)

        
        self.Tab_test2 = QVBoxLayout(self.Central_Widget)
        self.Tab_test2.addLayout(self.Tabella_test)
        self.Tab_test2.addSpacing(30)
        self.Tab_test2.addWidget(Frame_50)
        print(Ui_TTi_Ver)
        self.setCentralWidget(self.Central_Widget)
        # ------ Inizio Creazioni Azioni per i Menu ---
        self.Act_Usb = self.MakeAction('Usb Connect', 'Usb.png', 'Connect Usb', 'F4')
        self.Act_Angel = self.MakeAction('Angel Connection', 'Angel.png', 'Angel Connetion','F5')
        self.Act_Info = self.MakeAction('ppp', 'Info.png', 'Info UI', 'F10')
        
        # ------ Inizio dei Menu ----------------------
        self.Menu_File = self.menuBar().addMenu('&File') #crea il menu "file"
        self.Menu_Set = self.menuBar().addMenu('&Setting') # crea menu settaggi
        self.Menu_Conn = self.menuBar().addMenu('&Connection') #cra menu connessioni
        self.Menu_Conn_Und = self.Menu_Conn.addMenu(QIcon(':/Connect.png'),'&Type of Connection')
        self.Menu_Conn_Und.addAction(self.Act_Usb)
        self.Menu_Conn_Und.addAction(self.Act_Angel)
        self.Menu_Info = self.menuBar().addMenu('&Info')
        self.Menu_Info.addAction(self.Act_Info)
    # ----- Varie finestre -----------------------
    def Info(self): #Crea una finestra per mostare varie informazioni 
        QMessageBox.about(self,'Remote Inteface for TTi','''<b>pippo</b>''')
        
    # ----- Funzioni ricorsive --------------------
    
    def Make_Display(self, Value):# funzione per la creazione del display
        font = QFont()
        font.setPointSize(25)
        font.setItalic(True)
        font.setBold(True)
        Visual = QLineEdit()
        Visual.setFocusPolicy(Qt.NoFocus)
        Visual.setReadOnly(True)
        Visual.setGeometry(QRect(0,0,300,80))
        Visual.setFont(font)
        Visual.setAlignment(Qt.AlignCenter)
        Visual.setText(Value)
        return Visual
    
    def Make_Line(self, Orientation):
        Line = QFrame()
        if Orientation == "V":
            Line.setFrameShape(QFrame.VLine)
            Line.setFrameShadow(QFrame.Sunken)
        elif Orientation == "H":
            Line.setFrameShape(QFrame.HLine)
            Line.setFrameShadow(QFrame.Sunken)
        return Line
    
    def Make_Frame(self):# funzione per la creazione di un frame
        Frame = QFrame()
        #Frame.setMaximumSize(900, 850)
        Frame.setFrameShape(QFrame.Box)
        Frame.setFrameShadow(QFrame.Raised)
        return Frame
    
    def Make_Led(self, ColorLed, Dim=35):# crea i vari led e li ridimensione
        ImgX = QPixmap(':/{}'.format(ColorLed))
        Scaled_Imgx = ImgX.scaled(Dim, Dim, Qt.KeepAspectRatio,
                                  Qt.SmoothTransformation)
        return Scaled_Imgx
    
    def MakeAction(self, Text, Icon=None, Tip=None, Short=None, Disable=False,
                   ChecK=False, Sel=False):
        ActionX = QAction(Text, self)
        if Icon is not None:
            ActionX.setIcon(QIcon(':/{}'.format(Icon)))
        if Tip is not None:
            ActionX.setToolTip(Tip)
        if Short is not None:
            ActionX.setShortcut(Short)
        if Disable is True:
            ActionX.setDisabled(True)
        if ChecK is True:
            ActionX.setCheckable(True)
        if Sel is True:
            ActionX.setChecked(True)
        return ActionX
        
        
        
if __name__ == '__main__':
    import sys
    print('main grafico')
    app = QApplication(sys.argv)
    form = Ui_Interface()
    form.setWindowTitle('Only For Test...')
    form.Status_Bar.showMessage('Ui Version: {0}'.format(Ui_TTi_Ver),10000)
    form.show()
    app.exec_()