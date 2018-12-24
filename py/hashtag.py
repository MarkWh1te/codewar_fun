# The marketing team is spending way too much time typing in hashtags.
# Let's help them with out own Hashtag Generator!

# Here's the deal:

# It must start with a hashtag (#).
# All words must have their first letter capitalized.
# If the final result is longer than 140 chars it must return false.
# If the input or the result is an empty string it must return false


# " Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
# "    Hello     World   "                  =>  "#HelloWorld"
# ""                                        =>  false
def generate_hashtag(s):
    result = "#" + "".join([x.title() for x in s.split()])
    return result if (len(result) < 140 and len(result) > 1) else False


if __name__ == "__main__":
    assert generate_hashtag("code wars") == "#CodeWars"
    assert generate_hashtag("") == False
    assert generate_hashtag(
        "#LooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooongCat"
    ) == False
