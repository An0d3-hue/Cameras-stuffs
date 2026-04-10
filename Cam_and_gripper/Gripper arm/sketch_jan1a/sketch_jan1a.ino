#include <Servo.h> 
Servo GripperServo;
Servo Arm1Servo1;
Servo Arm2Servo2;

#define VRX_PIN      A0 // Arduino pin connected to VRX pin
#define VRY_PIN      A1 // Arduino pin connected to VRY pin
#define SERVO_X_PIN  2  // Arduino pin connected to Servo motor 1
#define SERVO_Y_PIN  3  // Arduino pin connected to Servo motor 2

Servo xServo;  // create servo object to control a servo 1
Servo yServo;  // create servo object to control a servo 2

void setup() {
  Serial.begin(9600) ;
  xServo.attach(SERVO_X_PIN);
  yServo.attach(SERVO_Y_PIN);
}

void loop() {
  // read analog X and Y analog values
  int xValue = analogRead(VRX_PIN);
  int yValue = analogRead(VRY_PIN);

  int xAngle = map(xValue, 0, 1023, 0, 180); // scale it to the servo's angle (0 to 180)
  int yAngle = map(yValue, 0, 1023, 0, 180); // scale it to the servo's angle (0 to 180)

  xServo.write(xAngle); // rotate servo motor 1
  yServo.write(yAngle); // rotate servo motor 2

  // print data to Serial Monitor on Arduino IDE
  Serial.print("Joystick: ");
  Serial.print(xValue);
  Serial.print(", ");
  Serial.print(yValue);
  Serial.print(" => Servo Motor: ");
  Serial.print(xAngle);
  Serial.print("°, ");
  Serial.print(yAngle);
  Serial.println("°");
}
