// src/app/models/organization-request.ts
export interface OrganizationRequest {
    name: string;
    description: string;
    website: string;
    logo: File | null;
    address: string;
    categories: number[]; // IDs of selected categories
    social_media: string;
    phone_number: string;
    email: string;
  }
  