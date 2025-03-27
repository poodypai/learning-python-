class loopy:
    def input_1(cls):
        nm = int(input("How long should the loop go for? "))
        nm2 = input("What should it print? ")
        return nm, nm2

class Act1(loopy):
    def myfunc(cls, inp, inp1):
        x = inp
        for j in range(x):
            print(inp1)

def main():
    nm, nm2 = loopy.input_1()
    Act1.myfunc(nm, nm2)

 
main()