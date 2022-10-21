class sinif:
    a=0
    b="ads"
    c=[1,3,5]

    def yazdir(self):
        d = 100
        print(d, self.a)

    def yazdir2(self,t):
        self.yazdir()
        print(t)


def palamut():{print("asdasdasd")}

palamut()



nesne=sinif()
nesne.yazdir()
nesne.yazdir2("asdasdas")
print(nesne.a)
nesne.a=999
print(nesne.a)