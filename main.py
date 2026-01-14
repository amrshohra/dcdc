
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
import webbrowser
import os

class AmrLayout(BoxLayout):
    def build(self):
        self.icon = "app_icon.png"
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        # أضافة الصورة
        img_path = os.path.join(os.path.dirname(__file__), "m.png")
        if os.path.exists(img_path):
            self.img = Image(source=img_path, size_hint_y=None, height=600, allow_stretch=True,keep_ratio=True)
            self.add_widget(self.img)
        else:
            self.img = None

        # زر فتح الموقع 
        btn_open = Button(text="Press to enter ",size_hint_y=None, height=60)
        btn_open.bind(on_release=self.open_site)
        self.add_widget(btn_open)

    def open_site(self, *args):
        url = "https://sites.google.com/view/amr-app?usp=sharing"
        webbrowser.open(url)

class AmrApp(App):
    def build(self):
        self.title = "تطبيق عمرو لتوصيل ونشر الإعلانات "
        return AmrLayout()

if __name__ == "__main__":
    AmrApp().run()
