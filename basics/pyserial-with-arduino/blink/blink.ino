int led = 13;

void setup(){
    pinMode(led, OUTPUT);
    Serial.begin(9600);
}

void loop(){
  if (Serial.available()){
      char command = Serial.read();
      if (command=='o'){
        digitalWrite(led, HIGH);
      }
      else{
        digitalWrite(led, LOW);
      }
  }
}