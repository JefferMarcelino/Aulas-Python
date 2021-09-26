class Televisão:
    def __init__(self):
        self.ligada = False
        self.canal = 2
    
    def muda_canal_para_baixo(self):
        self.canal -=1
    
    def muda_canal_para_cima(self):
        self.canal +=1


tv = Televisão()
tv.muda_canal_para_cima()
tv.muda_canal_para_cima()
print(tv.canal)

tv.muda_canal_para_baixo()
print(tv.canal)
