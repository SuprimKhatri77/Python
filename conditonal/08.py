Chars = 5

if Chars < 6:
    pw_strength = 'Weak'
elif Chars <= 10:
    pw_strength = 'Medium' 
else:
    pw_strength = 'Strong'
print(pw_strength)