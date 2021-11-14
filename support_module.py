import requests
import json
import os


def clear_screen():
        if os.name=="nt":
                os.system("cls")
        else:
                os.system("clear")


def l(n):
        for i in range(n): print("")


def standby(): 
    a=input()


def esp(n):
        if n <= 0:
                n = 0
        if type(n) == float:
                n = round(n)
        for i in range(n):
                print(" ", end="")