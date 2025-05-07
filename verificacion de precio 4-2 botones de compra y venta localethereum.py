from bs4 import BeautifulSoup
from urllib.request import urlopen
import tkinter as tk
import requests
import webbrowser
import datetime
from selenium import webdriver

class Localbitcoin:
   
   def __init__(self,pagina):
      self.pagina=pagina
     
   def extraccion(pagina,fila,columna):
      html = requests.get(pagina)
      res = BeautifulSoup(html.text, "lxml")
      precios= res.find_all("td","column-price")[:3]
      precios2=[]
      for a in precios:
         b=a.get_text()
         c=b[38:46]
         precios2.append(c)

      etiqueta1= tk.Label(ventana, text=precios2[0])
      etiqueta1.grid(row=fila,column=columna)

      etiqueta2= tk.Label(ventana, text=precios2[1])
      etiqueta2.grid(row=fila+1,column=columna)

      etiqueta3= tk.Label(ventana, text=precios2[2])
      etiqueta3.grid(row=fila+2,column=columna)

   def ver(self):
      webbrowser.open(self.pagina, new=2, autoraise=True)
   
class Localethereum:
  
   def __init__(self,pagina1,pagina2,pagina3,pagina4,pagina5,pagina6):
      self.pagina1=pagina1
      self.pagina2=pagina2
      self.pagina3=pagina3
      self.pagina4=pagina4
      self.pagina5=pagina5
      self.pagina6=pagina6
      self.navegador= webdriver.Chrome()
      self.programa= self.programa()
 
   def programa(self):
      browser=self.navegador
      browser.minimize_window()
      browser.implicitly_wait(100)
      
      extracion1= self.extraccion(self.pagina1)
      extracion2= self.extraccion(self.pagina2)
      extracion3= self.extraccion(self.pagina3)
      extracion4= self.extraccion(self.pagina4)
      extracion5= self.extraccion(self.pagina5)
      extracion6= self.extraccion(self.pagina6)
      
      self.publicacion(extracion1,10,5)
      self.publicacion(extracion2,18,5)
      self.publicacion(extracion3,22,5)
      self.publicacion(extracion4,10,6)
      self.publicacion(extracion5,18,6)
      self.publicacion(extracion6,22,6)
      
      browser.quit()

   def extraccion(self, pagina):
      try:
         browser=self.navegador
         self.navegador.get(str(pagina))
         nav = self.navegador.find_elements_by_xpath('//*[@id="root"]/div[3]/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div/a/div[2]')[0]
         nav1 = self.navegador.find_elements_by_xpath('//*[@id="root"]/div[3]/div[2]/div/div/div[2]/div/div/div/div[2]/div[1]/div/a/div[2]')[0]
         nav2 = self.navegador.find_elements_by_xpath('//*[@id="root"]/div[3]/div[2]/div/div/div[2]/div/div/div/div[3]/div[1]/div/a/div[2]')[0]

         valor1= nav.text
         valor2= nav1.text
         valor3= nav2.text
         valores=[valor1,valor2,valor3]
         return valores
      except:
         pass
       
   def publicacion(self,lista,fila,columna):
      try:         
         str(lista)
         valor1=lista[0]
         valor2=lista[1]
         valor3=lista[2]
         etiqueta1= tk.Label(ventana, text=valor1)
         etiqueta1.grid(row=fila,column=columna)

         etiqueta2= tk.Label(ventana, text=valor2)
         etiqueta2.grid(row=fila+1,column=columna)

         etiqueta3= tk.Label(ventana, text=valor3)
         etiqueta3.grid(row=fila+2,column=columna)
      except:
         pass

def actualizar():
   localbitcoinSkrillCompra= Localbitcoin.extraccion("https://localbitcoins.com/es/buy-bitcoins-online/usd/moneybookers-skrill/",10,2)
   localbitcoinSkrillVenta= Localbitcoin.extraccion("https://localbitcoins.com/es/sell-bitcoins-online/usd/moneybookers-skrill/",10,3) 
   localbitcoinSkrillCompra= Localbitcoin.extraccion("https://localbitcoins.com/es/buy-bitcoins-online/usd/neteller/",14,2)
   localbitcoinSkrillVenta= Localbitcoin.extraccion("https://localbitcoins.com/es/sell-bitcoins-online/usd/neteller/",14,3)
   localbitcoinSkrillCompra= Localbitcoin.extraccion("https://localbitcoins.com/es/buy-bitcoins-online/usd/payeer/",18,2)
   localbitcoinSkrillVenta= Localbitcoin.extraccion("https://localbitcoins.com/es/sell-bitcoins-online/usd/payeer/",18,3)
   localbitcoinSkrillCompra= Localbitcoin.extraccion("https://localbitcoins.com/es/buy-bitcoins-online/usd/advcash/",22,2)
   localbitcoinSkrillVenta= Localbitcoin.extraccion("https://localbitcoins.com/es/sell-bitcoins-online/usd/advcash/",22,3)
   Localethereum("https://localethereum.com/offers/Skrill/Buy/Sort:Price",
                 "https://localethereum.com/offers/PAYEER/Buy/Sort:Price",
                 "https://localethereum.com/offers/Russia/AdvCash/Buy/Sort:Price",
                 "https://localethereum.com/offers/Skrill/Sell/Sort:Price",
                 "https://localethereum.com/offers/PAYEER/Sell/Sort:Price",
                 "https://localethereum.com/offers/Russia/AdvCash/Sell/Sort:Price")


   fechayhora= datetime.datetime.now()
   ventana.title("Actualizado:"+str(fechayhora))

#_____________________________LOCALBITCOIN_________________________________   
def verCompraSkrill():
   webbrowser.open("https://localbitcoins.com/es/buy-bitcoins-online/usd/moneybookers-skrill/", new=2, autoraise=True)

def verSellSkrill():
   webbrowser.open("https://localbitcoins.com/es/sell-bitcoins-online/usd/moneybookers-skrill/", new=2, autoraise=True)

def verCompraNeteller():
   webbrowser.open("https://localbitcoins.com/es/buy-bitcoins-online/usd/neteller/", new=2, autoraise=True)

def verSellNeteller():
   webbrowser.open("https://localbitcoins.com/es/sell-bitcoins-online/usd/neteller/", new=2, autoraise=True)

def verCompraPayeer():
   webbrowser.open("https://localbitcoins.com/es/buy-bitcoins-online/usd/payeer/", new=2, autoraise=True)

def verSellPayeer():
   webbrowser.open("https://localbitcoins.com/es/sell-bitcoins-online/usd/payeer/", new=2, autoraise=True)

def verCompraAdvcash():
   webbrowser.open("https://localbitcoins.com/es/buy-bitcoins-online/usd/advcash/", new=2, autoraise=True)

def verSellAdvcash():
   webbrowser.open("https://localbitcoins.com/es/sell-bitcoins-online/usd/advcash/", new=2, autoraise=True)

#_____________________________LOCALETHEREUM_________________________________
                
def verCompraSkrillLocalethereum():
   webbrowser.open("https://localethereum.com/offers/Skrill/Buy/Sort:Price", new=2, autoraise=True)

def verSellSkrillLocalethereum():
   webbrowser.open("https://localethereum.com/offers/Skrill/Sell/Sort:Price", new=2, autoraise=True)
"""
def verCompraNetellerLocalethereum():
   webbrowser.open("https://localbitcoins.com/es/buy-bitcoins-online/usd/neteller/", new=2, autoraise=True)

def verSellNetellerLocalethereum():
   webbrowser.open("https://localbitcoins.com/es/sell-bitcoins-online/usd/neteller/", new=2, autoraise=True)
"""
def verCompraPayeerLocalethereum():
   webbrowser.open("https://localethereum.com/offers/PAYEER/Buy/Sort:Price", new=2, autoraise=True)

def verSellPayeerLocalethereum():
   webbrowser.open("https://localethereum.com/offers/PAYEER/Sell/Sort:Price", new=2, autoraise=True)

def verCompraAdvcashLocalethereum():
   webbrowser.open("https://localethereum.com/offers/Russia/AdvCash/Buy/Sort:Price", new=2, autoraise=True)

def verSellAdvcashLocalethereum():
   webbrowser.open("https://localethereum.com/offers/Russia/AdvCash/Sell/Sort:Price", new=2, autoraise=True)

compraLocalbitcoin=Localbitcoin("https://localbitcoins.com/es/buy-bitcoins-online/usd/moneybookers-skrill/")

class creacion:

   def __init__(self,nombre_pagina, pagador, fila, columna):
      self.etiquetaLocalbitcoin= tk.Label(ventana, text=nombre_pagina)
      self.etiquetaLocalbitcoin.grid(row=fila,column=columna)

      self.etiqueta= tk.Label(ventana, text=pagador)
      self.etiqueta.grid(row=fila+1,column=columna)

      self.etiqueta= tk.Label(ventana, text=pagador)
      self.etiqueta.grid(row=fila+2,column=columna)

      self.etiqueta= tk.Label(ventana, text=pagador)
      self.etiqueta.grid(row=fila+3,column=columna)

      


ventana=tk.Tk()

creacionSkrillLocalbitcoin= creacion("Localbitcoin", "Skrill", 9,1)
creacionNetellerLocalbitcoin= creacion("Localbitcoin", "Neteller", 13,1)
creacionPayeerLocalbitcoin= creacion("Localbitcoin", "Payeer", 17,1)
creacionAdvcashLocalbitcoin= creacion("Localbitcoin", "Advcash", 21,1)
creacionSkrillLocalethereum= creacion("LocalEthereum", "Skrill", 9,4)
creacionSkrillLocalethereum= creacion("LocalEethereum", "Neteller", 13,4)
creacionPayeerLocalbitcoin= creacion("LocalEethereum", "Payeer", 17,4)
creacionAdvcashLocalbitcoin= creacion("LocalEethereum", "Advcash", 21,4)

botonActualizar= tk.Button(ventana, command=actualizar, text="Actualizar")
botonActualizar.grid(row=1, column=1)

#_____________________________LOCALBITCOIN_________________________________

BotonCompraSkrill= tk.Button(ventana, text="Compra", command=verCompraSkrill)
BotonCompraSkrill.grid(row=9,column=2)

BotonVentaSkrill= tk.Button(ventana, text="Venta", command=verSellSkrill)
BotonVentaSkrill.grid(row=9,column=3)

BotonCompraNeteller= tk.Button(ventana, text="Compra", command=verCompraNeteller)
BotonCompraNeteller.grid(row=13,column=2)

BotonVentaNeteller= tk.Button(ventana, text="Venta", command=verSellNeteller)
BotonVentaNeteller.grid(row=13,column=3)

BotonCompraPayeer= tk.Button(ventana, text="Compra", command=verCompraPayeer)
BotonCompraPayeer.grid(row=17,column=2)

BotonVentaPayeer= tk.Button(ventana, text="Venta", command=verSellPayeer)
BotonVentaPayeer.grid(row=17,column=3)

BotonCompraAdvcash= tk.Button(ventana, text="Compra", command=verCompraAdvcash)
BotonCompraAdvcash.grid(row=21,column=2)

BotonVentaAdvcash= tk.Button(ventana, text="Venta", command=verSellAdvcash)
BotonVentaAdvcash.grid(row=21,column=3)

#_____________________________LOCALETHEREUM_________________________________


BotonCompraSkrill= tk.Button(ventana, text="Compra", command=verCompraSkrillLocalethereum)
BotonCompraSkrill.grid(row=9,column=5)

BotonVentaSkrill= tk.Button(ventana, text="Venta", command=verSellSkrillLocalethereum)
BotonVentaSkrill.grid(row=9,column=6)


BotonCompraPayeer= tk.Button(ventana, text="Compra", command=verCompraPayeerLocalethereum)
BotonCompraPayeer.grid(row=17,column=5)

BotonVentaPayeer= tk.Button(ventana, text="Venta", command=verSellPayeerLocalethereum)
BotonVentaPayeer.grid(row=17,column=6)

BotonCompraAdvcash= tk.Button(ventana, text="Compra", command=verCompraAdvcashLocalethereum)
BotonCompraAdvcash.grid(row=21,column=5)

BotonVentaAdvcash= tk.Button(ventana, text="Venta", command=verSellAdvcashLocalethereum)
BotonVentaAdvcash.grid(row=21,column=6)

#ok
ventana.mainloop()
