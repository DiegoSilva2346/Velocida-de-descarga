from speedtest import Speedtest         
import time     
       
import csv    
import pandas as pd
st = Speedtest()         
list_signal=list()            
list_time=list()      
ti=0      
       

        
def genera_lista():      
  tiempo_acumulado=0    
  for i in range(0,600): # El numero 600 de esta linea representa el numero de mediciones , este puede ser  modificado a  gusto del  usuario.        
   if i==0:   
    speed=st.download()   
    print(str(speed)+ "  " + str(i))   
    list_signal.append(speed)         
   

    list_time.append(0)    
           
   else:       
    ti=time.time()     
    speed=st.download()
    list_signal.append(speed)    
    print(str(speed)+ "  " + str(i))   

    list_time.append(time.time()-ti+tiempo_acumulado)    
    tiempo_acumulado=time.time()-ti +tiempo_acumulado      
  return list_signal,list_time               

def guarda_csv():       
  tupla=genera_lista()       
  lista_tiempos=tupla[1]    
  signal=tupla[0]       	

  
  df = pd.DataFrame ({"tiempo":lista_tiempos,"signal":signal})       
  df.to_csv (r'C:/escritorio/Python/BBDD1/export_dataframe_clear_600new2.csv', index = False, header=True)  

if __name__ == '__main__':
   	guarda_csv()
