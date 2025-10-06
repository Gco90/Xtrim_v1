import { Component, OnInit } from '@angular/core';
import { CommonModule, DatePipe } from '@angular/common';
import { ConsumoService } from '../services/consumo';
import { Consumo } from '../models/model';
import { catchError } from 'rxjs/operators';
import { of } from 'rxjs';
import { NgCircleProgressModule } from 'ng-circle-progress';

@Component({
  selector: 'app-consumo',
  standalone: true,
  imports: [CommonModule, DatePipe, NgCircleProgressModule],
  templateUrl: './consumo.html',
  styleUrl: './consumo.css'
})
export class ConsumoComponent implements OnInit  {
  consumo: Consumo | null = null;
  loading = false;
  error = '';

  constructor(private consumoService: ConsumoService) { }

  ngOnInit(): void {
    this.cargar();
  }

  cargar(): void {
    this.loading = true;
    this.error = '';
    this.consumoService.getConsumo()
      .pipe(
        catchError(err => {
          this.error = 'No se pudieron obtener los datos. Intenta más tarde.';
          this.loading = false;
          return of(null);
        })
      )
      .subscribe(res => {
        this.consumo = res;
        this.loading = false;
      });
  }

 getDatosPercent(): number {
    if (!this.consumo) return 0;
    return Math.min(100, Math.round((this.consumo.datos_gb / this.consumo.datos_limite_gb) * 100));
  }

  getMinutosPercent(): number {
    if (!this.consumo) return 0;
    const p = (this.consumo.minutos / this.consumo.minutos_limite) * 100;
    return Math.min(100, Math.round(p));
  }

}
