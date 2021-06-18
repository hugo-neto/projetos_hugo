#define ativador_rele_unico 13
#define ativador_rele_cima 9
#define ativador_rele_baixo 7
#define corrente_arduino 5
#define led_verde 11
#define led_vermelho 3
#define leitura A0

unsigned int tempo_inicial = 6000;
unsigned int tempo_final = 6000;
float valor;

void setup()
{
  // Habilita porta serial 9600 para leitura de dados
  Serial.begin(9600);
  pinMode(leitura, INPUT);
  pinMode(led_vermelho, OUTPUT);
  
  pinMode(led_verde, OUTPUT);
  
  pinMode(ativador_rele_cima, OUTPUT);
  pinMode(ativador_rele_baixo, OUTPUT);
  pinMode(ativador_rele_unico, OUTPUT);
  
  pinMode(corrente_arduino, OUTPUT);
}

void loop()
{
  
  // Inicia a eletrólise de BAIXA Voltagem
  
  // Define a saída pwm como analógica. Escala varia de
  // [0,255] <-> [0,5]V
  analogWrite(corrente_arduino, 0);

  // Relé duplo: HIGH fica desligado (N.F)
  digitalWrite(ativador_rele_cima, HIGH);
  digitalWrite(ativador_rele_baixo, HIGH);
  
  // Relé único: LOW fica desligado (N.F)
  digitalWrite(ativador_rele_unico, LOW);

  // Tempo de 0,2 segundo para iniciar leitura
  delay(200);

  // Lê valor da porta analógica A0 para avaliar se ele vai ou não iniciar o processo
  valor = analogRead(leitura);
  Serial.print(valor);
  Serial.println("\n");
  

 // Fica no while enquanto o botão não estiver apertado 
  while (valor < 600){
    valor = analogRead(leitura);
    Serial.print(valor);
    Serial.println("\n");
    delay(500);
    }

  // Simula saída analógica no Arduino
  // [0,255] <-> [0,5]V
  analogWrite(corrente_arduino, 200);

  digitalWrite(ativador_rele_unico, HIGH);

  digitalWrite(led_verde, HIGH);
  digitalWrite(led_vermelho, LOW); 

 
  delay(tempo_inicial);
  
  // Zera saída de 2V do Arduino
  analogWrite(corrente_arduino, 0);
  
  // Tempo de segurança
  delay(200);

  digitalWrite(led_verde, LOW);
  digitalWrite(led_vermelho, HIGH);
  
  // Inicia a eletrólise de ALTA Voltagem
  digitalWrite(ativador_rele_cima, LOW);
  digitalWrite(ativador_rele_baixo, LOW);
  digitalWrite(ativador_rele_unico, LOW);
  
  delay(tempo_final);

  digitalWrite(led_vermelho, LOW);
  
  digitalWrite(ativador_rele_cima, HIGH);
  digitalWrite(ativador_rele_baixo, HIGH);
  digitalWrite(ativador_rele_unico, LOW);

  // Gera uma varíavel booleana para caso seja necessário reiniciar o processo
  bool condi = true;
  while (condi == true){
    delay(1000);
    
    valor = analogRead(leitura);
    
    Serial.print(valor);
    Serial.println("\n");

    // Caso o botão esteja apertado na hora, ele começa a função novamente
    if (valor >= 600){
    loop();
    }
    
    }
  
  
}
  
