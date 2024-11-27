// src/app/services/auth.service.ts

import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { HttpInterceptor, HttpRequest, HttpHandler } from '@angular/common/http';

interface LoginResponse {
    access?: string;
    refresh?: string;
    error?: string; // Optional property to capture error messages
  }
  

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  private loginUrl = 'http://localhost:8000/api/auth/login/';

  constructor(private http: HttpClient) {}

  login(username: string, password: string): Observable<LoginResponse> {
    const body = { username, password };
    return this.http.post<LoginResponse>(this.loginUrl, body, { withCredentials: true }); // Ensure credentials are included
  }  

}
