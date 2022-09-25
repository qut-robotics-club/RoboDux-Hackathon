int dir[] = {2, 8, 11, 5};
int step[] = {3, 9, 12, 6};
int sleep[] = {4, 10, 13, 7};

void setup() {
    for( int i = 0; i < sizeof(dir)/sizeof(dir[0]); i++){
        pinMode(dir[i], OUTPUT);
        pinMode(dir[i], HIGH);
    }

    for( int i = 0; i < sizeof(step)/sizeof(step[0]); i++){
        pinMode(step[i], OUTPUT);
        digitalWrite(step[i], LOW);
    }

    for( int i = 0; i < sizeof(sleep)/sizeof(sleep[0]); i++){
        pinMode(sleep[i], OUTPUT);
        digitalWrite(sleep[i], HIGH);
    }
    digitalWrite(sleep[0], HIGH);
    
    Serial.begin(115200);
    
}

void loop() {

    for( int i=0; i<4; i++){
            digitalWrite(dir[i], HIGH);
        }

    for( int i = 1; i < 1600; i++) {
        for( int i=0; i<4; i++){
            digitalWrite(step[i], HIGH);
            delayMicroseconds(200);
            digitalWrite(step[i], LOW);
            delayMicroseconds(200);
        }
    }

    for( int i=0; i<4; i++){
            digitalWrite(dir[i], LOW);
    }

    for( int i = 1; i < 1600; i++) {
        for( int i=0; i<4; i++){
            digitalWrite(step[i], HIGH);
            delayMicroseconds(200);
            digitalWrite(step[i], LOW);
            delayMicroseconds(200);
        }
    }
    // Left-Right
    digitalWrite(dir[0], HIGH);
    digitalWrite(dir[1], LOW);
    digitalWrite(dir[2], HIGH);
    digitalWrite(dir[3], LOW);

    for( int i = 1; i < 1600; i++) {
        for( int i=0; i<4; i++){
            digitalWrite(step[i], HIGH);
            delayMicroseconds(200);
            digitalWrite(step[i], LOW);
            delayMicroseconds(200);
        }
    }

    digitalWrite(dir[0], LOW);
    digitalWrite(dir[1], HIGH);
    digitalWrite(dir[2], LOW);
    digitalWrite(dir[3], HIGH);

    for( int i = 1; i < 1600; i++) {
        for( int i=0; i<4; i++){
            digitalWrite(step[i], HIGH);
            delayMicroseconds(200);
            digitalWrite(step[i], LOW);
            delayMicroseconds(200);
        }
    }


}