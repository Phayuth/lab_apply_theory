double Vout = 0;
double Current = 0;

const double scale_factor = 0.185;

const double vRef = 5.00;
const double resConv = 1024;
double resADC = vRef/resConv;
double zeroPoint = 2.48;
void setup() {
  Serial.begin(9600);
}

void loop() {
  //read vout 1000 time
  for (int i = 0;i<1000;i++){
    Vout = (Vout +(resADC*analogRead(A4)));
    delay(1);
  }
  //get vount in mv
  Vout = Vout /1000;

  // conv Vout into current
  //Current = (Vout -zeroPoint)/scale_factor;
  Serial.print("Vout = ");
  Serial.print(Vout);
  Serial.print(" Volts");
  // Print
  //Serial.print("Vout = ");
  //Serial.print(Vout);
  //Serial.print(" Volts");
  //Serial.print("\t Current = ");
  //Serial.print(Current);
  //Serial.println(" Amps");
}
