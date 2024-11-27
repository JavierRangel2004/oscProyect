// front/src/app/services/project.service.ts

import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';

import { Project } from '../models/project';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root',
})
export class ProjectService {
  private apiUrl = `${environment.apiUrl}/projects/projects/`;

  constructor(private http: HttpClient) {}

  getProjects(): Observable<Project[]> {
    return this.http.get<Project[]>(this.apiUrl);
  }

  getProject(id: number): Observable<Project> {
    return this.http.get<Project>(`${this.apiUrl}${id}/`);
  }

  // src/app/services/project.service.ts
  getProjectsByOrganization(organizationId: number): Observable<Project[]> {
    return this.http.get<Project[]>(`${this.apiUrl}?organization=${organizationId}`);
  }

  getProjectsFiltered(categoryId?: number, organizationId?: number): Observable<Project[]> {
    let params = new HttpParams();
    if (categoryId) {
      params = params.append('category', categoryId.toString());
    }
    if (organizationId) {
      params = params.append('organization', organizationId.toString());
    }
    return this.http.get<Project[]>(this.apiUrl, { params: params });
  }
}
