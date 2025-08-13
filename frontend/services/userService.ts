// services/productService.ts
import { useApi } from './api';
import apiUser from './apiUser';
import type { AuthResponse } from '../types/user';



export async function registerUser(payload: any): Promise<AuthResponse> {
  const api = useApi(); 
  const res = await api.post('api/registercustomeruser/', payload);
  return res.data; 
}


export async function updatePhone(payload: any): Promise<AuthResponse> {
  const api = useApi(); 
  const res = await api.put(`api/registercustomeruser/${payload.pk}/`, payload);
  return res.data; 
}

export async function getAddress(): Promise< any> {
  console.log('getAddress'); 
   const res = await apiUser.get('api/customeraddresses/');
   console.log(res.data); 
  return res.data;
}


export async function setAddress(payload: any): Promise< any> {
  
   const res = await apiUser.post('api/customeraddresses/', payload);
   console.log(res.data); 
  return res.data;
}
