from moviepy.editor import *


class VidEdit:
    def __init__(self, file_path):
        self.file_path = file_path
        self.cur_video = VideoFileClip
        self.final_path = file_path
        self.history = []
        self.change_path = True

    def get_dur(self):
        if self.change_path:
            clip = VideoFileClip(self.file_path)
        else:
            clip = self.cur_video
        return clip.duration()

    def change_speed(self, factor):
        if self.change_path:
            clip = VideoFileClip(self.file_path)
        else:
            clip = self.cur_video
        newclip = clip.speedx(factor)
        self.cur_video = newclip
        newclip.write_videofile(self.final_path)
        self.change_path = False
        action = ("change_speed", factor)
        self.history.append(action)

    def cut_video(self, start_time, end_time):
        if start_time == "":
            start_time = 0
        if end_time == 0:
            end_time = 10000000  # anywayyy

        if self.change_path:
            cut_clip = VideoFileClip(self.file_path).subclip(start_time, end_time)
        else:
            cut_clip = self.cur_video.subclip(start_time, end_time)

        self.cur_video = cut_clip
        self.cur_video.write_videofile(self.final_path)
        self.change_path = False
        print("action")
        action = ("cut_video", start_time, end_time)
        self.history.append(action)

    def insert_image(self, image_path, duration, position, filename):
        video_clip = VideoFileClip(self.file_path)
        image_clip = ImageClip(image_path)
        image_clip = image_clip.set_duration(duration).set_position(position)
        final_clip = CompositeVideoClip([video_clip, image_clip.set_start(0)])
        final_clip.write_videofile(filename)
        self.file_path = filename

    def con(self, an_path):
        if self.change_path:
            clip = VideoFileClip(self.file_path)
        else:
            clip = self.cur_video
        an_clip = VideoFileClip(an_path)
        print("con start")
        con_clip = concatenate_videoclips([clip, an_clip], method = "compose")
        con_clip.write_videofile(self.final_path)
        self.cur_video = con_clip
        self.change_path = False
        action = ("con", an_path)
        self.history.append(action)

    def save_edited_video(self, output_path):
        self.cur_video = output_path
        self.cur_video.write_videofile(self.final_path)
        print(output_path)

    def fade_in(self, dur):
        if self.change_path:
            clip = VideoFileClip(self.file_path)
        else:
            clip = self.cur_video
        print(dur)
        newclip = clip.fadein(dur)
        self.cur_video = newclip
        newclip.write_videofile(self.final_path)
        self.change_path = False
        action = ("fade_in", dur)
        self.history.append(action)

    def fade_out(self, dur):
        if self.change_path:
            clip = VideoFileClip(self.file_path)
        else:
            clip = self.cur_video
        newclip = clip.fadeout(dur)
        self.cur_video = newclip
        newclip.write_videofile(self.final_path)
        self.change_path = False
        action = ("fade_out", dur)
        self.history.append(action)


    def undo_last_action(self):
        act_history = self.history
        self.history = []
        act_history.pop()
        self.change_path = True
        for action in act_history:
            print(action)
            getattr(self, action[0])(*action[1:])
