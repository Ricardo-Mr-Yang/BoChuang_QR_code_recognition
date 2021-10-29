import cv2
import uptech
import apriltag
import time


class ApriltagDetect:
    def __init__(self):
        self.target_id = 0
        self.at_detector = apriltag.Detector(apriltag.DetectorOptions(families='tag36h11 tag25h9'))   #for linux
        #self.at_detector = apriltag.Detector(families='tag36h11 tag25h9')                            #for windows
    
    def update_frame(self,frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        tags = self.at_detector.detect(gray)
        #print(tags)
        if len(tags) == 0 :
            up.ADC_IO_SetIOLevel(0,0)
            up.LCD_PutString(0, 0, 'NULL!!')
            up.LCD_Refresh()
        
        else:
            for tag in tags:
                print(tag.tag_id)
                # 炸弹
                if tag.tag_id == 0:
                    up.LCD_SetForeColor(fore_color)
                    up.LCD_PutString(0, 0, 'Bomb!!')
                    up.LCD_Refresh()
                    up.ADC_IO_SetIOLevel(0,1)
                # 非炸弹
                elif tag.tag_id == 1:
                    up.LCD_PutString(0, 0, 'Energy')
                    up.LCD_Refresh()
                    up.ADC_IO_SetIOLevel(0,0)
                else:
                    up.LCD_PutString(0, 0, 'Baffle')
                    up.LCD_Refresh()
                    up.ADC_IO_SetIOLevel(0,0)


if __name__ == '__main__':
    up=uptech.UpTech()
    up.LCD_Open(2)
    up.ADC_IO_Open()
    fore_color = up.COLOR_GREEN
    back_color = up.COLOR_BLACK
    up.LCD_SetForeColor(fore_color)
    up.LCD_SetBackColor(back_color)
    up.LCD_FillScreen(back_color)
    #up.LCD_SetFont(up.FONT_8X14)
    up.LCD_SetFont(up.FONT_24X40)
    time.sleep(0.1)
    up.ADC_IO_SetIOMode(0,1)
    up.LCD_PutString(0, 0, 'Start!')
    up.LCD_Refresh()
    #ADC_IO_SetIOLevel(index,level)

    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
    ad = ApriltagDetect()
    while True:
        ret, frame = cap.read()
        #frame = cv2.rotate(frame, cv2.ROTATE_180)
        ad.update_frame(frame)
        #cv2.imshow("img", frame)
        if cv2.waitKey(100) & 0xff == ord('q'):
            up.LCD_PutString(0, 0, 'End   ')
            up.LCD_Refresh()
            break
    cap.release()
    cv2.destroyAllWindows()
