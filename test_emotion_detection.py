from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        #test case for joy as dominant emotion
        result1 = emotion_detector('I am glad this happened')
        self.assertEqual(result1['dominant_emotion'], 'joy')

        #test case for anger as dominant emotion
        result2 = emotion_detector('I am really mad about this')
        self.assertEqual(result2['dominant_emotion'], 'anger')

        #test case for disgust as dominant emotion
        result3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result3['dominant_emotion'], 'disgust')
        
        #test case for sadness as dominant emotion
        result4 = emotion_detector('I am so sad about this')
        self.assertEqual(result4['dominant_emotion'], 'sadness')

        #test case for fear as dominant emotion
        result5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result5['dominant_emotion'], 'fear')

unittest.main()