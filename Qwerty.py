const int trgpin = 9;
const int echopin = 10;

int counter = 0;
long time;
int distance; 

void setup(){
pinMode(trgpin, OUTPUT);
pinMode(echopin, INPUT);
Serial.begin(9600);
}


void distance(){
digitalWrite(trgpin, LOW);
delayMicroseconds(3);
digitalWrite(trgpin, HIGH);
delayMicroseconds(12);
digitalWrite(trgpin, LOW);

time = pulseIn(echopin, HIGH);

distance = (time*0.0343)/2;

Serial.print("Distance: ");
Serial.println(distance);


}

void loop(){





}

    





