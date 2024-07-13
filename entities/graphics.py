from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit
from entities.funcs import VidEdit


class VideoGraphics(QWidget):
    def __init__(self):
        super().__init__()
        self.file_path = "none"
        self.save_file_path = "none"
        self.setWindowTitle("the mp4 editor")
        self.path_input = QLineEdit()
        self.set_path = QPushButton("Choose this video")
        self.cut_from = QLineEdit()
        self.cut_to = QLineEdit()
        self.cut_video_button = QPushButton("Cut Video")
        self.speed_factor = QLineEdit()
        self.change_speed_button = QPushButton("Change Speed")
        self.image_input = QLineEdit()
        self.insert_image_button = QPushButton("Insert Image")
        self.save_path_input = QLineEdit()
        self.save_video_button = QPushButton("SAVE HERE")
        self.another_path = QLineEdit()
        self.another_one = QPushButton("Concatenate")
        self.fadeindur = QLineEdit()
        self.fadeinbut = QPushButton("Fade in")
        self.fadeoutdur = QLineEdit()
        self.fadeoutbut = QPushButton("Fade out")
        self.undo_button = QPushButton("Undo Last Action")

        self.edit_f = VidEdit(self.file_path)

        self.set_path.clicked.connect(self.set_file)
        self.cut_video_button.clicked.connect(self.cut)
        self.save_video_button.clicked.connect(self.set_save_file)
        self.change_speed_button.clicked.connect(self.speed)
        self.undo_button.clicked.connect(self.undo)
        self.another_one.clicked.connect(self.another)
        self.fadeinbut.clicked.connect(self.fade_in_click)
        self.fadeinbut.clicked.connect(self.fade_out_click)



        layout = QVBoxLayout()
        layout.addWidget(self.path_input)
        layout.addWidget(self.set_path)
        layout.addWidget(self.save_path_input)
        layout.addWidget(self.save_video_button)
        layout.addWidget(self.cut_from)
        layout.addWidget(self.cut_to)
        layout.addWidget(self.cut_video_button)
        layout.addWidget(self.speed_factor)
        layout.addWidget(self.change_speed_button)
        layout.addWidget(self.fadeindur)
        layout.addWidget(self.fadeinbut)
        layout.addWidget(self.fadeoutdur)
        layout.addWidget(self.fadeoutbut)
        layout.addWidget(self.image_input)
        layout.addWidget(self.insert_image_button)
        layout.addWidget(self.another_path)
        layout.addWidget(self.another_one)
        layout.addWidget(self.undo_button)

        self.setLayout(layout)

    def cut(self):
        self.edit_f.cut_video(self.cut_from.text(), self.cut_to.text())

    def speed(self):
        self.edit_f.change_speed(float(self.speed_factor.text()))

    def fade_in_click(self):
        self.edit_f.fade_in(int(self.fadeindur.text()))

    def fade_out_click(self):
        self.edit_f.fade_out(int(self.fadeoutdur.text()))


    def another(self):
        self.edit_f.con(self.another_path.text())

    def set_file(self):
        chosen = self.path_input.text()
        if chosen != "":
            self.file_path = chosen
        else:
            self.file_path = "none"
        self.edit_f = VidEdit(self.file_path)
        self.edit_f.change_path = True
        print(self.edit_f.file_path)

    def set_save_file(self):
        chosen = self.save_path_input.text()
        self.edit_f.final_path = chosen
        print(self.edit_f.final_path)

    def undo(self):
        self.edit_f.undo_last_action()
