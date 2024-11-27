// src/app/com/signin/signin.component.ts

import { Component } from '@angular/core';
import { AuthService } from '../../services/auth.service';
import { Router } from '@angular/router';
import { HttpErrorResponse } from '@angular/common/http';

@Component({
  selector: 'app-signin',
  templateUrl: './signin.component.html',
  styleUrls: ['./signin.component.css']
})
export class SigninComponent {
  username = '';
  password = '';
  errorMessage = '';

  constructor(private authService: AuthService, private router: Router) {}

  onSubmit() {
    this.authService.login(this.username, this.password).subscribe({
      next: (response) => {
        if (response.access && response.refresh) {
          localStorage.setItem('access_token', response.access);
          localStorage.setItem('refresh_token', response.refresh);
          window.location.href = 'http://localhost:8000/admin/'; // Redirect to Django admin
        }
      },
      error: (error: HttpErrorResponse) => {
        console.error('Error during login:', error);
        this.errorMessage = error.error?.message || 'An error occurred during login.';
      },
    });
  }  
  }
  

