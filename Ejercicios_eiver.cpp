#include <iostream>
#include <cmath>
#include <vector> 
#include <string>
using namespace std;


int main(){
    cout << "Hola Mundo!"<< endl;


    int Edad = 23;
    float numeroFlotante = 10.3f;
    char caracter = 'E';
    bool Booleano = true;

    cout << "El valor de edad: "<< Edad << endl;
    cout << "El valor de numero flotante: "<< numeroFlotante << endl; 
    cout << "El valor de Caracter: "<< caracter << endl;  
    cout << "El valor de Booleano: "<< Booleano << endl; 

}


Ejercicio 2.


int main() {
    double num1, num2;

   
    cout << "Introduce el primer numero: "; cin >> num1;
    cout << "Introduce el segundo numero: "; cin >> num2;


    cout << "Suma: " << num1 + num2 << endl;
    cout << "Resta: " << num1 - num2 << endl;
    cout << "Multiplicacion: " << num1 * num2 << endl;
    
   
    if (num2 != 0) {
        cout << "Division: " << num1 / num2 << endl;
    } else {
        cout << " No se puede dividir por cero." << endl;
    }

    
    cout << "Potencia (" << num1 << " elevado a " << num2 << "): " << pow(num1, num2) << endl;
    
    if (num1 >= 0) {
        cout << "Raiz cuadrada de " << num1 << ": " << sqrt(num1) << endl;
    } else {
        cout << "Raiz cuadrada de " << num1 << ": No se puede calcular la raiz de un numero negativo." << endl;
    }

    return 0;
}


Ejercicio 3

int main(){
    int edad;

    cout<< "Que edad tienes?: "; cin >> edad;

    if(edad < 18){
        cout << "Tienes " << edad << " No puedes pasar"<< endl;
    }
    else{
        cout << "Adelante eres mayor de edad!"<< endl;
    }
}


Ejercicio 4

#define LIMITE 10

int main(){

    cout << "------------- Tablas de multiplicar----------------"<< endl;

    int numero;
    cout << "Dime un numero: "; cin >> numero;

    cout << "Tabla de multiplicar del " << numero << ":" <<endl;

    for(let i = 1; i >= LIMITE; i++){
        cout << numero << " x " << i << " = " << (numero * i) << endl;
    }
}


Ejercicio 5

int main(){
    int numeroSecreto = 26;
    int intentos = 0;
    
    cout<<"--JUEGO DE ADIVINANZAS--"<<endl;
    
    while (intentos != numeroSecreto) {
        cout << "Introduce tu intento: ";cin >> intentos;
            
        if (intentos < numeroSecreto) {
           cout << "El numero secreto es mas alto." << endl;
        } else if (intentos > numeroSecreto) {
            cout << "El numero secreto es mas bajo." << endl;
        }
        }
    
        // Este mensaje solo se muestra cuando el bucle termina
        cout << "Felicidades! Adivinaste el numero secreto: " << numeroSecreto <<endl;
    
        return 0;
    }


Ejercicio 6


int main(){
    int opcion;

    
    do {
        
        cout << "--- MENU ---" << endl;
        cout << "1. Saludar" << endl;
        cout << "2. Despedirse" << endl;
        cout << "3. Salir" << endl;
        cout << "Elige una opcion: ";cin >> opcion;

        
        switch (opcion) {
            case 1:
                cout << "Hola! Como estas?" << endl;
                break; 
            case 2:
                cout << "Adios!" << endl;
                break;
            case 3:
                cout << "Cerrando programa" << endl;
                break;
            default: 
                cout << "Opcion no valida. Por favor, intenta de nuevo." << endl;
                break;
        }

    } while (opcion != 3); 

    return 0;
}


Ejercicio 7

float calcularAreaRectangulo(float base, float altura);

int main() {
    float baseUsuario, alturaUsuario;

    
    cout << "Introduce la base del rectangulo: ";cin >> baseUsuario;
    cout << "Introduce la altura del rectangulo: ";cin >> alturaUsuario;

    float area = calcularAreaRectangulo(baseUsuario, alturaUsuario);

    cout << "El area del rectangulo es: " << area << endl;

    return 0;
}


float calcularAreaRectangulo(float base, float altura) {
    return base * altura;
}

Ejercicio 8

void modificarValor(int val) {
    cout << "  (Dentro de 'modificarValor') El valor recibido es: " << val << endl;
    val += 10;
    cout << "  (Dentro de 'modificarValor') El valor ahora es: " << val << endl;
}


void modificarReferencia(int &ref) {
    cout << "  (Dentro de 'modificarReferencia') El valor recibido es: " << ref << endl;
    ref += 10;
    cout << "  (Dentro de 'modificarReferencia') El valor ahora es: " << ref << endl;
}

int main() {
    int numero = 20;

    cout << "Valor de 'numero' ANTES de llamar a la funcion: " << numero << endl;
    modificarValor(numero);
    cout << "Valor de 'numero' DESPUES de llamar a la funcion: " << numero << " (SIN CAMBIOS)" << endl;
    
    cout << "Valor de 'numero' ANTES de llamar a la funcion: " << numero << endl;
    modificarReferencia(numero);
    cout << "Valor de 'numero' DESPUES de llamar a la funcion: " << numero << " (¡CAMBIO!)" << endl;

    return 0;
}


Ejercicio 9

int main() {
    vector<string> comidasFavoritas;
    string comidaTemporal;

    cout << "Por favor, introduce tus 3 comidas favoritas." << endl;

    for (int i = 0; i < 3; ++i) {
        cout << "Comida " << i + 1 << ": ";
        
        
        getline(cin >> ws, comidaTemporal); 
        
       
        comidasFavoritas.push_back(comidaTemporal);
    }

    cout << "--- Tus comidas favoritas ---" << endl;

    for (int i = 0; i < comidasFavoritas.size(); ++i) {
        cout << "- " << comidasFavoritas[i] << endl;
    }

    return 0;
}

Ejercicio 10

const double PI = 3.1415926535;

void calcularPerimetro(double radio);

int main() {
    double radioUsuario;

    cout << "Introduce el radio del circulo: ";cin >> radioUsuario;

    calcularPerimetro(radioUsuario);

    return 0;
}

void calcularPerimetro(double radio) {
    double perimetro = 2 * PI * radio;
    
    cout << "El perimetro del circulo es: " << perimetro <<endl;
}
