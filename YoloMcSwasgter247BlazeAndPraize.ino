  int LEDR = 2;
  int LEDG = 3;
  int LEDB = 4;

void setup() {
  Serial.begin(9600); // set the baud rate
  Serial.println("Ready"); // print "Ready" once
  pinMode(LEDR, OUTPUT);
  pinMode(LEDG, OUTPUT);
  pinMode(LEDB, OUTPUT);
}
void loop() {
  if(Serial.available()){ // only send data back if data has been sent
    char inByte = Serial.read(); // read the incoming data
    switch(inByte) {
      case 'a':
        digitalWrite(LEDR, HIGH); 
        digitalWrite(LEDG, LOW); 
        digitalWrite(LEDB, LOW); 
        break; 
      case 'n':
        digitalWrite(LEDR, LOW); 
        digitalWrite(LEDG, LOW); 
        digitalWrite(LEDB, LOW); 
        break; 
      case 's':
        digitalWrite(LEDR, LOW); 
        digitalWrite(LEDG, LOW); 
        digitalWrite(LEDB, HIGH);
        break; 
      case 'd':
        digitalWrite(LEDR, LOW); 
        digitalWrite(LEDG, HIGH); 
        digitalWrite(LEDB, LOW);
        break; 
      case 'c':
        digitalWrite(LEDR, HIGH); 
        digitalWrite(LEDG, HIGH); 
        digitalWrite(LEDB, LOW);
        break;
      case 'f':
        digitalWrite(LEDR, HIGH); 
        digitalWrite(LEDG, LOW); 
        digitalWrite(LEDB, HIGH);                
        break; 
      case 'h':
        digitalWrite(LEDR, HIGH); 
        digitalWrite(LEDG, HIGH); 
        digitalWrite(LEDB, HIGH);  
        break; 
      case 'x':
        digitalWrite(LEDR, LOW); 
        digitalWrite(LEDG, HIGH); 
        digitalWrite(LEDB, HIGH);                   
        break; 
    }
  }
  
  delay(100); // delay for 1/10 of a second
}
