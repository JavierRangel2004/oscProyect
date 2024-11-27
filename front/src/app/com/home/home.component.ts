// src/app/com/home/home.component.ts
import { Component, OnInit } from '@angular/core';
import { Category } from '../../models/category';
import { OrganizationService } from '../../services/organization.service';
import { OrganizationRequestService } from '../../services/organization-request.service';
import { OrganizationRequest } from '../../models/organization-request';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent implements OnInit {
  categories: Category[] = [];
  organizationRequest: OrganizationRequest = {
    name: '',
    description: '',
    website: '',
    logo: null,
    address: '',
    categories: [],
    social_media: '',
    phone_number: '',
    email: ''
  };
  successMessage: string = '';
  errorMessage: string = '';

  constructor(
    private organizationService: OrganizationService,
    private organizationRequestService: OrganizationRequestService
  ) {}

  ngOnInit(): void {
    this.organizationService.getCategories().subscribe(
      (data) => {
        this.categories = data;
      },
      (error) => console.error('Error fetching categories', error)
    );
  }

  onSubmit() {
    this.organizationRequestService.submitOrganizationRequest(this.organizationRequest).subscribe(
      (response) => {
        this.successMessage = 'Solicitud enviada exitosamente.';
        this.errorMessage = '';
        // Reset the form
        this.organizationRequest = {
          name: '',
          description: '',
          website: '',
          logo: null,
          address: '',
          categories: [],
          social_media: '',
          phone_number: '',
          email: ''
        };
      },
      (error) => {
        console.error('Error submitting organization request', error);
        this.errorMessage = 'Hubo un error al enviar la solicitud.';
        this.successMessage = '';
      }
    );
  }

  onFileChange(event: any) {
    if (event.target.files.length > 0) {
      this.organizationRequest.logo = event.target.files[0];
    }
  }
}
