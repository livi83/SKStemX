import re

class Skstemx:
    WORD_PATTERN = re.compile(r"^\w+$", re.UNICODE)

    def stem(self, word):
        s = word.lower()
        s = self.rem_case(s)
        s = self.rem_possessives(s)
        s = self.rem_comparative(s)
        s = self.rem_diminutive(s)
        s = self.rem_augmentative(s)
        s = self.rem_derivational(s)
        return s

    def rem_case(self, word):
        if len(word) > 7 and word.endswith("atoch"):
            return word[:-5]
        if len(word) > 6 and word.endswith("aťom"):
            return self._palatalise(word[:-3])
        if len(word) > 5:
            if word[-3:] in ("och", "ich", "ích", "ého", "ami", "emi", "ému", "ete", "eti", "iho", "ího", "ími", "imu", "aťa"):
                return self._palatalise(word[:-2])
            if word[-3:] in ("ách", "ata", "aty", "ých", "ami", "ové", "ovi", "ými", "avý"):
                return word[:-3]
        if len(word) > 4:
            if word.endswith("om"):
                return self._palatalise(word[:-1])
            if word[-2:] in ("es", "ém", "ím"):
                return self._palatalise(word[:-2])
            if word[-2:] in ("úm", "at", "ám", "os", "us", "ým", "mi", "ou", "ej"):
                return word[:-2]
        if len(word) > 3:
            if word[-1] in "eií":
                return self._palatalise(word)
            if word[-1] in "úyaoáéý":
                return word[:-1]
        return word

    def rem_possessives(self, word):
        if len(word) > 5:
            if word.endswith("ov"):
                return word[:-2]
            if word.endswith("in"):
                return self._palatalise(word[:-1])
        return word

    def rem_comparative(self, word):
        if len(word) > 5 and word[-3:] in ("ejš", "ějš"):
            return self._palatalise(word[:-2])
        return word

    def rem_diminutive(self, word):
        if len(word) > 7 and word.endswith("oušok"):
            return word[:-5]
        if len(word) > 6:
            if word[-4:] in ("ečok", "éčok", "ičok", "íčok", "enok", "énok", "inok", "ínok"):
                return self._palatalise(word[:-3])
            if word[-4:] in ("áčok", "ačok", "očok", "učok", "anok", "onok", "unok", "ánok"):
                return self._palatalise(word[:-4])
        if len(word) > 5:
            if word[-3:] in ("ečk", "éčk", "ičk", "íčk", "enk", "énk", "ink", "ínk", "áčk", "ačk", "očk", "učk", "ank", "onk", "unk", "átk", "ánk", "ušk"):
                return self._palatalise(word[:-3])
            if word[-3:] in ("ek", "ék", "ík", "ik", "ák", "ak", "ok", "uk"):
                return word[:-1]
        if len(word) > 4:
            if word[-2:] in ("ek", "ék", "ík", "ik"):
                return self._palatalise(word[:-1])
            if word[-2:] in ("ák", "ak", "ok", "uk"):
                return word[:-1]
        if len(word) > 3 and word[-1] == "k":
            return word[:-1]
        return word

    def rem_augmentative(self, word):
        if len(word) > 6 and word.endswith("ajzn"):
            return word[:-4]
        if len(word) > 5 and word[-3:] in ("izn", "isk"):
            return self._palatalise(word[:-2])
        if len(word) > 4 and word.endswith("ák"):
            return word[:-2]
        return word

    def rem_derivational(self, word):
        if len(word) > 8 and word.endswith("obinec"):
            return word[:-6]
        if len(word) > 7:
            if word.endswith("ionár"):
                return self._palatalise(word[:-4])
            if word[-5:] in ("ovisk", "ovstv", "ovišt", "ovník", "ostný", "nosti"):
                return word[:-5]
        if len(word) > 6:
            if word[-4:] in ("ások", "nosť", "teln", "ovec", "ovík", "ovtv", "ovin", "štin"):
                return word[:-4]
            if word[-4:] in ("enic", "inec", "itel"):
                return self._palatalise(word[:-3])
        if len(word) > 5:
            if word.endswith("árn"):
                return word[:-3]
            if word[-3:] in ("enk", "ián", "ist", "isk", "išt", "itb", "írn"):
                return self._palatalise(word[:-2])
            if word[-3:] in ("och", "ost", "ovn", "oun", "out", "ouš", "ušk", "kyn", "čan", "kář", "néř", "ník", "ctv", "stv"):
                return word[:-3]
        if len(word) > 4:
            if word[-2:] in ("áč", "ač", "án", "an", "ár", "ar", "ás", "as"):
                return word[:-2]
            if word[-2:] in ("ec", "en", "ér", "ír", "ic", "in", "ín", "it", "iv"):
                return self._palatalise(word[:-1])
            if word[-2:] in ("ob", "ot", "ov", "oň", "ul", "yn", "čk", "čn", "dl", "nk", "tv", "tk", "vk"):
                return word[:-2]
        if len(word) > 3 and word[-1] in "cčklnt":
            return word[:-1]
        return word

    def _palatalise(self, word):
        if word[-2:] in ("ci", "ce", "či", "če"):
            return word[:-2] + "k"
        if word[-2:] in ("zi", "ze", "ži", "že"):
            return word[:-2] + "h"
        if word[-3:] in ("čte", "čti", "čtí"):
            return word[:-3] + "ck"
        if word[-3:] in ("šte", "šti", "ští"):
            return word[:-3] + "sk"
        return word[:-1]
