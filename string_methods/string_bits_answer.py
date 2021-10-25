movie = "My    beautiful laundrette!"

# Create a list of the above string
# without extra spaces or new lines
movie = movie.split()


# Use slices, concatenation and list index all in one line
# to join the elements of the list excluding the exclamation mark
movie = " ".join(movie[:-1]) + " " + movie[-1][:-1]

# Change the word laundrette to garden
movie = movie.replace('laundrette', 'garden')

# Switch the case of all the letters
print(movie.title())
