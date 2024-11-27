// front/src/app/services/organization.service.ts

import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';

import { Organization } from '../models/organization';
import { Category } from '../models/category'; // Import Category interface
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root',
})
export class OrganizationService {
  private apiUrl = `${environment.apiUrl}/organizations/organizations/`;
  private categoriesUrl = `${environment.apiUrl}/organizations/categories/`; // Added this line

  constructor(private http: HttpClient) {}

  getOrganizations(categoryId?: number): Observable<Organization[]> {
    let params = new HttpParams();
    if (categoryId) {
      params = params.append('category', categoryId.toString());
    }
    return this.http.get<Organization[]>(this.apiUrl, { params: params });
  }

  getOrganization(id: number): Observable<Organization> {
    return this.http.get<Organization>(`${this.apiUrl}${id}/`);
  }

  getCategories(): Observable<Category[]> {
    return this.http.get<Category[]>(this.categoriesUrl);
  }
}
