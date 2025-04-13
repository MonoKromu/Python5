text = 'cats dog CAT DOGGY monkey'
print(sorted(text.split()))
print(sorted(text.split(), key=lambda x: x.lower()))
