import cv2

image = cv2.imread('data/saya.JPG')
(h, w) = image.shape[0:2]

cv2.imshow('Gambar saya: ', image)

# access pixel
(b, g, r) = image[0,0]
print("pixel on (0, 0) - Red : {}, Green : {}, Blue : {}".format(r,g,b))

# cX = center of x(column) | cY = center of y(row)
(cX, cY) = (w//2, h//2)
tl = image[0:cY, 0:cX]
tr = image[0:cY, cX:w]
bl = image[cY:h, 0:cX]
br = image[cY:h, 0:cX]
cv2.imshow('Top Left', tl)
cv2.imshow('Top Right', tr)
cv2.imshow('Bottom Left', bl)
cv2.imshow('Bottom Right', br)

image[cY:h, 0:cX] = (100, 240, 233)
cv2.imshow('Result manipulated image', image)

cv2.waitKey(0)
