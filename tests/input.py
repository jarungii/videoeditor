import unittest
from entities import *
from entities.funcs import VidEdit


class TestVidEdit(unittest.TestCase):
    def setUp(self):
        self.edit_f = VidEdit("Video_1min.mp4")

    def test_cut_video(self):
        start_time = "00:00:05"
        end_time = "00:00:10"
        self.edit_f.cut_video(start_time, end_time)
        duration_after_cut = self.edit_f.get_dur()

        # Проверяет, что длительность видео после обрезки равна ожидаемой длительности
        expected_duration = 45  # Ожидаемая длительность после обрезки (в секундах)
        self.assertEqual(duration_after_cut, expected_duration, "Длительность видео после обрезки неверная")


if __name__ == '__main__':
    unittest.main()
