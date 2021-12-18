mdecode(data, cv2.IMREAD_COLOR)
        # img=cv2.imread("pallav.jpg")

        res,c=detect_hand(img)
        # cv2.imwrite("raw_data.jpg",c)
        # cv2.imwrite("res.jpg", res)
        res=image_preprocessing(res)
        label=prediction(res)
