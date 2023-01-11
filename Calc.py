from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.config import Config

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 300)
Config.set('graphics', 'height', 400)


class CalcApp(App):
    def update_label(self):
        self.lbl.text = self.formula

    def add_number(self, instance):
        if self.formula == "0":
            self.formula = ""
        self.formula += str(instance.text)
        self.update_label()

    def add_operation(self, instance):
        self.formula += str(instance.text)
        self.update_label()

    def calc_result(self, instance):
        if '_' in self.lbl.text:
            self.lbl2.text = "Неверное значение"
            return self.lbl2.text

        self.lbl.text = str(eval(self.lbl.text))
        self.formula = "0"

    def clear_str(self, instance):
        self.formula = "0"
        self.lbl2.text = ""
        self.update_label()

    def p_operation(self, instance):
        if len(self.lbl.text) <= 2 or "_" not in self.lbl.text or self.lbl.text.count("_") >= 2:
            self.lbl2.text = "Неверное значение"
            return self.lbl2.text
        elif self.lbl.text[0] == "_" or self.lbl.text[len(self.lbl.text) - 1] == "_":
            self.lbl2.text = "Неверное значение"
            return self.lbl2.text
        self.lst = list(map(float, self.lbl.text.split('_')))
        self.lbl2.text = str(2 * (self.lst[0] + self.lst[1]))

    def s_operation(self, insance):
        if len(self.lbl.text) <= 2 or "_" not in self.lbl.text or self.lbl.text.count("_") >= 2:
            self.lbl2.text = "Неверное значение"
            return self.lbl2.text
        elif self.lbl.text[0] == "_" or self.lbl.text[len(self.lbl.text) - 1] == "_":
            self.lbl2.text = "Неверное значение"
            return self.lbl2.text
        self.lst = list(map(float, self.lbl.text.split('_')))
        self.lbl2.text = str(self.lst[0] * self.lst[1])

    def build(self):
        self.formula = "0"
        bl = BoxLayout(orientation='vertical', padding=10)
        gl = GridLayout(cols=4, spacing=2, size_hint=(1, .6))
        self.lbl = Label(text='0', font_size=30, size_hint=(1, .2))
        self.lbl2 = Label(text='', font_size=30, size_hint=(1, .2), color=[.87, .19, .58, 1])

        bl.add_widget(self.lbl)
        bl.add_widget(self.lbl2)

        gl.add_widget(Button(text='C', on_press=self.clear_str))
        gl.add_widget(Button(text='P(перим)', on_press=self.p_operation))
        gl.add_widget(Button(text='S(площ)', on_press=self.s_operation))
        gl.add_widget(Button(text='_', on_press=self.add_number))

        gl.add_widget(Button(text='7', on_press=self.add_number))
        gl.add_widget(Button(text='8', on_press=self.add_number))
        gl.add_widget(Button(text='9', on_press=self.add_number))
        gl.add_widget(Button(text='+', on_press=self.add_operation))

        gl.add_widget(Button(text='4', on_press=self.add_number))
        gl.add_widget(Button(text='5', on_press=self.add_number))
        gl.add_widget(Button(text='6', on_press=self.add_number))
        gl.add_widget(Button(text='-', on_press=self.add_operation))

        gl.add_widget(Button(text='1', on_press=self.add_number))
        gl.add_widget(Button(text='2', on_press=self.add_number))
        gl.add_widget(Button(text='3', on_press=self.add_number))
        gl.add_widget(Button(text='*', on_press=self.add_operation))

        gl.add_widget(Button(text='.', on_press=self.add_number))
        gl.add_widget(Button(text='0', on_press=self.add_number))
        gl.add_widget(Button(text='=', on_press=self.calc_result))
        gl.add_widget(Button(text='/', on_press=self.add_operation))

        bl.add_widget(gl)

        return bl


if __name__ == '__main__':
    CalcApp().run()
