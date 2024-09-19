import cv2
from pyzbar.pyzbar import decode
import pyttsx3

# Initialize the pyttsx3 engine to convert text to speech
engine = pyttsx3.init()

# Method to decode the barcode or QR code
def CodeReader(image):
    # Decode the image
    detectedCodes = decode(image)

    # If nothing is detected, display a message
    if not detectedCodes:
        engine.say("Sorry, No Barcode or QR Code Detected!, Please try again")
        engine.runAndWait()
        engine.stop()
        print("Sorry, No Barcode or QR Code Detected!, Please try again")        
    else:
        # Traverse through all the detected barcodes or QR codes in the image
        for code in detectedCodes:
            # Locate the position of the barcode/QR code in the image
            (x, y, w, h) = code.rect

            # Draw a rectangle around the detected code
            cv2.rectangle(image, (x-10, y-10), (x + w+10, y + h+10), (0, 255, 0), 2)

            # Convert the byte data to a string
            codeData = code.data.decode('utf-8')
            codeType = code.type  # Get the type (QR Code, CODE128, etc.)

            # Determine if it's a barcode or QR code and print accordingly
            if codeType == "QRCODE":
                engine.say(f"A QR Code has been detected with data: {codeData}")
                engine.runAndWait()
                engine.stop()
                print(f"QR Code Data: {codeData}")
            else:
                engine.say(f"A Bar code has been detected with the data: {codeData}")
                engine.runAndWait()
                engine.stop()
                print(f"Barcode Data: {codeData} \n Type: {codeType}")
                
                
        # cv2.imshow("Detected Code", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    # Capture image from webcam
    
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Could not open the webcam!")
        exit()
        
    engine.say(f"Please show the Barcode or QR Code in front of the camera and press Enter button to capture the image")
    engine.runAndWait()
    engine.stop()
    print("Please show the Barcode or QR Code in front of the camera and press Enter button to capture the image")

    while True:
        # Read frame from the webcam
        ret, frame = cap.read()
        if not ret:
            engine.say(f"Failed to capture image")
            engine.runAndWait()
            engine.stop()
            print("Failed to capture image")
            break

        # Display the live camera feed
        cv2.imshow("Camera", frame)

        # Wait for the user to press 's' to save the image
        key = cv2.waitKey(1) & 0xFF
        if key == ord('s') or key == 13:
            # Save the captured frame to process
            captured_image = frame
            break

    # Release the camera and close the window
    
    cap.release()
    cv2.destroyAllWindows()

    # Pass the captured image to the CodeReader function
    CodeReader(captured_image)
