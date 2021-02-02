import difflib


dif = difflib.Differ()
differ = dif.compare('abc', 'abcd')

dif_2 = difflib.SequenceMatcher(None, '123', '1234')


print(list(differ), '\n', dif_2.ratio())
