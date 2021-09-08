import numpy as np
import cv2

template = cv2.imread('template.jpg',0)
cv2.imshow("template",template)

frame = cv2.imread("players.jpg",0)
cv2.imshow("Frame",frame)

result = cv2.matchTemplate(frame, template, cv2.TM_CCOEFF_NORMED)
cv2.imshow("matching",result)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
print(max_val,max_loc)
# cv2.circle(result,max_loc,10,(255,10,10),2)

cv2.imshow("matching",result)

cv2.waitKey(0)
cv2.destroyAllWindows()