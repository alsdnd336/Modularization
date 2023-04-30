from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import NumericProperty, StringProperty
import os.path


class First(Screen):
    def __init__(self, **kwargs):
        super(First, self).__init__(**kwargs)
        self.grid_layout = GridLayout()
        self.grid_layout.cols = 7

        for i in range(1, 31):
            bth = Button(text = f'{i} d')
            bth.bind(on_release = self.go_to_second)
            self.grid_layout.add_widget(bth)
        self.add_widget(self.grid_layout)

    def go_to_second(self, instance):
        num = int(instance.text.split(" ")[0])
        page_name = f'{num} day'

        if not self.manager.has_screen(page_name):
            day_page = Second(name = page_name,num = num) # 이 부분에서 class의 name과 num을 제정의
            self.manager.add_widget(day_page) # 나중에 ScreenManager에 day_Page를 추가한다.

        app = App.get_running_app() # MyApp 인스턴스를 반환한다.
        app.page_name = page_name 
        app.num = num

        self.manager.current = page_name
        self.manager.transition.direction = "left"



class Second(Screen):
    num = NumericProperty(0) # 지속적으로 num 오류가 뜬 이유는 26번 줄에서 num을 추가했지 Second에는 num 속성이 없었기 때문

    def __init__(self, **kwargs):
        super(Second, self).__init__(**kwargs)
        self.num = kwargs.get('num', 0)
        
    
    def on_pre_enter(self):
        self.grid_layout = GridLayout(cols = 1)
        label = Label(text=f'Days {self.num}', font_size = 44, size_hint = (1, 0.17))
        self.tpt = TextInput(text = '', font_size = 20, pos = (0,0), size_hint = (1, 1))
        self.btn = Button(text = f'{self.num} click', font_size=44, size_hint = (1,0.1))
        self.grid_layout.add_widget(label)
        self.grid_layout.add_widget(self.tpt)
        self.grid_layout.add_widget(self.btn)
        self.add_widget(self.grid_layout)

        if not os.path.isfile(f"C:\\venv\\Page\\{self.num} day"):
            with open(f"C:\\venv\\Page\\{self.num} day", 'w') as f:
                f.write('To-Do-List')


        with open(f"C:\\venv\\Page\\{self.num} day", 'r') as f:
            self.text = f.read()
            self.tpt.text = self.text
        
    def on_text(self, instance, value):
        with open(f"C:\\venv\\Page\\{self.num} day", "a") as f:
            f.write(value)

    def on_leave(self):
        with open(f"C:\\venv\\Page\\{self.num} day", "w") as f:
            f.write(self.tpt.text)


   
class three(Screen):
    pass

class MyApp(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(First(name='first'))
        return sm
    
    def on_stop(self):
        text_input = self.root.get_screen(self.page_name).tpt
        with open(f"C:\\venv\\Page\\{self.num} day", "w") as f:
            f.write(text_input.text)
            
if __name__ == "__main__":
    MyApp().run()