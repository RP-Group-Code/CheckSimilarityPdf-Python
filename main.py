from difflib import SequenceMatcher
text1 = "Saya firdaus dan saya tinggal di jakarta"
text2 = "Hai, saya jaka dan saya tinggal di jakarta"
sequenceScore = SequenceMatcher(None, text1, text2).ratio()
print("Both are ",sequenceScore * 100," % similar")