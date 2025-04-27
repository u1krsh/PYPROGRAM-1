import tkinter as tk
from tkinter import messagebox
import random
import time
root = tk.Tk()
root.geometry("500x500")

tk.Label(text="Enter sentence ")

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Programming is the art of telling a computer what to do.",
    "Practice makes perfect when it comes to typing skills.",
    "Coding is like poetry, it should be concise and beautiful.",
    "A journey of a thousand miles begins with a single step.",
    "Innovation distinguishes between a leader and a follower.",
    "The best way to predict the future is to create it.",
    "Life is what happens when you're busy making other plans.",
    "Knowledge is power, but enthusiasm pulls the switch.",
    "Success is not final, failure is not fatal, it is the courage to continue that counts."
]

inp_sen = ""
str_tim = 0
