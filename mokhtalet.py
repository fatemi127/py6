class mokhtalet :

    def __init__(self, haghighi=None, mohoomi=None):
        self.r = haghighi
        self.i = mohoomi
        


    def sub(self, other):
        result=mokhtalet()
        result.r= self.r - other.r
        result.i= self.i - other.i
        return result


    def sum(self, other):
        result=mokhtalet()
        result.r= self.r + other.r
        result.i= self.i + other.i
        return result



    def mul(self, other):
        result=mokhtalet()
        result.r= self.r * other.r - self.i * other.i
        result.i= self.r * other.i - self.i * other.r
        return result


    def show(self):
        return str(self.r )+'+('+str(self.i) +')i'

haghighi1=int(input('Haghighi num1: '))
mohoomi1=int(input('Mohoomi num1: '))


haghighi2=int(input('Haghighi num2: '))
mohoomi2=int(input('Mohoomi num2:'))

C1 = mokhtalet(haghighi1,mohoomi1)
C2 = mokhtalet(haghighi2,mohoomi2)
print('+  is',(C1.sum(C2)).show())
print('- is',(C1.sub(C2)).show())
print('* is',(C1.mul(C2)).show())