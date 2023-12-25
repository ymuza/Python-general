from window import Window
from textfile import TexFile

storage = TexFile()
w = Window(storage)

w.write_text("Greetings from Córdoba")

w.show_window()

w.save_text()
