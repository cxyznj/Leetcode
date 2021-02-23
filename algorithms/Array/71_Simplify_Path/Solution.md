# 71. Simplify Path

This problem is to convert a path string to a canonical path string, the key idea is to process three special characters: "/", ".", "..". we can simply split the string with "/" and throw away "" and "." to easily process "/" and ".". The last task is to deal with "..". Traverse the divided array sequentially from beginning to end and append each word with "/" in canonical expect "..". When meet "..", skip it and pop the previous appended word (if there have previous one).

