const int center = 1200;
const int upThresh = center + 200;
const int downThresh = center - 200;

int driver = PA7;
int sensor = PA6;

void setup() {
  Serial.begin(1000000);
  pinMode(driver, OUTPUT);
  pinMode(sensor, INPUT);
}

int highReading, lowReading, sum;
unsigned long time;

void loop() {
	
	sum = 0;
	for (int i = 0; i < 10; i++) {
		time = micros();
		digitalWrite(driver, HIGH);
		while ((analogRead(sensor)) < upThresh) {}
		sum += micros() - time;

		time = micros();
		digitalWrite(driver, LOW);
		while ((analogRead(sensor)) > downThresh) {}
		sum += micros() - time;
	}
	Serial.println(sum);
  delay(50);
}
