import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class ApiService {
  // Use direct backend URL (works in dev with CORS and in docker with nginx proxy)
  private base = 'http://127.0.0.1:8000';

  constructor(private http: HttpClient) {}

  health(): Observable<any> {
    return this.http.get(`${this.base}/health`);
  }

  quote(symbol: string): Observable<any> {
    return this.http.get(`${this.base}/quote/${encodeURIComponent(symbol)}`);
  }

  analyze(body: any): Observable<any> {
    return this.http.post(`${this.base}/analyze`, body);
  }

  getMarketWinners(market: string): Observable<any> {
    return this.http.get(`${this.base}/markets/${market}/winners`);
  }

  getMarketLosers(market: string): Observable<any> {
    return this.http.get(`${this.base}/markets/${market}/losers`);
  }
}
