// src/app/services/organization-request.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

import { OrganizationRequest } from '../models/organization-request';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root',
})
export class OrganizationRequestService {
  private requestUrl = `${environment.apiUrl}/organizations/organization_requests/`;

  constructor(private http: HttpClient) {}

  submitOrganizationRequest(request: OrganizationRequest): Observable<any> {
    const formData = new FormData();
    formData.append('name', request.name);
    formData.append('description', request.description);
    formData.append('website', request.website || '');
    if (request.logo) {
      formData.append('logo', request.logo);
    }
    formData.append('address', request.address);
    request.categories.forEach((categoryId) => {
      formData.append('categories', categoryId.toString());
    });
    formData.append('social_media', request.social_media || '');
    formData.append('phone_number', request.phone_number);
    formData.append('email', request.email);

    return this.http.post<any>(this.requestUrl, formData);
  }
}
