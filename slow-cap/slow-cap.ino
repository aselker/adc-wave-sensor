const int capLen = 100;

int driver = PA7;
int sensor = PA6;

void setup() {
  Serial.begin(1000000);
  pinMode(driver, OUTPUT);
  pinMode(sensor, INPUT);
}

int highReading, lowReading;
int sum;
int samples[capLen];

void loop() {
  digitalWrite(driver, HIGH);
  for (int i = 0; i < capLen; i++) {
		samples[i] = analogRead(sensor);
    delayMicroseconds(10);
  }

  digitalWrite(driver, LOW);
  for (int i = 0; i < capLen; i++) {
    samples[i] -= analogRead(sensor);
    delayMicroseconds(10);
  }

  for (int i = 0; i < capLen; i++) {
		Serial.println(samples[i]);
		delay(10);
	}

	delay(1000);

}
