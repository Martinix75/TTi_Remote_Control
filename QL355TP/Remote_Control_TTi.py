'''
Created on 7 mag 2020

@author: andrea
'''

import serial

from Ui import Ui_Power_Interface as POI



'''
class Connect_To():
    def Usb_Conn(self):
        Usb = serial.Serial('/dev/ttyUSB0',19200, timeout =1)
        return Usb
'''            
Remote_TTi_Ver = "0.1.2"

class Remote_TTi(POI.Ui_Interface):
    def __init__(self, parent = None):
        super(Remote_TTi, self).__init__(parent)
        self.Usb_Error = False
        print(POI.Ui_TTi_Ver,Remote_TTi_Ver)
        self.SetUp()
        
    def SetUp(self):
        Usb_OK = self.Usb_Connect()
        if self.Usb_Error == True:
            self.setWindowTitle(self.Init_Interface(Usb_OK, '*idn?\n')[1])
            self.Display_V_10.setText(self.Check_Voltage_1(Usb_OK, 'V1?\n'))
            self.Display_I_10.setText(self.Init_Interface(Usb_OK, 'I1?\n')[0][3:])
            self.Display_V_11.setText(self.Init_Interface(Usb_OK, 'V2?\n')[0][3:])
            self.Display_I_11.setText(self.Init_Interface(Usb_OK, 'I2?\n')[0][3:])
            self.Check_Range_1(Usb_OK, 'RANGE1?\n')
            self.Check_Range_2(Usb_OK, 'RANGE2?\n')
            self.Set_V_30.setValue(float(self.Check_Voltage_1(Usb_OK, 'V1?\n')))
            self.Set_V_31.setValue(float(self.Check_Voltage_2(Usb_OK, 'V2?\n')))
            self.Set_I_30.setValue(float(self.Check_Amp_1(Usb_OK, 'I1?\n')))
            self.Set_I_31.setValue(float(self.Check_Amp_2(Usb_OK, 'I2?\n')))
            #self.Check_Exit_1(Usb_OK, 'OP1?\n')
            Usb_OK.close()
            
        # --- signal -------------------------------------------------------
            self.Button_20.clicked.connect(lambda:self.Set_Range_1('RANGE1 0\n'))
            self.Button_21.clicked.connect(lambda:self.Set_Range_1('RANGE1 1\n'))
            self.Button_22.clicked.connect(lambda:self.Set_Range_1('RANGE1 2\n'))
            self.Button_23.clicked.connect(lambda:self.Set_Range_2('RANGE2 0\n'))
            self.Button_24.clicked.connect(lambda:self.Set_Range_2('RANGE2 1\n'))
            self.Button_25.clicked.connect(lambda:self.Set_Range_2('RANGE2 2\n'))
            '''
            self.Set_V_30.valueChanged.connect(self.Set_Voltage_1)
            self.Set_V_31.valueChanged.connect(self.Set_Voltage_2)
            self.Set_I_30.valueChanged.connect(self.Set_Amp_1)
            self.Set_I_31.valueChanged.connect(self.Set_Amp_2)
            '''
            self.Button_30.clicked.connect(self.Set_Voltage_1)
            self.Button_30.clicked.connect(self.Set_Amp_1)
            self.Button_31.clicked.connect(self.Set_Voltage_2)
            self.Button_31.clicked.connect(self.Set_Amp_2)
            self.Button_ONOFF_40.toggled.connect(self.Enable_Exit_1)
            self.Button_ONOFF_41.toggled.connect(self.Enable_Exit_2)
            self.Button_ON_ALL_50.clicked.connect(self.Enable_Exit_All)
            self.Button_OFF_ALL_50.clicked.connect(self.Disable_Exit_All)
            self.Act_Info.triggered.connect(self.Info)
        if self.Usb_Error == False:
            self.setEnabled(False)
            self.Status_Bar.showMessage('Error USB not connected!')
            self.setWindowTitle('Not Connect!!')
                                       
    def Usb_Connect(self, timeout=.1):
        try:
            Usb = serial.Serial('/dev/ttyUSB0',19200, timeout=timeout)
            self.Usb_Error = True
            return Usb
        except:
            self.Usb_Error = False
            print('Seriale Errore', self.Usb_Error)

    def Init_Interface(self,conn, string):
        self.Write_Data(conn, string)
        Date_I = self.Read_Data(conn)
        return Date_I
    
    def Write_Data(self, conn, string):
        conn.write(string.encode('utf-8'))
        
    def Read_Data (self, conn, size=32):
        Date = conn.read(size)
        print('Read data', Date)
        Date = self.Convert_to_List(Date)
        return Date
    
    def Convert_to_List(self, string):
        Date = string.decode('utf-8')
        Date.replace('\n','')
        Date = Date.split(',')
        print('Convert to list',Date)
        return Date
    
    def Check_Range_1(self, conn, string):
        self.Write_Data(conn, string)
        Data = self.Read_Data(conn)
        print('++++++++++++++',Data)
        Range_Type = int(Data[0][3:])
        self.Reset_Range_1()
        if Range_Type == 0:
            self.Led_20.setPixmap(self.Make_Led('Led_Rosso.png'))
            self.Set_V_30.setMaximum(15)
        elif Range_Type == 1:
            self.Led_21.setPixmap(self.Make_Led('Led_Rosso.png'))
            self.Set_V_30.setMaximum(35)
        elif Range_Type == 2:
            self.Led_22.setPixmap(self.Make_Led('Led_Rosso.png'))
            self.Set_V_30.setMaximum(35)
            
    def Check_Range_2(self, conn, string):
        self.Write_Data(conn, string)
        Range_Type = int(self.Read_Data(conn)[0][3:])
        self.Reset_Range_2()
        if Range_Type == 0:
            self.Led_23.setPixmap(self.Make_Led('Led_Rosso.png'))
            self.Set_V_31.setMaximum(15)
        elif Range_Type == 1:
            self.Led_24.setPixmap(self.Make_Led('Led_Rosso.png'))
            self.Set_V_30.setMaximum(35)
        elif Range_Type == 2:
            self.Led_25.setPixmap(self.Make_Led('Led_Rosso.png'))
            self.Set_V_30.setMaximum(35)
            
    def Reset_Range_1(self):
        self.Led_20.setPixmap(self.Make_Led('Led_Spento.png'))
        self.Led_21.setPixmap(self.Make_Led('Led_Spento.png'))
        self.Led_22.setPixmap(self.Make_Led('Led_Spento.png'))
        
    def Reset_Range_2(self):
        self.Led_23.setPixmap(self.Make_Led('Led_Spento.png'))
        self.Led_24.setPixmap(self.Make_Led('Led_Spento.png'))
        self.Led_25.setPixmap(self.Make_Led('Led_Spento.png'))
    
    def Check_Voltage_1(self, conn, string):
        self.Write_Data(conn, string)
        V_Set  = self.Read_Data(conn)[0][3:]
        print('Tensione1 ceccata' ,V_Set)
        return V_Set
    
    def Check_Voltage_2(self, conn, string):
        self.Write_Data(conn, string)
        V_Set  = self.Read_Data(conn)[0][3:]
        print('Tensione2 ceccata' ,V_Set)
        return V_Set
    
    def Check_Amp_1(self, conn, string):
        self.Write_Data(conn, string)
        I_Set = self.Read_Data(conn)[0][3:]
        print('Corrente1 ceccata' ,I_Set)
        return I_Set
    
    def Check_Amp_2(self, conn, string):
        self.Write_Data(conn, string)
        I_Set = self.Read_Data(conn)[0][3:]
        print('Corrente2 ceccata' ,I_Set)
        return I_Set
    
    def Check_Exit_1(self, conn ,string):
        #Non risponde dall'alimentatore on OP1 forse bug!
        self.Write_Data(conn, 'string')
        Status_Exit_1 = self.Read_Data(conn)
        print('Cheh_exit 1-->', Status_Exit_1, type(Status_Exit_1))
        
          
    def Set_Range_1(self, string):
        Usb_OK = self.Usb_Connect(timeout=.8)
        self.Write_Data(Usb_OK ,string)
        self.Check_Range_1(Usb_OK, 'RANGE1?\n')
        print('set_range_1_ok')
        Usb_OK.close()
    
    def Set_Range_2(self, string):
        Usb_OK = self.Usb_Connect(timeout=.8)
        self.Write_Data(Usb_OK ,string)
        self.Check_Range_2(Usb_OK, 'RANGE2?\n')
        print('set_range_2_ok')
        Usb_OK.close()
    
    def Set_Voltage_1(self):
        Command_String = 'V1 {Value_String}\n'.format(Value_String = str(self.Set_V_30.value()))
        Usb_OK = self.Usb_Connect(timeout=.8)
        self.Write_Data(Usb_OK ,Command_String)
        self.Display_V_10.setText(self.Check_Voltage_1(Usb_OK, 'V1?\n'))
        print('set_v_1', Command_String)
        Usb_OK.close()
        
    def Set_Voltage_2(self):
        Command_String = 'V2 {Value_String}\n'.format(Value_String = str(self.Set_V_31.value()))
        Usb_OK = self.Usb_Connect(timeout=.8)
        self.Write_Data(Usb_OK ,Command_String)
        self.Display_V_11.setText(self.Init_Interface(Usb_OK, 'V2?\n')[0][3:])
        print('set_v_2', Command_String)
        Usb_OK.close()
    
    def Set_Amp_1(self):
        Command_String = 'I1 {Value_String}\n'.format(Value_String = str(self.Set_I_30.value()))
        Usb_OK = self.Usb_Connect(timeout=.8)
        self.Write_Data(Usb_OK ,Command_String)
        self.Display_I_10.setText(self.Init_Interface(Usb_OK, 'I1?\n')[0][3:])
        print('set_I_1', Command_String)
        Usb_OK.close()
        
    def Set_Amp_2(self):
        Command_String = 'I2 {Value_String}\n'.format(Value_String = str(self.Set_I_31.value()))
        Usb_OK = self.Usb_Connect(timeout=.8)
        self.Write_Data(Usb_OK ,Command_String)
        self.Display_I_11.setText(self.Init_Interface(Usb_OK, 'I2?\n')[0][3:])
        print('set_I_1', Command_String)
        Usb_OK.close()
    
    def Enable_Exit_1(self):
        Usb_OK = self.Usb_Connect(timeout=.8)
        if self.Button_ONOFF_40.isChecked() == True:
            self.Write_Data(Usb_OK, 'OP1 1\n')
            self.Led_40.setPixmap(self.Make_Led('Led_Rosso.png', Dim=60))
            print('Enable_exit_1')
        else:
            self.Write_Data(Usb_OK, 'OP1 0\n')
            self.Led_40.setPixmap(self.Make_Led('Led_Verde.png', Dim=60))
            print('Disable_exit_1')
        Usb_OK.close()
        
    def Enable_Exit_2(self):
        Usb_OK = self.Usb_Connect(timeout=.8)
        if self.Button_ONOFF_41.isChecked() == True:
            self.Write_Data(Usb_OK, 'OP2 1\n')
            self.Led_41.setPixmap(self.Make_Led('Led_Rosso.png', Dim=60))
            print('Enable_exit_2')
        else:
            self.Write_Data(Usb_OK, 'OP2 0\n')
            self.Led_41.setPixmap(self.Make_Led('Led_Verde.png', Dim=60))
            print('Disable_exit_2')
        Usb_OK.close()
        
    def Enable_Exit_All(self):
        Usb_OK = self.Usb_Connect(timeout=.8)
        self.Write_Data(Usb_OK, 'OPALL 1\n')
        self.Led_ON_ALL_50.setPixmap(self.Make_Led('Led_Rosso.png', Dim=60))
        self.Led_OFF_ALL_50.setPixmap(self.Make_Led('Led_Spento.png',Dim=60))
        self.Led_40.setPixmap(self.Make_Led('Led_Rosso.png', Dim=60))
        self.Led_41.setPixmap(self.Make_Led('Led_Rosso.png', Dim=60))
        Usb_OK.close()
        
    def Disable_Exit_All(self):
        Usb_OK = self.Usb_Connect(timeout=.8)
        self.Write_Data(Usb_OK, 'OPALL 0\n')
        self.Led_ON_ALL_50.setPixmap(self.Make_Led('Led_Spento.png',Dim=60))
        self.Led_OFF_ALL_50.setPixmap(self.Make_Led('Led_Verde.png', Dim=60))
        self.Led_40.setPixmap(self.Make_Led('Led_Spento.png', Dim=60))
        self.Led_41.setPixmap(self.Make_Led('Led_Spento.png', Dim=60))
        Usb_OK.close()

    def Info(self): #Crea una finestra per mostare varie informazioni 
        POI.QMessageBox.about(self,'Remote Inteface for TTi','''<p>Remote Control TTi = {0}</p>
        <p>Graphic Interface Ver = {1}'''.format(Remote_TTi_Ver,POI.Ui_TTi_Ver))

if __name__ == '__main__':
    import sys

    app = POI.QApplication(sys.argv)
    form = Remote_TTi()
    form.show()
    app.exec_()
