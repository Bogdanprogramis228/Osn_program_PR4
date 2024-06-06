class Error:
    def message_handler(self):
        return "Error"

class Success:
    def message_handler(self):
        return "Success"

# Класи, що наслідують Error
class NG(Error):
    pass

class NI(Error):
    pass

class NN(Error):
    pass

class NE(Error):
    pass

class I:
    pass

class G(NI, I):
    pass

class E(G):
    pass

class B(NE, E):
    pass

class L(Success):
    pass

class N(Success):
    pass

class I(NN, L, N):
    pass

class H(I):
    pass

class R(I):
    pass

class W(R, H):
    pass

class Begin(B):
    pass

# Створення об'єктів початкового стану та стану B
begin = Begin()
b = B()

# Вивід результатів виклику обробників повідомлень
print("Begin state handler:", begin.message_handler())
print("B state handler:", b.message_handler())

# Перевірка обробників для кінцевих станів
ng = NG()
ni = NI()
g = G()
e = E()
ne = NE()
w = W()
r = R()
h = H()
i = I()
l = L()
n = N()
success = Success()
error = Error()

print("NG state handler:", ng.message_handler())
print("NI state handler:", ni.message_handler())
print("G state handler:", g.message_handler())
print("E state handler:", e.message_handler())
print("NE state handler:", ne.message_handler())
print("W state handler:", w.message_handler())
print("R state handler:", r.message_handler())
print("H state handler:", h.message_handler())
print("L state handler:", l.message_handler())
print("N state handler:", n.message_handler())
print("Success state handler:", success.message_handler())
print("Error state handler:", error.message_handler())