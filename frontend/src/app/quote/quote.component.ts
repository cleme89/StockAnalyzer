import { Component, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ApiService } from '../services/api.service';

@Component({
  selector: 'app-quote',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './quote.html',
  styleUrls: ['./quote.css']
})
export class QuoteComponent {
  symbol = 'AAPL';
  loading = signal(false);
  quote: any = null;

  constructor(private api: ApiService) {}

  getQuote() {
    this.loading.set(true);
    this.quote = null;
    this.api.quote(this.symbol).subscribe({
      next: (r) => {
        this.quote = r;
        this.loading.set(false);
      },
      error: (e) => {
        this.quote = { error: e?.message ?? e };
        this.loading.set(false);
      }
    });
  }
}
