from time import *

def get(truc):
  if truc == "temperature":
    temperature = #il faut definir
  if truc == "luminositee":
    luminositee = #il faut definir
def on_IF():
  #il faut definir
def off_IF():
  #il faut definir
def close_door():
  #il faut definir
def open_door():
  #il faut definir

while True:
  get(temperature)
  if temperature < 10:
    on_IF()
    close_door()
  elif temperature > 20:
    off_IF()
    open_door()
  get(luminositee)
