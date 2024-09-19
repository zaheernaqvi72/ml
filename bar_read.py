import cv2
from pyzbar.pyzbar import decode
import pyttsx3


engine = pyttsx3.init()

# Make one method to decode the barcode
def BarcodeReader(image):
    # Decode the barcode image
    detectedBarcodes = decode(image)

    # If not detected, then print the message
    if not detectedBarcodes:
        engine.say("Sorry, Barcode Not Detected or your barcode is blank/corrupted!")
        engine.runAndWait()
        engine.stop()
    else:
        # Traverse through all the detected barcodes in the image
        for barcode in detectedBarcodes:
            # Locate the barcode position in image
            (x, y, w, h) = barcode.rect

            # Put the rectangle in image using cv2 to highlight the barcode
            cv2.rectangle(image, (x-10, y-10), (x + w+10, y + h+10), (255, 0, 0), 2)

            if barcode.data != "":
                # Print the barcode data
                print("Barcode Data:", barcode.data.decode('utf-8'))
                print("Barcode Type:", barcode.type)

        # Display the image with the barcode highlighted
        cv2.imshow("Barcode Detection", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    # Capture image from webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Could not open the webcam!")
        exit()

    print("Press 's' to capture the image")

    while True:
        # Read frame from the webcam
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image")
            break

        # Display the live camera feed
        cv2.imshow("Camera", frame)

        # Wait for the user to press 's' to save the image
        if cv2.waitKey(1) & 0xFF == ord('s'):
            # Save the captured frame to process
            captured_image = frame
            break

    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()

    # Pass the captured image to the BarcodeReader function
    BarcodeReader(captured_image)
