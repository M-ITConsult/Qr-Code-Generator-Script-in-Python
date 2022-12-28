import qrcode

# Encoding data
data = 'insert your data, link, images'
# Encoding data using function make()
img = qrcode.make(data)

# Save image file
img.save('MyQrCode.png')