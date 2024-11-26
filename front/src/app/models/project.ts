// src/app/models/project.ts
import { Organization } from './organization';
import { Category } from './category';
import { Image } from './image';

export interface Project {
  id: number;
  organization: Organization;
  name: string;
  description: string;
  objectives: string;
  achievements: string;
  participation_methods: string;
  images: Image[];
  categories: Category[];
  date_added: string;
  is_active: boolean;
}
