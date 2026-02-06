import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { forkJoin } from 'rxjs';
import { ApiService } from '../services/api.service';

interface Stock {
  symbol: string;
  name: string;
  price: number;
  change: number;
  changePercent: number;
}

interface MarketData {
  market: string;
  type: string;
  timestamp: string;
  stocks: Stock[];
}

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './home.html',
  styleUrls: ['./home.css']
})
export class HomeComponent implements OnInit {
  usaWinners: Stock[] = [];
  usaLosers: Stock[] = [];
  milanWinners: Stock[] = [];
  milanLosers: Stock[] = [];
  switzerlandWinners: Stock[] = [];
  switzerlandLosers: Stock[] = [];
  
  loading = true;
  error = '';

  constructor(private api: ApiService) {}

  ngOnInit() {
    this.loadMarketData();
  }

  loadMarketData() {
    this.loading = true;
    this.error = '';
    
    forkJoin([
      this.api.getMarketWinners('usa'),
      this.api.getMarketLosers('usa'),
      this.api.getMarketWinners('milan'),
      this.api.getMarketLosers('milan'),
      this.api.getMarketWinners('switzerland'),
      this.api.getMarketLosers('switzerland'),
    ]).subscribe({
      next: ([usaWin, usaLose, milanWin, milanLose, swissWin, swissLose]: any[]) => {
        console.log('Data loaded:', usaWin);
        this.usaWinners = usaWin?.stocks || [];
        this.usaLosers = usaLose?.stocks || [];
        this.milanWinners = milanWin?.stocks || [];
        this.milanLosers = milanLose?.stocks || [];
        this.switzerlandWinners = swissWin?.stocks || [];
        this.switzerlandLosers = swissLose?.stocks || [];
        this.loading = false;
      },
      error: (err) => {
        console.error('Error loading market data:', err);
        this.error = 'Errore nel caricamento dei dati: ' + (err?.message || 'Sconosciuto');
        this.loading = false;
      }
    });
  }

  formatChange(changePercent: number): string {
    return changePercent >= 0 ? '+' + changePercent.toFixed(2) + '%' : changePercent.toFixed(2) + '%';
  }

  getChangeClass(changePercent: number): string {
    return changePercent >= 0 ? 'positive' : 'negative';
  }
}
