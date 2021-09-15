import sqlite3
import datetime
import pandas as pd

con = sqlite3.connect('Banco.db')
cur = con.cursor()

# Create or Connect to DataBase
try:
	cur.execute('''CREATE TABLE Banco(Data TEXT ,Motivo TEXT ,Valor Float ,Total Float)''')
	con.commit()
	print('[+] Data Base Created')
except:
	print('[+] Conection to Data Base Done')

def PrintAllValues():
	print('\n\n')
	print(pd.read_sql_query("SELECT * FROM Banco", con))
	print('\n\n')

def AddValues(Total):
	Motivo = input('[!] Motive?\n	')
	Valor = input('[!] Value? (Outcome = -Value | Income = Value)\n	')
	Total = Total + float(Valor)
	cur.execute('''INSERT INTO Banco VALUES(?,?,?,?)''', [str(datetime.date.today()), Motivo, float(Valor), float(Total)])
	con.commit()
	print("[+] Motive = " + Motivo + "  Value = " + Valor + "  Added!\n")
	
def GetTotal():
	Total = cur.execute('''SELECT MAX(rowid), Total FROM Banco''')
	for i in Total:
		if i[1] != None:
			total = i[1]
		else:
			total = 0
	return float(total)

Con = 1
while Con:
	Total = GetTotal()
	print("[+] Atual Cash - " + str(Total) + "€")
	R = input('[+] All Activity - 1\n[+] Add Income/Outcome - 2\n')
	
	if R == '1':
		PrintAllValues()
	elif R == '2':
		AddValues(Total)
