// front/src/app/com/projects/projects.component.ts

import { Component, OnInit } from '@angular/core';
import { ProjectService } from '../../services/project.service';
import { Project } from '../../models/project';
import { Category } from '../../models/category';
import { Organization } from '../../models/organization';
import { OrganizationService } from '../../services/organization.service';
import { Router, ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-projects',
  templateUrl: './projects.component.html',
  styleUrl: './projects.component.css'
})
export class ProjectsComponent implements OnInit {
  projects: Project[] = [];
  categories: Category[] = [];
  organizations: Organization[] = [];
  selectedCategory: number | null = null;
  selectedOrganization: number | null = null;
  selectedFilters: string[] = [];

  constructor(
    private projectService: ProjectService,
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

    // Obtener organizaciones para el filtro
    this.organizationService.getOrganizations().subscribe(
      (data) => {
        this.organizations = data;
      },
      (error) => console.error('Error fetching organizations', error)
    );

    // Obtener parámetros de consulta para filtros
    this.route.queryParams.subscribe(params => {
      const categoryId = params['category'] ? Number(params['category']) : null;
      const organizationId = params['organization'] ? Number(params['organization']) : null;

      if (categoryId) {
        this.selectedCategory = categoryId;
        const category = this.categories.find(cat => cat.id === categoryId);
        if (category) {
          this.selectedFilters.push(category.name);
        }
      }

      if (organizationId) {
        this.selectedOrganization = organizationId;
        const organization = this.organizations.find(org => org.id === organizationId);
        if (organization) {
          this.selectedFilters.push(organization.name);
        }
      }

      this.fetchProjects(
        categoryId !== null ? categoryId : undefined,
        organizationId !== null ? organizationId : undefined
      );
      
    });
  }

  fetchProjects(categoryId?: number, organizationId?: number) {
    this.projectService.getProjectsFiltered(categoryId, organizationId).subscribe(
      (data) => {
        this.projects = data.sort((a, b) => a.name.localeCompare(b.name));
      },
      (error) => console.error('Error fetching projects', error)
    );
  }

  onFilter() {
    // Redirigir con los filtros seleccionados como parámetros de consulta
    const queryParams: any = {};
    if (this.selectedCategory) {
      queryParams.category = this.selectedCategory;
    }
    if (this.selectedOrganization) {
      queryParams.organization = this.selectedOrganization;
    }
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
      const category = this.categories.find(cat => cat.name === filter);
      if (category) {
        this.selectedCategory = null;
      }
      const organization = this.organizations.find(org => org.name === filter);
      if (organization) {
        this.selectedOrganization = null;
      }
      this.selectedFilters.splice(index, 1);
      this.fetchProjects();
      this.router.navigate(['/projects']);
    }
  }
}
