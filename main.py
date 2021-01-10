import kivy
from kivymd.app import MDApp
from kivy.uix.gridlayout import GridLayout

class CalculatorApp(GridLayout):
    def calculate(self,calculation):
        if calculation:
            try:
                self.display.text=str(eval(calculation))
            except Exception:
                self.display.text = "Error"
class Calculator(MDApp):
    def build(self):
        return CalculatorApp()
Calculator().run()
