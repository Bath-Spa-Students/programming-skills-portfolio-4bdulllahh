def famous_quote(quote, author):
    return f'{author} once said, "{quote}"'

quote = "It takes a wise man to discover a wise man"
author = "Diogenes"

formatted_quote = famous_quote(quote, author)
print(formatted_quote)