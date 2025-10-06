import { Component } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';

import { ConsumoComponent } from './consumo/consumo';


@Component({
  selector: 'app-root',

  imports: [ HttpClientModule, ConsumoComponent],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected title = 'frontend';
}
