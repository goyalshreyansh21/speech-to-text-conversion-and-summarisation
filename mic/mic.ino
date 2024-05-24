#include <Arduino.h>
#include <stdint.h>

const int sampleWindow = 50; // Sample window width in milliseconds (50ms = 20Hz)
unsigned int sample;
int micPin = A0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  unsigned long startMillis = millis();  // Start of sample window
  unsigned int peakToPeak = 0;   // peak-to-peak level
  unsigned int signalMax = 0;
  unsigned int signalMin = 1024;

  // collect data for 50 milliseconds
  while (millis() - startMillis < sampleWindow) {
    sample = analogRead(micPin);
    if (sample < 1024)  // toss out spurious readings
    {
      if (sample > signalMax) {
        signalMax = sample;  // save just the max levels
      } else if (sample < signalMin) {
        signalMin = sample;  // save just the min levels
      }
    }
  }
  peakToPeak = signalMax - signalMin;  // max - min = peak-peak amplitude
  Serial.println(peakToPeak);  // Send peak to peak value over serial
}
