import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Delivery } from '../models/delivery.model';

@Injectable({
  providedIn: 'root'
})
export class DeliveryService {
  private apiUrl = 'https://cuddly-guide-wrv6pjp7w7rp3gqx6-5000.app.github.dev/deliveries';

  constructor(private http: HttpClient) { }

  getDeliveries(): Observable<Delivery[]> {
    return this.http.get<Delivery[]>(this.apiUrl);
  }

  createDelivery(delivery: Delivery): Observable<any> {
    return this.http.post(this.apiUrl, delivery);
  }

  updateStatus(id: number, status: string): Observable<any> {
    return this.http.put(`${this.apiUrl}/${id}/status`, { status });
  }
}