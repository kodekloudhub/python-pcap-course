txt = ",$,,   chocolate   banana ice-cream..."

# Add more options in the strip()
txt = txt.strip(",$ .")

# Clear any whitespaces left and print the outcome
txt = " ".join(txt.split())
print(txt)
