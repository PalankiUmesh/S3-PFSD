class Train:
    ticket = 100
    ac1ticket = 40
    ac2ticket = 50
    ac3ticket = 70

    @staticmethod
    def display():
        print()
        print("Ticket booked")

class Sleeper(Train):
    def book(self):
        if self.ticket != 0:
            Train.display()
            ticket=self.ticket-1
        else:
            print("Tickets are full")

class AC1(Train):
    def book(self):
        if self.ac1ticket !=0:
            Train.display()
            ac1ticket=self.ac1ticket-1
        else:
            print("Tickets are full")

class AC2(Train):
    def book(self):
        if self.ac2ticket != 0:
            Train.display()
            ac2ticket=self.ac2ticket-1
        else:
            print("Tickets are full")

class AC3(Train):
    def book(self):
        if sticket !=0:
            Train.display()
            ac3ticket=self.ac3ticket-1
        else:
            print("Tickets are full")

if __name__ == '__main__':

    name=input("Enter your name:")
    gender=input("Enter your gender")
    phoneno=int(input("Enter your phone number"))
    def info():
        print(name)
        print(gender)
        print(phoneno)
    repeat=True
    print("1.Sleeper,2.AC1,3.AC2,4.AC3")
    ch=int(input("Enter your choice"))
    if ch==1:
        info()
        s=Sleeper()
        s.book()
    elif ch==2:
        info()
        a1=AC1()
        a1.book()
    elif ch==3:
        info()
        a2=AC2()
        a2.book()
    elif ch==4:
        info()
        a3=AC3()
        a3.book()
    else:
        repeat=False




