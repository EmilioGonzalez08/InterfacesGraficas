#include <iostream>

class Cuenta {
private:
    long int numero_cuenta;
    float saldo;
    float interes_anual;

public:
    void inicializar(long int num);
    float dar_saldo();
    float dar_interes();
    void mod_saldo(float s);
    void mod_interes(float i);
    void ingreso(float cantidad);
    bool reintegro(float r);
    void mostrar_datos();
    void abono_intereses();
};

void Cuenta::inicializar(long int num) {
    numero_cuenta = num;
    saldo = 0;
    interes_anual = 0;
}

float Cuenta::dar_saldo() {
    return saldo;
}

float Cuenta::dar_interes() {
    return interes_anual;
}

void Cuenta::mod_saldo(float s) {
    saldo = s;
}

void Cuenta::mod_interes(float i) {
    interes_anual = i;
}

void Cuenta::ingreso(float cantidad) {
    saldo += cantidad;
}

bool Cuenta::reintegro(float r) {
    if (r > saldo) {
        return false;
    } else {
        saldo -= r;
        return true;
    }
}

void Cuenta::mostrar_datos() {
    std::cout << "Nº de cuenta: " << numero_cuenta << std::endl;
    std::cout << "Saldo: " << saldo << std::endl;
}

void Cuenta::abono_intereses() {
    float cantidad;
    cantidad = (saldo * interes_anual) / 100;
    ingreso(cantidad);
}

int main() {
    Cuenta cc;  // cc es un objeto de la clase Cuenta
    cc.inicializar(24316622);
    cc.mod_saldo(10000);
    cc.mod_interes(2);
    cc.mostrar_datos();
    cc.ingreso(12000);
    cc.mostrar_datos();
    bool b;
    b = cc.reintegro(10000);
    if (b == false) {
        std::cout << "No hay saldo" << std::endl;
    }
    cc.mostrar_datos();
    return 0;
}
