// src/app/models/organization.ts
import { Category } from './category';

export interface Organization {
  id: number;
  name: string;
  description: string | null;
  website: string | null;
  logo: string | null;
  address: string;
  categories: Category[];
  date_added: string;
  is_active: boolean;
  social_media_1: string | null;
  social_media_2: string | null;
  phone_number: string | null;
  email: string | null;
}
