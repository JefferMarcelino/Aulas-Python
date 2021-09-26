class Televisão:
    def __init__(self, min = 2, max = 14):
        self.ligada = False
        self.canal = 2
        self.cmin = min
        self.cmax = max
    
    def muda_canal_para_baixo(self):
        self.canal = self.cmin
    
    def muda_canal_para_cima(self):
        self.canal = self.cmax


tv1 = Televisão(10, 50)
tv2 = Televisão(11, 29)
