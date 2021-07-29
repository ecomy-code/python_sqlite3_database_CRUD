import sqlite3 as db
import os
from datetime import date
from datetime import datetime


class Database_ecom():

	def fecha(self):
		now = date.today()
		an = now.year
		ms = now.month
		di = now.day
		fecha = "{} del {} de {}".format(di,ms,an)
		return fecha
	
	def id_database(self):
		gen = Generator()
		id = gen.new_id()
		return str(id)

	def start(self):
		try:

			if os.path.isdir('database') == False:
				os.mkdir('database')
				dba = db.connect("database/home.db")
				mycur = dba.cursor()

				q1 = """CREATE TABLE if not exists gastos(ID varchar(89),FECHA varchar (22),DETALLE varchar (255),MONTO varchar (28))"""
					
				q2 = """CREATE TABLE if not exists ingresos(ID varchar(89), FECHA varchar (22), DETALLE varchar (255), MONTO varchar (28))"""
					
				q3 = """CREATE TABLE if not exists balances(ID varchar(89), FECHA varchar (22), GASTO varchar (255), INGRESO varchar (255), BALANCE varchar (255))"""
					
				q4 = """CREATE TABLE if not exists user(ID integer, USER varchar(28), PAS varchar(28))"""
				
				
				
				querys = [q1,q2,q3, q4]
				for i in querys:
					mycur.execute(i)
					dba.commit()
				dba.close()
				self.add_user()
				
			else:
				pass

		except:
			pass

    
#INSERT
	def add_user(self):
		dba = db.connect("database/home.db")
		mycur = dba.cursor()
		q5 = "INSERT INTO user VALUES (?,?,?)"
		datos = ('1','economy','root')
		mycur.execute(q5,datos)
		dba.commit()
		dba.close()

	def add_factura(self, tabla, detalle, monto):

		datos = (self.id_database(),self.fecha(),str(detalle),str(monto))
		query = "INSERT INTO {} VALUES(?,?,?,?)".format(tabla)
		try:
			dba = db.connect("database/home.db")
			mycur = dba.cursor()
			mycur.execute(query,datos)
			dba.commit()
			dba.close()
			return True
		except Exception as e:
			print(e)
			return False

    
#UPDATE
	def update_factura(self,tabla, id, detalle, monto):
		query = """UPDATE {} SET DETALLE = ?, MONTO = ? WHERE ID = {}""".format(tabla, id)

		datos = (str(detalle), str(monto))

		try:
			dba = db.connect("database/home.db")
			mycur = dba.cursor()

			mycur.execute(query,datos)
			dba.commit()
			dba.close()

		except Exception as e:
			print(e)

      
#DELETE
	def delete_factura(self,tabla,id):
		query = "DELETE FROM {} where ID = {}".format(tabla,id)

		try:
			dba = db.connect("database/home.db")
			mycur = dba.cursor()

			mycur.execute(query)
			dba.commit()
			dba.close()
			return True
			
		except:
			return False


#DELETE   AND   CREATE
	def reiniciar_tabla(self,tabla):
		tabla = str(tabla)
		query = " DROP TABLE {}".format(tabla)

		try:
			dba = db.connect("database/home.db")
			mycur = dba.cursor()

			mycur.execute(query)
			dba.commit()
			dba.close()
			self.create(tabla)
			return True

		except:
			return False

	def create(self, tabla):
		
		q1 = """CREATE TABLE if not exists gastos(
			ID varchar(89),
			FECHA varchar (22), 
			DETALLE varchar (255), 
			MONTO varchar (28))"""
				
		q2 = """CREATE TABLE if not exists ingresos(ID varchar(89), FECHA varchar (22), DETALLE varchar (255), MONTO varchar (28))"""
				
		q3 = """CREATE TABLE if not exists balances(ID varchar(89), FECHAI varchar (22),FECHAF varchar (22), GASTOS_TOTAL varchar (255), INGRESOS_TOTAL varchar (255), BALANCE varchar (255))"""
		
		if tabla == "gastos":
			query = q1
			try:
				dba = db.connect("database/home.db")
				mycur = dba.cursor()
				
				mycur.execute(query)
				dba.commit()
				dba.close()
			except:
				pass


		elif tabla == "ingresos":
			query = q2
			try:
				dba = db.connect("database/home.db")
				mycur = dba.cursor()
				
				mycur.execute(query)
				dba.commit()
				dba.close()
			except:
				pass
				
				
		elif tabla == "balances":
			query = q3
			
			try:
				dba = db.connect("database/home.db")
				mycur = dba.cursor()
				
				mycur.execute(query)
				dba.commit()
				dba.close()
				pass
			except:
				pass
				
		else:
			pass

	def update_factura(self,tabla, id, detalle, monto):
		query = """UPDATE {} SET DETALLE = ?, MONTO = ? WHERE ID = {}""".format(tabla, id)

		datos = (str(detalle), str(monto))

		try:
			dba = db.connect("database/home.db")
			mycur = dba.cursor()

			mycur.execute(query,datos)
			dba.commit()
			dba.close()

		except Exception as e:
			print(e)

	def select_tabla(self,tabla):
		query ="SELECT * FROM {}".format(tabla)
		dba = db.connect("database/home.db")
		mycur = dba.cursor()
		mycur.execute(query)
		datos = mycur.fetchall()
		
		return datos


class User():
	
	def conector_db(self, user, pas):
		try:
			dba = db.connect("database/home.db")
			mycur = dba.cursor()
			
			query = "SELECT * FROM user WHERE ID = {}".format(1)
			
			mycur.execute(query)
			cur = mycur.fetchone()
			
			if user == cur[1] and pas == cur[2]:
				return True
			else:
				return False
				
		except:
			pass


	def update(self,us,pas):
		try:
			dba = db.connect("database/home.db")
			mycur = dba.cursor()
			
			query = 'UPDATE user SET USER = ?, PAS = ? WHERE ID = {}'.format(1)
			datos = (us,pas)
			mycur.execute(query, datos)
			dba.commit()
			dba.close()
			return True
			
		except Exception as e:
			print(e)
			return False
    
	def update_user(self, pasValido, user, pasNew):
		try:
			dba = db.connect("database/home.db")
			mycur = dba.cursor()
			
			query = "SELECT * FROM user WHERE ID = {}".format(1)
			
			mycur.execute(query)
			cur = mycur.fetchone()
			
			if pasValido == cur[2]:
				us = user
				pas = pasNew
				var = self.update(us,pas)
				return var
				
			else:
				return False
				
			dba.close()
				
		except Exception as e:
			print(e)
	


class Generator():
	
	def activa(self):
		
		if os.path.isfile ("database/id.txt") == False:
			txt = open("database/id.txt", "w")
			txt.write("10")
			txt.close()
			return '10'
			
		else:
			txt = open ("database/id.txt", "r")
			ids = txt.read()
			txt.close()
			return str(ids)
			

	def new_id(self):
		ids = self.activa()
		
		ids = int(ids)+1
		
		txt = open ("database/id.txt", 'w')
		num = "{}".format(ids)
		txt.write(num)
		txt.close()
		
		return str(ids)

