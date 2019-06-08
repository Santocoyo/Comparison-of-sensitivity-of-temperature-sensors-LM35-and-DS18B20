#include <OneWire.h>
#include <DallasTemperature.h>
OneWire ourWire1(9);
DallasTemperature sensors1(&ourWire1);
void setup() {
delay(1000);
Serial.begin (9600);
sensors1.begin();
Serial.print("DS18B20");
Serial.print("\t");
Serial.println("LM35");
}
void loop() {
sensors1.requestTemperatures();
float temp1= sensors1.getTempCByIndex(0);
Serial.print (temp1);
Serial.print(",");
Serial.println(analogRead(A0)*500.0/1023.0);
delay(1000);
}
