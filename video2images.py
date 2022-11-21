import cv2


if __name__ == "__main__":
    cap = cv2.VideoCapture('video/video3.mp4')

    frameCounter = 0
    while True:
        ret, frame = cap.read()
        cv2.imshow("video3", frame)

        if frameCounter % 10 == 0:
            isWritten = cv2.imwrite(f'images/video3/video3-frame-{frameCounter}.png', frame)
            if isWritten:
                print(f"Frame {frameCounter} successfully saved to folder 'images'")
            else:
                print(f"Failed to save frame {frameCounter}")
                break;

        frameCounter += 1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break