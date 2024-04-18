def pause():
    print("\nНажмите Enter для продолжения...")
    input()  # Останавливаем консоль и ждем ввода от пользователя\

def print_formula(formula):
    print("")
    print(formula)
    pause()

def division_formula():
    formula = """
    Формула F(x) = x⁴ - x - 1
    """
    print_formula(formula)

def tanden_formula_a():
    formula = """
    Формула A F(x) = x³ + 0.2x² + 0.5x - 2
    
    Формула A F'(x) = 3x² + 0.4x + 0.5

    Формула A F''(x) = 6x + 4
    """
    print_formula(formula)

def tanden_formula_b():
    formula = """
    Формула B F(x) = tg(0.5x + 0.1) - x²
    
                              1 
    Формула B F'(x) = ━━━━━━━━━━━━━━━━ - 2x
                      cos²(0.5x + 0.1)
    
    Формула B F''(x) = 2·sin(0.5x + 0.1)·cos(0.5x + 0.1)
    """
    print_formula(formula)

def simpson_f(form):
    if form == 1:
        formula_1 = """
                1) eᵃˣ  ·  sin(bx)

                """

        formula = """
        Производная 4-го порядка:

        (a⁴·sin(bx) + 4·a³·b·cos(bx) - 6·a²·b³·sin(bx) + b⁴·sin(bx))·eᵃˣ

        """
        print(formula_1)
        print(formula)
    elif form == 2:

        formula_2 = """  
                       1
                2) ━━━━━━━━━
                   √(x + a²)

                """

        formula = """
        Производная 4-го порядка:
                                  
          105·x⁴     90·x²
        ━━━━━━━━━ - ━━━━━━ + 9
        (a + x²)²   a + x²
        ━━━━━━━━━━━━━━━━━━━━━━
              (a + x²)²
        
        """
        print(formula_2)
        print(formula)
    elif form == 0:
        formula_1 = """
        1) eᵃˣ · sin(bx)
        
        """
        formula_2 = """  
                       1
                2) ━━━━━━━━━
                   √(x² + a)

                """
        print(formula_1)
        print(formula_2)

def Runge_Kutta_f(form):
    if form == 1:
        formula_1 = """
        y' = (1 + x²) · (1 + y)
        
        """
        formula_2 = """
             x + (x³ / 3)
        y = e             - 1
        
        """
        print(formula_1)
        print(formula_2)
    elif form == 2:
        formula_1 = """
        1) y'' - ay' - by = sin(x)

        2) y'' - ay' - by = e⁻ˣ
        
        3) y'' - ay' - by = cos(x)
        
        """
        formula_2 = """
        y' = u
        y'' = u' = au + by + f(x)
        
        """
        print(formula_1)
        print(formula_2)
