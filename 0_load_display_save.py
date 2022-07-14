import cv2

filepath = 'data//gambar_keren.PNG'
# load file image
image = cv2.imread(filepath)

# display image
cv2.imshow('Tugas pak djum', image)
cv2.waitKey(0)

# save image
save_url = 'data//tugas_pak_djum.png'
cv2.imwrite(save_url, image)
print("GAMBAR TELAH DISIMPAN : ", save_url)