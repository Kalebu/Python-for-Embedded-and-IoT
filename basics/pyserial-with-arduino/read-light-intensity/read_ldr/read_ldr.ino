
int ldr = A0;

void setup(){
  pinMode(ldr, INPUT);
  Serial.begin(115200);
}

void loop(){
  int intensity = analogRead(ldr);
  if (Serial.available()){
    char command = Serial.read();
    if (command=='r') Serial.println(intensity);
  } 
}
