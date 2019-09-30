from bs4 import BeautifulSoup
from urllib.request import urlopen
import tkinter as tk
import requests
import webbrowser

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
      



def actualizar():
   localbitcoinSkrillCompra= Localbitcoin.extraccion("https://localbitcoins.com/es/buy-bitcoins-online/usd/moneybookers-skrill/",10,2)
   localbitcoinSkrillVenta= Localbitcoin.extraccion("https://localbitcoins.com/es/sell-bitcoins-online/usd/moneybookers-skrill/",10,3) 
   localbitcoinSkrillCompra= Localbitcoin.extraccion("https://localbitcoins.com/es/buy-bitcoins-online/usd/neteller/",14,2)
   localbitcoinSkrillVenta= Localbitcoin.extraccion("https://localbitcoins.com/es/sell-bitcoins-online/usd/neteller/",14,3)
   localbitcoinSkrillCompra= Localbitcoin.extraccion("https://localbitcoins.com/es/buy-bitcoins-online/usd/payeer/",18,2)
   localbitcoinSkrillVenta= Localbitcoin.extraccion("https://localbitcoins.com/es/sell-bitcoins-online/usd/payeer/",18,3)
   
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
creacionSkrillLocalethereum= creacion("LocalEthereum", "Skrill", 9,4)
creacionSkrillLocalethereum= creacion("LocalEethereum", "Neteller", 13,4)
creacionPayeerLocalbitcoin= creacion("LocalEethereum", "Payeer", 17,4)

botonActualizar= tk.Button(ventana, command=actualizar, text="Actualizar")
botonActualizar.grid(row=1, column=1)

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



ventana.mainloop()
