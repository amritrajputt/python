class ChaiUtils:
    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]

raw = " water ,  milk, ginger, honey"
obj = ChaiUtils()
print(obj.clean_ingredients(raw))

cleaned = ChaiUtils.clean_ingredients(raw)
print(cleaned)


# Without @staticmethod:
# Python object se call karne par self automatically pass karta hai.

# With @staticmethod:
# Python kabhi bhi self pass nahi karta.

# Isliye static method ko class aur object dono se call kar sakte ho, aur wo normal function ki tarah behave karta hai.*/