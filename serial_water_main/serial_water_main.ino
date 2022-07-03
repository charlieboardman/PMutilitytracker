// the setup function runs once when you press reset or power the board

void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(2, INPUT_PULLUP);
  Serial.begin(9600);  

}


// the loop function runs over and over again forever
void loop() {
  
  int sensorVal = digitalRead(2);
  if (sensorVal == HIGH) {

  //digitalWrite(LED_BUILTIN, LOW);
    //Serial.println('0');
    //Serial.flush();

  } if (sensorVal == LOW) {

  digitalWrite(LED_BUILTIN, HIGH);
    Serial.println('1');
    Serial.flush();
  }
  
}
