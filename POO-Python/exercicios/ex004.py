class Televisão:
    def __init__(self, min, max):
        self.ligada = False
        self.canal = 2
        self.cmin = min
        self.cmax = max
    
    def muda_canal_para_baixo(self):
        self.canal = self.cmin
    
    def muda_canal_para_cima(self):
        self.canal = self.cmax


tv = Televisão(2, 10)
tv.muda_canal_para_cima()
print(tv.canal)
tv.muda_canal_para_baixo()
print(tv.canal)
