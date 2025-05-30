#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 4, 5, 6, 7);

String inputString = "";         // a String to hold incoming data
bool stringComplete = false;     // whether the string is complete

void setup() {
  lcd.begin(16, 2);
  Serial.begin(9600);
  lcd.print("Waiting...");
  lcd.setCursor(0,1);
  lcd.print("Run Script :)");
  lcd.setCursor(0,0);
  inputString.reserve(50);       
}

void loop() {
  if (stringComplete) {
    lcd.clear();

    int separatorIndex = inputString.indexOf('|');
    if (separatorIndex != -1) {
      String dateStr = inputString.substring(0, separatorIndex);
      String timeStr = inputString.substring(separatorIndex + 1);

      // Trim if too long for LCD 16 chars max
      if (dateStr.length() > 16) {
        dateStr = dateStr.substring(0, 16);
      }
      if (timeStr.length() > 16) {
        timeStr = timeStr.substring(0, 16);
      }

      lcd.setCursor(0, 0);
      lcd.print(dateStr);

      lcd.setCursor(0, 1);
      lcd.print(timeStr);
    }
    else {
      
      lcd.setCursor(0, 0);
      lcd.print(inputString.substring(0, 16));
    }

    
    inputString = "";
    stringComplete = false;
  }
}

void serialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    if (inChar == '\n') {
      stringComplete = true;
      break;
    } else {
      inputString += inChar;
    }
  }
}
