import qrcode

img=qrcode.make("https://www.youtube.com/watch?v=-GmJLI122ZM")
img.save("utube.jpg")