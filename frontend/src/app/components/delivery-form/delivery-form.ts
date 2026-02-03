import { Component, EventEmitter, Output } from '@angular/core';
import { Delivery } from '../../models/delivery.model';
import { DeliveryService } from '../../services/delivery';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-delivery-form',
  imports: [FormsModule, CommonModule],
  templateUrl: './delivery-form.html',
  styleUrls: ['./delivery-form.css'],
  standalone: true,
})
export class DeliveryFormComponent {
  @Output() deliveryCreated = new EventEmitter<void>();

  newDelivery: Delivery = {
    tracking_code: '',
    recipient: '',
    address: '',
    time_slot: '',
    status: 'READY',
    priority: 'LOW'
  };

  constructor(private deliveryService: DeliveryService) {}

  onSubmit() {
  this.deliveryService.createDelivery(this.newDelivery).subscribe({
    next: (res) => {
      console.log('Consegna creata!', res);
      this.deliveryCreated.emit(); // Questo serve per aggiornare la dashboard
    },
    error: (err) => console.error('Errore durante la creazione', err)
  });
}
}