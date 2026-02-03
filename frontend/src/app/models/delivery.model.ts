export interface Delivery {
  id?: number;
  tracking_code: string;
  recipient: string;
  address: string;
  time_slot: string;
  status: 'READY' | 'OUT_FOR_DELIVERY' | 'DELIVERED' | 'FAILED';
  priority: 'LOW' | 'MEDIUM' | 'HIGH';
}