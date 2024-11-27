// front/src/app/com/organizations/organizations.component.ts

import { Component, OnInit } from '@angular/core';
import { OrganizationService } from '../../services/organization.service';
import { Organization } from '../../models/organization';
import { Category } from '../../models/category';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-organizations',
  templateUrl: './organizations.component.html',
  styleUrl: './organizations.component.css'
})
export class OrganizationsComponent implements OnInit {
  organizations: Organization[] = [];
  categories: Category[] = [];
  selectedCategory: number | null = null;
  selectedFilters: string[] = [];

  constructor(
    private organizationService: OrganizationService,
    private route: ActivatedRoute,
    private router: Router
  ) {}

  ngOnInit(): void {
    // Obtener categorías para el filtro
    this.organizationService.getCategories().subscribe(
      (data) => {
        this.categories = data;
      },
      (error) => console.error('Error fetching categories', error)
    );

    // Obtener parámetros de consulta para filtros
    this.route.queryParams.subscribe(params => {
      const categoryId = params['category'] ? Number(params['category']) : null;
      if (categoryId) {
        this.selectedCategory = categoryId;
        this.selectedFilters.push(this.categories.find(cat => cat.id === categoryId)?.name || 'Categoría desconocida');
        this.fetchOrganizations(categoryId);
      } else {
        this.fetchOrganizations();
      }
    });
  }

  fetchOrganizations(categoryId?: number) {
    if (categoryId) {
      this.organizationService.getOrganizations(categoryId).subscribe(
        (data) => {
          this.organizations = data.sort((a, b) =>
            a.name.localeCompare(b.name)
          );
        },
        (error) => console.error('Error fetching organizations', error)
      );
    } else {
      this.organizationService.getOrganizations().subscribe(
        (data) => {
          this.organizations = data.sort((a, b) =>
            a.name.localeCompare(b.name)
          );
        },
        (error) => console.error('Error fetching organizations', error)
      );
    }
  }

  onFilter() {
    // Redirigir con los filtros seleccionados como parámetros de consulta
    const queryParams: any = {};
    if (this.selectedCategory) {
      queryParams.category = this.selectedCategory;
    }
    // Puedes añadir más filtros aquí si es necesario
    this.router.navigate([], {
      relativeTo: this.route,
      queryParams: queryParams,
      queryParamsHandling: 'merge'
    });
  }

  // Método para eliminar un filtro seleccionado
  removeFilter(filter: string) {
    const index = this.selectedFilters.indexOf(filter);
    if (index > -1) {
      this.selectedFilters.splice(index, 1);
      // Resetear el filtro
      this.selectedCategory = null;
      this.fetchOrganizations();
      this.router.navigate(['/organizations']);
    }
  }
}
