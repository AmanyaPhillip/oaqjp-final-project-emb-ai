from EmotionDetection.emotion_detection import emotion_detection
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection1(self):
        result = emotion_detection("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], "joy")
    def test_emotion_detection2(self):
        result = emotion_detection("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], "anger")
    def test_emotion_detection3(self):
        result = emotion_detection("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], "disgust")
    def test_emotion_detection4(self):
        result = emotion_detection("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], "sadness")
    def test_emotion_detection5(self):
        result = emotion_detection("I am really afraid that this will happen")
        self.assertEqual(result['dominant_emotion'], "fear")    

unittest.main()