import { Component, OnInit } from '@angular/core';
import { DeliveryService } from '../../services/delivery';
import { Delivery } from '../../models/delivery.model';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.html',
  styleUrls: ['./dashboard.css']
})
export class DashboardComponent implements OnInit {
  deliveries: Delivery[] = [];

  constructor(private deliveryService: DeliveryService) { }

  ngOnInit(): void {
    this.loadDeliveries();
  }

  loadDeliveries(): void {
    this.deliveryService.getDeliveries().subscribe(data => {
      this.deliveries = data;
    });
  }
}