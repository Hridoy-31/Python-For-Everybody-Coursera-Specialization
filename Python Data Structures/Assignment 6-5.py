text = "X-DSPAM-Confidence:    0.8475"
x = text.find('0')
x = float(text[23:29])
print(x)
