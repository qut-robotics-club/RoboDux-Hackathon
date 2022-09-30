double v1 = 0; // Front Left
double v2 = 0; // Back Right
double v3 = 0; // Front Left
double v4 = 0; // Back Right

double angle = 0;
double velocity = 0;

int i = 0;
String msg[2];

String temp;

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
}

unsigned long m1LastPulse = millis();
unsigned long m2LastPulse = millis();
unsigned long m3LastPulse = millis();
unsigned long m4LastPulse = millis();

unsigned long m1curtime = millis();
unsigned long m2curtime = millis();
unsigned long m3curtime = millis();
unsigned long m4curtime = millis();

unsigned long m1waitTime = 0;
unsigned long m2waitTime = 0;
unsigned long m3waitTime = 0;
unsigned long m4waitTime = 0;

void spinMotor(int motorPin, double vel) {
  Serial.println("Spinning motor");
}


void loop() {
  // put your main code here, to run repeatedly:
  //if (Serial.available() > 0) {
    //String data = Serial.readStringUntil('\n');    
  //}
  i = 0;
  msg[0] = msg[1] = "";
  if (Serial.available()) {
    delay(10);
    while (Serial.available() > 0) {
      temp = (char)Serial.read();

      if (temp == ",") {
        i += 1;
      }
      
      msg[i] += temp;
    }
    Serial.flush();

    drive(msg);
  }
}

void drive(String msg[]) {

  velocity = msg[0].toDouble();
  angle = msg[1].toDouble();
  
  v1 = velocity * cos(angle);
  v2 = velocity * sin(angle);
  v3 = velocity * sin(angle);
  v4 = velocity * cos(angle);

  v1 = map(v1, -velocity, velocity, -100, 100);
  v2 = map(v2, -velocity, velocity, -100, 100);
  v3 = map(v3, -velocity, velocity, -100, 100);
  v4 = map(v4, -velocity, velocity, -100, 100);
}
