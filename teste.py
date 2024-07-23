import flet as ft 
from flet import colors as clr

bottons = [
    {'operator': 'AC', 'fonte': clr.BLACK, 'fundo': clr.BLUE_GREY_100},
    {'operator': '+/-', 'fonte': clr.BLACK, 'fundo': clr.BLUE_GREY_100},
    {'operator': '%', 'fonte': clr.BLACK, 'fundo': clr.BLUE_GREY_100},
    {'operator': '÷', 'fonte': clr.WHITE, 'fundo': clr.ORANGE},
    {'operator': '7', 'fonte': clr.WHITE, 'fundo': clr.WHITE24},
    {'operator': '8', 'fonte': clr.WHITE, 'fundo': clr.WHITE24},
    {'operator': '9', 'fonte': clr.WHITE, 'fundo': clr.WHITE24},
    {'operator': 'X', 'fonte': clr.WHITE, 'fundo': clr.ORANGE},
    {'operator': '4', 'fonte': clr.WHITE, 'fundo': clr.WHITE24},
    {'operator': '5', 'fonte': clr.WHITE, 'fundo': clr.WHITE24},
    {'operator': '6', 'fonte': clr.WHITE, 'fundo': clr.WHITE24},
    {'operator': '-', 'fonte': clr.WHITE, 'fundo': clr.ORANGE},
    {'operator': '1', 'fonte': clr.WHITE, 'fundo': clr.WHITE24},
    {'operator': '2', 'fonte': clr.WHITE, 'fundo': clr.WHITE24},
    {'operator': '3', 'fonte': clr.WHITE, 'fundo': clr.WHITE24},
    {'operator': '+', 'fonte': clr.WHITE, 'fundo': clr.ORANGE},
    {'operator': '0', 'fonte': clr.WHITE, 'fundo': clr.WHITE24},
    {'operator': ',', 'fonte': clr.WHITE, 'fundo': clr.WHITE24},
    {'operator': '=', 'fonte': clr.WHITE, 'fundo': clr.ORANGE},
]

def main(page: ft.Page):
    page.bgcolor = '#000'
    page.window_resizable = False
    page.window_width = 300
    page.window_height = 390
    page.title = 'Calculadora'
    page.window_always_on_top = True
    
    result = ft.Text(value='0', color=clr.WHITE, size=25)
    
    display = ft.Row(
        width=250,
        controls=[result],
        alignment='end'
    )
    
    def calculate(expression):
        try:
            expression = expression.replace('X', '*').replace('÷', '/').replace(',', '.')
            value = eval(expression)
        except:
            return 'Error'
        
        return str(value)
    
    def select(e):
        value_at = '' if result.value in ('0', 'Error') else result.value
        value = e.control.content.value 
        
        if value.isdigit() or value == '.':
            value = value_at + value
        elif value == 'AC':
            value = '0'
        elif value in ('+', '-', '*', '/', 'X', '÷'):
            if value_at and value_at[-1] in ('/', '*', '-', '+', 'X', '÷'):
                value_at = value_at[:-1]
            value = value_at + value
        elif value == '+/-':
            if value_at:
                value = str(-float(value_at))
        elif value == '%':
            if value_at:
                value = str(float(value_at) / 100)
        elif value == '=':
            if value_at:
                value = calculate(value_at)
        
        result.value = value
        result.update()
    
    btn = [ft.Container(
        content=ft.Text(value=btn['operator'], color=btn['fonte']),
        width=50,
        height=50,
        bgcolor=btn['fundo'],
        border_radius=100,
        alignment=ft.alignment.center,
        on_click=select
    ) for btn in bottons]
    
    keyboard = ft.Row(
        width=250,
        wrap=True,
        controls=btn,
        alignment='end'
    )
    
    page.add(display, keyboard)

ft.app(target=main)
