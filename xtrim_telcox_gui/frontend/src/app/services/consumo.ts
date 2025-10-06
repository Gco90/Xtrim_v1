import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environment';
import { Consumo } from '../models/model';


@Injectable({
  providedIn: 'root'
})
export class ConsumoService {
   // Extraigo del environment la URL de la API de Flask
  private base =environment.apiUrl;

  //Se inyecta el httpclient
  constructor(private http : HttpClient){ }

  getConsumo():Observable<Consumo>{
    return this.http.get<Consumo>(`${this.base}/consumo`);
  }

  
}
