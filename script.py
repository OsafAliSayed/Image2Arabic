from ArabicOcr import arabicocr
import cv2

image_path='sample.jpg'
out_path='out.jpg'
results=arabicocr.arabic_ocr(image_path, out_path)
print(results)
words=[]
for i in range(len(results)):	
		word=results[i][1]
		words.append(word)

with open ('file.txt','w',encoding='utf-8')as myfile:
    for word in words:
        myfile.write(word+'\n')
img = cv2.imread('out.jpg', cv2.IMREAD_UNCHANGED)
cv2.imshow("arabic ocr",img)
cv2.waitKey(0)