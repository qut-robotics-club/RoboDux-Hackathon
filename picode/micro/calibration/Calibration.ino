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
        digitalWrite(sleep[i], LOW);
    }
    digitalWrite(sleep[0], HIGH);
    
    Serial.begin(115200);
    
}

void loop() {

    for(int i=1; i<1600; i++){
        digitalWrite(step[0], HIGH);
        delayMicroseconds(150);
        digitalWrite(step[0], LOW);
        delayMicroseconds(150);
    }

    digitalWrite(dir[0], HIGH);

    for(int i=1; i<1600; i++){
        digitalWrite(step[0], HIGH);
        delayMicroseconds(150);
        digitalWrite(step[0], LOW);
        delayMicroseconds(150);
    }
    digitalWrite(dir[0], LOW);
    digitalWrite(sleep[0], LOW);
    digitalWrite(sleep[1], HIGH);
    
    for(int i=1; i<800; i++){
        digitalWrite(step[1], HIGH);
        delayMicroseconds(150);
        digitalWrite(step[1], LOW);
        delayMicroseconds(150);
    }

    digitalWrite(dir[1], HIGH);

    for(int i=1; i<800; i++){
        digitalWrite(step[1], HIGH);
        delayMicroseconds(150);
        digitalWrite(step[1], LOW);
        delayMicroseconds(150);
    }

    digitalWrite(dir[1], LOW);
    digitalWrite(sleep[1], LOW);
    digitalWrite(sleep[2], HIGH);

        for(int i=1; i<800; i++){
        digitalWrite(step[2], HIGH);
        delayMicroseconds(150);
        digitalWrite(step[2], LOW);
        delayMicroseconds(150);
    }

    digitalWrite(dir[2], HIGH);

    for(int i=1; i<800; i++){
        digitalWrite(step[2], HIGH);
        delayMicroseconds(150);
        digitalWrite(step[2], LOW);
        delayMicroseconds(150);
    }

    digitalWrite(dir[2], LOW);
    digitalWrite(sleep[2], LOW);
    digitalWrite(sleep[3], HIGH);

        for(int i=1; i<800; i++){
        digitalWrite(step[3], HIGH);
        delayMicroseconds(150);
        digitalWrite(step[3], LOW);
        delayMicroseconds(150);
    }

    digitalWrite(dir[3], HIGH);

    for(int i=1; i<800; i++){
        digitalWrite(step[3], HIGH);
        delayMicroseconds(150);
        digitalWrite(step[3], LOW);
        delayMicroseconds(150);
    }
    digitalWrite(dir[3],LOW);
    digitalWrite(dir[0], LOW);
    digitalWrite(sleep[3], LOW);
    digitalWrite(sleep[0], HIGH);

}