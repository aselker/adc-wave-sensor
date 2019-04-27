const int avgLen = 10;
const int delayTime = 20; // Microseconds

int driver = PA7;
int sensor = PA6;

void setup() {
  Serial.begin(1000000);
  pinMode(driver, OUTPUT);
  pinMode(sensor, INPUT);
}

int highReading, lowReading;
int sum;
// int samples[avgLen];

void loop() {
  sum = 0;
  for (int i = 0; i < avgLen; i++) {
    digitalWrite(driver, HIGH);
    delayMicroseconds(delayTime);
    highReading = analogRead(sensor);
    digitalWrite(driver, LOW);
    delayMicroseconds(delayTime);
    lowReading = analogRead(sensor);
    /*
    samples[i] = highReading - lowReading;
    sum += samples[i];
    sum -= samples[0];
    */
    sum += (highReading - lowReading);
  }
  Serial.println(sum);

  delay(50);

  /*
  for (int i = 0; i < 100; i++) {
    Serial.println(analogRead(sensor));
    delayMicroseconds(10);
  }
  
  

  digitalWrite(driver, LOW);
  for (int i = 0; i < 100; i++) {
    Serial.println(analogRead(sensor));
    delayMicroseconds(10);
  }
  */
}
