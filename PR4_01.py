class Error:
    def message_handler(self):
        return "Error"

class Success:
    def message_handler(self):
        return "Success"

class G(Error):
    pass

class E(G):
    pass

class NE(E):
    pass

class B(E):
    pass

class I:
    pass

class H(I):
    pass

class W(H):
    pass

class R(I):
    pass

class Begin(B):
    pass

begin = Begin()
b = B()

print(begin.message_handler()) 
print(b.message_handler())