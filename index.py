import cv2

def get_click_position(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Position cliquée : x={x}, y={y}")
        cv2.circle(img, (x, y), 5, (0, 255, 0), -1)
        cv2.imshow("Image", img)

img = cv2.imread('')

cv2.namedWindow("Image", cv2.WINDOW_NORMAL)

cv2.imshow("Image", img)

cv2.setMouseCallback("Image", get_click_position)

cv2.waitKey(0)
cv2.destroyAllWindows()
