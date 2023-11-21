from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from functools import partial


class NumberConverterApp(App):
    def build(self):
        self.icon ="system 2.png"
        self.title = 'Number System Converter'

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.input_number = TextInput(multiline=False, input_type='number')
        self.input_base_from = TextInput(multiline=False, input_type='number')
        self.input_base_to = TextInput(multiline=False, input_type='number')

        convert_button = Button(text='Convert', on_press=self.convert_number)

        self.output_label = Label(text='', halign='center', font_size=20)

        layout.add_widget(Label(text='Enter the number:'))
        layout.add_widget(self.input_number)
        layout.add_widget(Label(text='Enter the source base (2, 8, 10, or 16):'))
        layout.add_widget(self.input_base_from)
        layout.add_widget(Label(text='Enter the target base (2, 8, 10, or 16):'))
        layout.add_widget(self.input_base_to)
        layout.add_widget(convert_button)
        layout.add_widget(self.output_label)

        return layout

    def convert_number(self, instance):
        number = self.input_number.text
        base_from = int(self.input_base_from.text)
        base_to = int(self.input_base_to.text)

        result = self._convert_number(number, base_from, base_to)

        if result is not None:
            self.output_label.text = f"Result in base {base_to}: {result}"
        else:
            self.output_label.text = ""

    def _convert_number(self, number, from_base, to_base):
        try:
            if from_base == 10:
                result = int(number, 10)
            elif from_base == 2:
                result = int(number, 2)
            elif from_base == 8:
                result = int(number, 8)
            elif from_base == 16:
                result = int(number, 16)
            else:
                print("Unsupported source base. Please enter 2, 8, 10, or 16.")
                return None

            if to_base == 10:
                return str(result)
            elif to_base == 2:
                return bin(result).replace("0b", "")
            elif to_base == 8:
                return oct(result).replace("0o", "")
            elif to_base == 16:
                return hex(result).replace("0x", "")
            else:
                print("Unsupported target base. Please enter 2, 8, 10, or 16.")
                return None
        except ValueError:
            print("Invalid input. Please enter a valid number in the specified base.")
            return None


if __name__ == '__main__':
    NumberConverterApp().run()
