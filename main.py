def yigindini_top(n):
    yigindi = 0
    i = 1
    while i <= n:
        yigindi += i
        i += 1
    return yigindi

natija = yigindini_top(10)
print("1 dan 10 gacha sonlar yig'indisi:", natija)

def raqamlar_yigindisi(son):
    yigindi = 0
    while son > 0:
        oxirgi_raqam = son % 10
        yigindi += oxirgi_raqam
        son //= 10
    return yigindi

print("458 sonining raqamlari yig'indisi:", raqamlar_yigindisi(458))

def parol_tekshir(togri_parol):
    urinishlar = 0
    maksimal_urinish = 3

    while urinishlar < maksimal_urinish:
        kiritilgan = input("Parolni kiriting: ")
        if kiritilgan == togri_parol:
            return "Xush kelibsiz! Tizimga kirdingiz."
        else:
            urinishlar += 1
            qolgan = maksimal_urinish - urinishlar
            print(f"Xato parol! Qolgan urinishlar: {qolgan}")

    return "Urinishlar tugadi. Tizim bloklandi!"

print(parol_tekshir("python123"))
