import cv2


def video2images(video_name, frame_num):
    cap = cv2.VideoCapture(f'videos/{video_name}.mp4')

    frame_counter = 0
    while True:
        ret, frame = cap.read()
        cv2.imshow("video3", frame)

        if frame_counter % frame_num == 0:
            isWritten = cv2.imwrite(f'images/{video_name}/{video_name}-frame-{frame_counter}.png', frame)
            if isWritten:
                print(f"Frame {frame_counter} successfully saved to folder 'images'")
            else:
                print(f"Failed to save frame {frame_counter}")
                break

        frame_counter += 1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == "__main__":
    video_names = ["video3"]
    frame_num = 20

    for video_name in video_names:
        video2images(video_name, frame_num)
