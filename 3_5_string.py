def count_chars(s):
    return {char: s.count(char) for char in set(s)}


print(count_chars('privet druz\'ja i poka'))
