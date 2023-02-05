
import tkinter as tk
import random as rd

coins = 5
nrl,nr2,nr3,nr4,nr5,nr6,nr7 = 0,0,0,0,0,0,0
pool = []
pool2 = []

def zreb():
   samplel = [i for i in range(1, 51)] 
   sample2 = [i for i in range(1, 13)] 
   selected = [0, 0, 0, 0, 0, 0, 0]

   for j in range(0, 5):
      x = rd.choice(samplel)
      selected[j] = x 
      samplel.remove(x) 
   for k in range(5, 7):
      y = rd.choice(sample2)
      selected[k] = y 
      sample2.remove(y) 
   return selected

selected = zreb() 

#winning combinations
v1 = "5+2"
v2 = "5+1"
v3 = "5+0"
v4 = "4+2"
v5 = "4+1"
v6 = "4+0"
v7 = "3+2"
v8 = "2+2"
v9 = "3+1"
v10 = "3+0" 
v11 = "1+2" 
v12 = "2+1"

#payout
d1 = 30000000.00
d2 = 2938894.20
d3 = 66249.60
d4 = 1671.60
d5 = 165.9
d6 = 85.9
d7 = 24.9
d8 = 12.7
d9 = 12.7
d10 = 12.7 
d11 = 6.6 
d12 = 6.6

dobitki = {}

for i in range(1, 13):
   dobitki[eval("v" + str(i))] = eval("d" + str(i))

def wins(selected, pool, pool2): 
   prvi = 0
   drugi = 0

   for i in pool:
      if i in selected[0:5]: 
         prvi += 1

   for j in pool2:
      if j in selected[5:]:
         drugi += 1
   return(str(prvi)+"+"+str(drugi))

znesek = None
################################################################################ 
class intro:
   def __init__(self, master):
      self.master = master
      self.master.geometry("600x600")
      self.top_frame = tk.Frame(master, bg='gray10', width=450, height=50, pady=3)
      self.center = tk.Frame(master, bg= 'gray40', width=450, height=40, padx=3, pady=3)
      self.btm_frame = tk.Frame(master, bg='gray70', width=450, height=45, pady=3)
      self.btm_frame2 = tk.Frame(master, bg='gray99', width=450, height=60, pady=3)
      self.master.grid_rowconfigure(1, weight=1) 
      self.master.grid_columnconfigure(0, weight=1)

      self.top_frame.grid(row=0, sticky="ew") 
      self.center.grid(row=1, sticky="nsew") 
      self.btm_frame.grid(row=3, sticky="ew") 
      self.btm_frame2.grid(row=4, sticky="ew")
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      self.pozdrav = tk.Label(self.top_frame,text="WELCOME!",bg="gray10",fg="white",font =("System",18))
      self.pozdrav.pack()

      # # # # # # # # # # # # # 4 4 # 4 # # # # # # # # # # # # # 
      coin_path = "./images/coin.gif"
      self.slika = tk.PhotoImage(file=coin_path)
      self.okvirzasliko =tk.Label(self.center, image=self.slika, bg="gray40") 
      self.okvirzasliko.config(anchor="center") 
      self.okvirzasliko.pack(expand = True)
      
      self.frame_count = 9
      self.frames = [tk.PhotoImage(file=coin_path, format = "gif -index %i" %(i)) for i in range(self.frame_count)]
      self.master.after(0,self.updategif,0)
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      self.coins_var = "Coins remaining: "+str(coins) 
      self.coins_remaining = tk.Label(self.center,text=self.coins_var,bg="gray40",fg="black",font=("System", 16))
      self.coins_remaining.config(anchor="s")
      self.coins_remaining.pack(expand=True)
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      self.insert_coin =tk.Button(self.btm_frame,text="INSERT x1 COIN",font=("System",16), command=lambda:[self.new_window(),self.use_coin()]) 
      self.insert_coin.config(anchor="center") 
      self.insert_coin.pack(expand=True)
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      self.quit = tk.Button(self.btm_frame2,text="QUIT",font=("system",16),command=self.close_window)
      self.quit.config(anchor="center")
      self.quit.pack(expand=True)

   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
   def use_coin(self): 
      global coins
      coins -= 1
   
   def updategif(self,gif):
      frame = self.frames[gif]
      gif += 1
      if gif == self.frame_count:
         gif = 0
      self.okvirzasliko.config(image=frame) 
      self.master.after(50,self.updategif,gif)

   def new_window(self):
      global coins
      coins -= 1
      self.master.destroy() # close the current window 
      self.master = tk.Tk() # create another Tk instance 
      self.app = insert(self.master) # create Demo2 window 
      self.master.mainloop()

   def close_window(self):
      self. master. destroy()
################################################################################
class insert:
   def __init__(self, master):
      self.master = master
      self. master. geometry("600x600") 
      self.title = master.title("")

      self.top_frame = tk.Frame(master, bg='gray10', width=450, height=50, pady=3)
      self.center = tk.Frame(master, bg='gray40', width=450, height=40, padx=3, pady=3)
      self.btm_frame = tk.Frame(master, bg='gray70', width=450, height=45, pady=3)
      self.master.grid_rowconfigure(1, weight=1) 
      self.master.grid_columnconfigure(0, weight=1)

      self.top_frame.grid(row=0, sticky ="ew") 
      self.center.grid(row=1, sticky="nsew") 
      self.btm_frame.grid(row=3, sticky="ew")

      self.navodilo = tk.Label(self.top_frame,text="Enter 1 to 50 in each white field and 1 to 12 in each red field!",bg="gray10", fg="white",font=("system",16)) 
      self.navodilo.config(anchor="center")
      self.navodilo.pack(expand=True)
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
      self.center.grid_columnconfigure(0,weight=1) 
      self.center.grid_columnconfigure(1, weight=2) 
      self.center.grid_rowconfigure((0,1,2,3,4,5,6),weight=1)

      self.pll =tk.Label(self.center,text="#1", width=5) 
      self.pll.grid(row=0,column=0,sticky="ew")
      self.pl =tk.Entry(self.center)
      self.pl.grid(row=0,column=1,sticky="ew")

      self.p21 = tk.Label(self.center,text="#2", width=5) 
      self.p21.grid(row=1, column=0,sticky="ew")
      self.p2 = tk.Entry(self.center)
      self.p2.grid(row=1, column=1, sticky="ew")

      self.p31 = tk.Label(self.center, text="#3", width=5) 
      self.p31.grid(row=2, column=0,sticky="ew")
      self.p3 = tk.Entry(self.center)
      self.p3.grid(row=2, column=1,sticky="ew")

      self.p41 = tk.Label(self.center, text="#4", width=5) 
      self.p41.grid(row=3, column=0,sticky="ew")
      self.p4 = tk.Entry(self.center)
      self.p4.grid(row=3, column=1,sticky="ew")

      self.p51 = tk.Label(self.center, text="#5", width=5) 
      self.p51.grid(row=4, column=0,sticky="ew")
      self.p5 = tk.Entry(self.center)
      self.p5.grid(row=4, column=1,sticky="ew")

      self.p61 = tk.Label(self.center, text="#6", width=5) 
      self.p61.grid(row=5, column=0,sticky="ew")

      self.p6 = tk.Entry(self.center, bg="red") 
      self.p6.grid(row=5, column=1,sticky="ew")

      self.p71 = tk.Label(self.center, text="#7", width=5) 
      self.p71.grid(row=6, column=0,sticky="ew")
      self.p7 = tk.Entry(self.center, bg="red") 
      self.p7.grid(row=6, column=1,sticky="ew")

      self.shrani = tk.Button(self.btm_frame,text="CONFIRM NUMBERS", font=("System",16),command=self.gettext)
      self.shrani.pack()

      self.zreb = tk.Button(self.btm_frame,text="START", font=("System",16),command=self.new_window,state="disabled") 
      self.zreb.pack()

      self.quit = tk.Button(self.btm_frame,text ="QUIT",font=("System",16),command=self.close_window)
      self.quit.config(anchor="center")
      self.quit.pack(expand=True)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
   def gettext(self):
      global nrl,nr2,nr3,nr4,nr5,nr6,nr7
      global pool
      global pool2
      nrl = int(self.pl.get())
      nr2 = int(self.p2.get())
      nr3 = int(self.p3.get())
      nr4 = int(self.p4.get())
      nr5 = int(self.p5.get())
      nr6 = int(self.p6.get())
      nr7 = int(self.p7.get())

      pool = [nrl, nr2, nr3, nr4, nr5]
      pool2 = [nr6, nr7]
      if all(i <= 50 for i in pool) and len(pool) == len(set(pool)) and all(j<= 12 for j in pool2) and len(pool2) == len(set(pool2)):
         self.navodilo.config(text= "PRESS START TO START THE LOTTERY!") 
         self.shrani.config(state="disabled")
         self.zreb.config(state="normal")
      else:
         self.navodilo.config(text="WRONG ENTRY! TRY AGAIN!")

   def new_window(self):
      self.master.destroy() 
      self.master = tk.Tk() 
      self .app = loading(self.master)
      self.master.mainloop()

   def close_window(self): 
      self.master.destroy()

###############################################################################

class loading:
   def  __init__(self, master):
      self.master = master
      self.master.geometry("600x600")
      self .title = master.title("LOTTERY IN PROGRESS...")

      self.top_frame = tk.Frame(master, bg='gray10', width=450, height=50,pady=3)
      self.center = tk.Frame(master, bg='gray40', width=450, height=40,padx=3, pady=3)
      self.btm_frame = tk.Frame(master, bg='gray70', width=450, height=45,pady=3)
      self.master.grid_rowconfigure(1, weight=1) 
      self.master.grid_columnconfigure(0, weight=1)

      self.top_frame.grid(row=0, sticky="ew") 
      self.center.grid(row=1, sticky="nsew") 
      self.btm_frame.grid(row=3, sticky="ew")

      self.navodilo = tk.Label(self.top_frame,bg="gray10",fg="white",font=("system",16)) 
      self.navodilo.config(anchor="center")
      self.navodilo.pack(expand=True)
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      lotto_path = "./images/lotto.gif"
      self.slika = tk.PhotoImage(file=lotto_path) 
      self.okvirzasliko =tk.Label(self.center,image=self.slika,bg="gray40") 
      self.okvirzasliko.config(anchor="center") 
      self.okvirzasliko.pack(expand=True)

      self.frame_count = 3
      self.frames = [tk.PhotoImage(file=lotto_path, format = "gif -index %i" %(i)) for i in range(self.frame_count)]
      self.master.after(0,self.updategif,0)

      #self.zreb = tk.Button(self.btm_frame,text="RESULTS",font=("system",16),command=self.new_window)
      #self.zreb.pack()

      self.quit=tk.Button(self.btm_frame,text="QUIT",font=("system",16),command=self.close_window)
      self.quit.config(anchor="center") 
      self.quit.pack(expand=True)

      self.master.after(2000,self.new_window)

   def updategif(self,gif):
      frame = self.frames[gif]
      gif += 1
      if gif == self.frame_count:
         gif = 0
      self.okvirzasliko.config(image=frame) 
      self.master.after(100,self.updategif,gif)

   def new_window(self):
       self.master.destroy() # close the current window
       self.master = tk.Tk() # create another Tk instance
       self.app = result(self.master) # create Demo2 window 
       self.master.mainloop()

   def close_window(self): 
       self.master.destroy()

################################################################################
class result:
   def __init__(self, master):
      self.master = master
      self. master. geometry("600x600") 
      self.title = master.title("RESULTS")

      self.top_frame = tk.Frame(master, bg='gray10', width=450, height=50, pady=3)
      self.center = tk.Frame(master, bg='gray40', width=450, height=40, padx=3, pady=3)
      self.btm_frame = tk.Frame(master, bg='gray70', width=450, height=45, pady=3)
      self.master.grid_rowconfigure(1, weight=1) 
      self.master.grid_columnconfigure(0, weight=1)

      self.top_frame.grid(row=0, sticky="ew")

      self.numbersl = tk.Label(self.top_frame,text="The winning numbers are:",bg="gray10",fg="white",font=("system",18))
      self.numbersl.pack()

      self.center.grid_rowconfigure((0,1,2,3), weight=1) 
      self.center.grid_columnconfigure((0,1,2,3,4,5,6,7),weight=1) 
      self.center.grid(row=1, sticky="nsew")

      self.numbers2 = tk.Label(self.center, text="Your numbers are:", fg="white",bg="gray40", font=("System", 18)) 
      self.numbers2.grid(row=1,columnspan=8, sticky="ew")

      self.btm_frame.grid(row=3, sticky="ew")

      col = 0
      for i in selected[0:5]:
         x= tk.Button(self.center,text=i,width=10,height=2,font=("system",16))
         col += 1
         x.grid(row=0, column=col, sticky = "n") ######
      for j in selected[5:7]:
         x = tk.Button(self.center,bg="red", text=j,width=10,height=2,font=("system", 16)) 
         col +=1 
         x.grid(row=0, column=col, sticky = "n") ######
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      col = 0
      for i in pool:
         x= tk.Button(self.center, text=i, width=10, height=2,font=("system", 16)) 
         col += 1 
         x.grid(row=2, column=col, sticky="n") ######
      for j in pool2:
         x= tk.Button(self.center, bg="green", text=j, width=10, height=2,font=("system", 16)) 
         col += 1 
         x.grid(row=2, column=col, sticky="n") ######

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
      self.zreb = tk.Button(self.btm_frame,text="TRY AGAIN",font=("System",16),command=self.new_window)
      self.zreb.pack()

      self.quit =tk.Button(self.btm_frame,text="QUIT",font=("system",16),command=self.close_window)
      self.quit.config(anchor="center")
      self.quit.pack(expand=True)

      global znesek
      znesek = wins(selected, pool, pool2)
      if znesek not in dobitki: 
         znesek = 0
      else:
         znesek = dobitki[wins(selected,pool,pool2)]
      if znesek > 0:
         self.znesek = tk.Label(self.center, text="You have won: "+str(znesek)+" EUR!!!", fg="white", bg="gray40",
                        font=("system", 18))
      else:
         self.znesek = tk.Label(self.center, text="Sorry, your ticket was not a winner...", fg="white", bg="gray40",
                        font=("system", 18))
      self.znesek.grid(row=3, columnspan=8, sticky="ew")
     # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

   def new_window(self):
     self.master.destroy() # close the current window 
     self.master = tk.Tk() # create another Tk instance 
     self.app = intro(self.master) # create Demo2 window 
     self.master.mainloop()

   def close_window(self): 
     self.master.destroy()

################################################################################ 
def main():
   root = tk.Tk()
   root.title("Intro")
   root.geometry("600x600")
   app = intro(root)
   root.mainloop()

if __name__ == "__main__":
   main()
################################################################################ 