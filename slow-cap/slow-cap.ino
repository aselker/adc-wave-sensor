const int capLen = 40;

int driver = PA7;
int sensor = PA6;

void setup() {
  Serial.begin(1000000);
  pinMode(driver, OUTPUT);
  pinMode(sensor, INPUT);
}

int highReading, lowReading;
int sum;
int upSamples[capLen];
int downSamples[capLen];

void loop() {
	pinMode(sensor, OUTPUT);
	digitalWrite(sensor, LOW);
	delay(1);
	pinMode(sensor, INPUT);

  digitalWrite(driver, HIGH);
  for (int i = 0; i < capLen; i++) {
		upSamples[i] = analogRead(sensor);
    delayMicroseconds(10);
  }

	pinMode(sensor, OUTPUT);
	digitalWrite(sensor, HIGH);
	delay(1);
	pinMode(sensor, INPUT);

  digitalWrite(driver, LOW);
  for (int i = 0; i < capLen; i++) {
    downSamples[i] = analogRead(sensor);
    delayMicroseconds(10);
  }

  for (int i = 0; i < capLen; i++) {
		Serial.println(upSamples[i]);
		delay(10);
	}

  for (int i = 0; i < capLen; i++) {
		Serial.println(downSamples[i]);
		delay(10);
	}

}
