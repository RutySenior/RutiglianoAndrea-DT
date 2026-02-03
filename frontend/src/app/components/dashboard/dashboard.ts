import { Component, OnInit } from '@angular/core';
import { DeliveryService } from '../../services/delivery';
import { Delivery } from '../../models/delivery.model';
import { CommonModule } from '@angular/common';
import { DeliveryFormComponent } from '../delivery-form/delivery-form';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [CommonModule, DeliveryFormComponent],
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