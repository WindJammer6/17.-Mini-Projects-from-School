// #define LED_PIN 2

// void setup() {
//   // put your setup code here, to run once:
//   // Serial.begin(115200);
//   // Serial.println("Hello World");
//   pinMode(LED_PIN, OUTPUT);
// }

// void loop() {
//   // put your main code here, to run repeatedly:
//   digitalWrite(LED_PIN, HIGH);
//   delay(1000);

//   digitalWrite(LED_PIN, LOW);
//   delay(1000);

//   // Serial.println("I am ESP32");
//   // delay(500);
// }



/* Arduino tutorial - Buzzer / Piezo Speaker
   More info and circuit: http://www.ardumotive.com/how-to-use-a-buzzer-en.html
   Dev: Michalis Vasilakis // Date: 9/6/2015 // www.ardumotive.com */


// Only Buzzer
// const int buzzer = 9; //buzzer to arduino pin 9

// void setup(){
//   pinMode(buzzer, OUTPUT); // Set buzzer - pin 9 as an output
// }

// void loop(){
//   tone(buzzer, 1000); // Send 1KHz sound signal...
//   delay(1000);        // ...for 1 sec
//   noTone(buzzer);     // Stop sound...
//   delay(1000);        // ...for 1sec
// }


// Buzzer and Button
// const int buzzer = 9; // Buzzer to Arduino pin 9
// const int button = 2; // Button connected to Arduino pin 7

// void setup() {
//   pinMode(buzzer, OUTPUT); // Set buzzer pin as an output
//   pinMode(button, INPUT_PULLUP); // Set button pin as an input with internal pull-up resistor
// }

// void loop() {
//   if (digitalRead(button) == LOW) { // Check if the button is pressed (LOW because of pull-up resistor)
//     tone(buzzer, 1000); // Send 1KHz sound signal
//   } 
//   else {
//     noTone(buzzer); // Stop sound when button is not pressed
//   }
// }


// Microphone with Light
const int sampleWindow = 100;  // Sample window width in mS (50 mS = 20Hz)
const int AMP_PIN = A2;       // Preamp output pin connected to A0
unsigned int sample;
const int buzzer = 10;
const int IR = 8;
int count = 0;
int latest10[10];

void setup()
{
  Serial.begin(9600);
  pinMode (buzzer, OUTPUT);
  pinMode (IR, INPUT);
}

void loop()
{
  unsigned long startMillis = millis(); // Start of sample window
  unsigned int peakToPeak = 0;   // peak-to-peak level

  unsigned int signalMax = 0;
  unsigned int signalMin = 1024;

  const int thres = 90;
  
  int IRs = digitalRead (IR);

  // collect data for 50 mS and then plot data
  while (millis() - startMillis < sampleWindow)
  {
    sample = analogRead(AMP_PIN);
    Serial.println(sample);
    Serial.println(IRs);
    for (int i = 0; i < 10; i++)
    {
      Serial.print(latest10[i]);
      Serial.print(' ');
    }
    delay(50);

    latest10[count] = sample;
    count += 1;
    if (count > 9)
    {
      count = 0;
    }
    if (sample < 1024)  // toss out spurious readings
    {
      if (sample > signalMax)
      {
        signalMax = sample;  // save just the max levels
      }
      else if (sample < signalMin)
      {
        signalMin = sample;  // save just the min levels
      }
    }

   int maxVal = latest10[0];
   int minVal = latest10[0];

   for (int i = 0; i < (sizeof(latest10) / sizeof(latest10[0])); i++) {
      maxVal = max(latest10[i],maxVal);
      minVal = min(latest10[i],minVal);
   }

    Serial.println(maxVal);
    Serial.println(minVal);
    
    if ((maxVal - minVal > 200) && IRs == LOW)
    // if ((maxVal - minVal > 200) || IRs == LOW)
    { 
      digitalWrite(buzzer, HIGH);
      delay(500);
      // tone(buzzer, 1000); // Send 1KHz sound signal    
    }
    else
    {
      digitalWrite(buzzer, LOW);
      // noTone(buzzer); // Stop sound when button is not pressed
    }
  }

  // peakToPeak = signalMax - signalMin;  // max - min = peak-peak amplitude
  // Serial.println(peakToPeak);
  //double volts = (peakToPeak * 5.0) / 1024;  // convert to volts
  //Serial.println(volts);

}
