export interface Cliente {
  id: number;
  nombre: string;
}

export interface Consumo {
  cliente: Cliente;
  datos_gb: number;
  datos_limite_gb: number;
  minutos: number;
  minutos_limite: number;
  ultima_actualizacion: string;
  plan_actual : string;
  saldo_cuenta: number;
  proximo_corte: number;
  ultima_factura:number;
  sms: number;
  sms_limite: number;
}
