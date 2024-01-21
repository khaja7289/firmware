#include <avr/eeprom.h>

const int chunk_size = 32; 
char buffer[chunk_size];
int buffer_index = 0;
int eeprom_address = 0;

void setup() {
  Serial.begin(2400);
}

void loop() {
  while (Serial.available()) {
    char data = Serial.read();
    buffer[buffer_index++] = data;
    
    if (buffer_index == chunk_size || data == '\0') {
      eeprom_write_block(buffer, (void *)eeprom_address, buffer_index);
      eeprom_address += buffer_index;
      buffer_index = 0;
    }
  }

  if (!Serial.available() && eeprom_address > 0) {
    for (int i = 0; i < eeprom_address; i++) {
      char data = eeprom_read_byte((const uint8_t *)i);
      Serial.write(data);
    }
    eeprom_address = 0;
  }
}
