import flet as ft 
from flet import colors as clr
from decimal import Decimal

bottons = [
    {'operator': 'AC', 'fonte':clr.BLACK, 'fundo':clr.BLUE_GREY_100},
    {'operator': '±', 'fonte':clr.BLACK, 'fundo':clr.BLUE_GREY_100},
    {'operator': '%', 'fonte':clr.BLACK, 'fundo':clr.BLUE_GREY_100},
    {'operator': '/', 'fonte':clr.WHITE, 'fundo':clr.ORANGE},
    {'operator': '7', 'fonte':clr.WHITE, 'fundo':clr.WHITE24},
    {'operator': '8', 'fonte':clr.WHITE, 'fundo':clr.WHITE24},
    {'operator': '9', 'fonte':clr.WHITE, 'fundo':clr.WHITE24},
    {'operator': '*', 'fonte':clr.WHITE, 'fundo':clr.ORANGE},
    {'operator': '4', 'fonte':clr.WHITE, 'fundo':clr.WHITE24},
    {'operator': '5', 'fonte':clr.WHITE, 'fundo':clr.WHITE24},
    {'operator': '6', 'fonte':clr.WHITE, 'fundo':clr.WHITE24},
    {'operator': '-', 'fonte':clr.WHITE, 'fundo':clr.ORANGE},
    {'operator': '1', 'fonte':clr.WHITE, 'fundo':clr.WHITE24},
    {'operator': '2', 'fonte':clr.WHITE, 'fundo':clr.WHITE24},
    {'operator': '3', 'fonte':clr.WHITE, 'fundo':clr.WHITE24},
    {'operator': '+', 'fonte':clr.WHITE, 'fundo':clr.ORANGE},
    {'operator': '0', 'fonte':clr.WHITE, 'fundo':clr.WHITE24},
    {'operator': '.', 'fonte':clr.WHITE, 'fundo':clr.WHITE24},
    {'operator': '=', 'fonte':clr.WHITE, 'fundo':clr.ORANGE},
]


#Create a window
def main(page: ft.Page):
    page.bgcolor = '#000' # -> background black 
    page.window_resizable = False
    page.window_width = 300
    page.window_height = 390
    page.title = 'Calculadora'
    page.window_always_on_top = True
    
    result =  ft.Text(value = '0', color= clr.WHITE, size=25)
    
    def calculate(operator, value_at):
        
        try:    
            value = eval(value_at)
            if operator  == '%':
                value /= 100
            elif operator == '±':
                value = -value
        except:        
            return 'Error'
        
        digits = min(abs(Decimal(value).as_tuple().exponent), 5)  
        return format(value, f'.{digits}f') 
        
    
    def select(e):
        value_at = result.value if result.value not in ('0', 'Error') else ''
        value = e.control.content.value
        
        if value.isdigit():
            value = value_at + value 
        elif value == 'AC':
            value = '0'
        else:
            if value_at and value_at[-1] in ('/', '*', '-', '+', '.'):
                value_at = value_at[:-1]
                
            value = value_at + value 
            
            if value[-1] in ('=', '%', '±'):
                value = calculate(operator=value[-1], value_at=value_at)
                
        result.value = value
        result.update()
    
    
        
    #create botton
    btn = [ft.Container(
        content=ft.Text(value=btn['operator'], color=btn['fonte']),
        alignment=ft.alignment.center,
        width=50,
        height=50,
        bgcolor= btn['fundo'],
        border_radius=100,
        on_click= select
    )   for btn in bottons  ]
    
    
    #define calculator number will be on the right side
    display = ft.Row(
        width=250,
        controls=[result], #row elements
        alignment=  'end'
    ) 
    
    
    Keyboard =ft.Row(
        width=250,
        wrap=True,#causes the buttons to have a break and be one below the other
        controls=btn,
        alignment='end'    
    )
        
    
    

    page.add(display)
    page.add(Keyboard)
    
    

ft.app(target = main)
