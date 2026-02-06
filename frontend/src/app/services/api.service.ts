import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class ApiService {
  private base = '/api';

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
}
